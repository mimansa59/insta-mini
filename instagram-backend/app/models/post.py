from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from app.models.base import MongoBaseModel

class PostCreate(BaseModel):
    image_url: str
    caption: str

class CommentCreate(BaseModel):
    text: str

class CommentResponse(MongoBaseModel):
    user_id: str
    username: str
    text: str
    created_at: datetime

class PostResponse(MongoBaseModel):
    user_id: str
    username: str
    image_url: str
    caption: str
    likes: List[str] = []
    comments: List[CommentResponse] = []
    created_at: datetime