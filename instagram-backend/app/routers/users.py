from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_current_user
from app.database import users_collection
from app.models.user import UserResponse
from bson import ObjectId

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/follow/{target_user_id}")
async def follow_user(target_user_id: str, current_user: UserResponse = Depends(get_current_user)):
    if target_user_id == current_user.id:
        raise HTTPException(status_code=400, detail="You cannot follow yourself")
    
    # Add target to current user's following
    await users_collection.update_one(
        {"_id": ObjectId(current_user.id)},
        {"$addToSet": {"following": target_user_id}}
    )
    
    # Add current user to target's followers
    await users_collection.update_one(
        {"_id": ObjectId(target_user_id)},
        {"$addToSet": {"followers": current_user.id}}
    )
    return {"message": "Followed successfully"}

@router.post("/unfollow/{target_user_id}")
async def unfollow_user(target_user_id: str, current_user: UserResponse = Depends(get_current_user)):
    # Remove target from current user's following
    await users_collection.update_one(
        {"_id": ObjectId(current_user.id)},
        {"$pull": {"following": target_user_id}}
    )
    
    # Remove current user from target's followers
    await users_collection.update_one(
        {"_id": ObjectId(target_user_id)},
        {"$pull": {"followers": current_user.id}}
    )
    return {"message": "Unfollowed successfully"}

@router.get("/{username}", response_model=UserResponse)
async def get_user_profile(username: str):
    user = await users_collection.find_one({"username": username})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user