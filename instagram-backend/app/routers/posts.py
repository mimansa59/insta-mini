from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.dependencies import get_current_user
from app.database import posts_collection, comments_collection, users_collection
from app.models.post import PostCreate, PostResponse, CommentCreate, CommentResponse
from app.models.user import UserResponse
from datetime import datetime
from bson import ObjectId

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/", response_model=PostResponse)
async def create_post(post: PostCreate, current_user: UserResponse = Depends(get_current_user)):
    post_dict = post.dict()
    post_dict["user_id"] = current_user.id
    post_dict["username"] = current_user.username
    post_dict["created_at"] = datetime.utcnow()
    post_dict["likes"] = []
    
    result = await posts_collection.insert_one(post_dict)
    created_post = await posts_collection.find_one({"_id": result.inserted_id})
    return created_post

@router.get("/feed", response_model=List[PostResponse])
async def get_feed(current_user: UserResponse = Depends(get_current_user)):
    # 1. Get users following + self
    following = current_user.following
    following.append(current_user.id)
    
    # 2. Fetch posts
    cursor = posts_collection.find({"user_id": {"$in": following}})\
                             .sort("created_at", -1).limit(50)
    
    posts = await cursor.to_list(length=50)
    
    # 3. Attach comments manually (MongoDB doesn't join easily)
    for post in posts:
        post_comments = await comments_collection.find({"post_id": str(post["_id"])}).to_list(length=10)
        post["comments"] = post_comments

    return posts

@router.post("/{post_id}/like")
async def like_post(post_id: str, current_user: UserResponse = Depends(get_current_user)):
    await posts_collection.update_one(
        {"_id": ObjectId(post_id)},
        {"$addToSet": {"likes": current_user.id}}
    )
    return {"message": "Post liked"}

@router.post("/{post_id}/unlike")
async def unlike_post(post_id: str, current_user: UserResponse = Depends(get_current_user)):
    await posts_collection.update_one(
        {"_id": ObjectId(post_id)},
        {"$pull": {"likes": current_user.id}}
    )
    return {"message": "Post unliked"}

@router.post("/{post_id}/comment", response_model=CommentResponse)
async def add_comment(post_id: str, comment: CommentCreate, current_user: UserResponse = Depends(get_current_user)):
    comment_dict = {
        "post_id": post_id,
        "user_id": current_user.id,
        "username": current_user.username,
        "text": comment.text,
        "created_at": datetime.utcnow()
    }
    result = await comments_collection.insert_one(comment_dict)
    created_comment = await comments_collection.find_one({"_id": result.inserted_id})
    return created_comment