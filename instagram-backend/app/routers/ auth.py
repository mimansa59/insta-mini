from fastapi import APIRouter, HTTPException, status
from app.models.user import UserCreate, UserLogin
from app.database import users_collection
from app.utils.security import get_password_hash, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/signup")
async def signup(user: UserCreate):
    # Check if user exists
    existing_user = await users_collection.find_one({"$or": [{"email": user.email}, {"username": user.username}]})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or Email already registered")

    user_dict = user.dict()
    user_dict["password_hash"] = get_password_hash(user_dict.pop("password"))
    user_dict["followers"] = []
    user_dict["following"] = []
    
    result = await users_collection.insert_one(user_dict)
    return {"message": "User created successfully", "id": str(result.inserted_id)}

@router.post("/login")
async def login(form_data: UserLogin): # Can also use OAuth2PasswordRequestForm
    user = await users_collection.find_one({"username": form_data.username})
    if not user or not verify_password(form_data.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}