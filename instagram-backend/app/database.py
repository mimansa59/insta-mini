from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

# No 'certifi', no 'tls' arguments needed for local DB
client = AsyncIOMotorClient(settings.MONGO_URI)
db = client[settings.DB_NAME]

# Collections
users_collection = db["users"]
posts_collection = db["posts"]
comments_collection = db["comments"]

# Indexes
async def create_indexes():
    try:
        await users_collection.create_index("username", unique=True)
        await users_collection.create_index("email", unique=True)
        await posts_collection.create_index("user_id")
    except Exception as e:
        print(f"Index creation warning: {e}")