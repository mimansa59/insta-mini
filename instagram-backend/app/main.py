from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import  users, posts , auth
from app.database import create_indexes

app = FastAPI(title="Instagram Mini Clone")

# CORS (Allow Frontend to talk to Backend)
origins = [
    "http://localhost:3000", # Next.js / React
    "http://localhost:5173", # Vite
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(posts.router)

@app.on_event("startup")
async def startup_db_client():
    await create_indexes()

@app.get("/")
def root():
    return {"message": "Instagram Clone API is running"}