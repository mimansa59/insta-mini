from pydantic import BaseModel, EmailStr
from typing import List, Optional
from app.models.base import MongoBaseModel

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(MongoBaseModel):
    username: str
    email: EmailStr
    followers: List[str] = []
    following: List[str] = []