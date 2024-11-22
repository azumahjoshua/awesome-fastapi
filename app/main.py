from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from random import randrange
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, users , auth, vote
from .config import Settings

# models.Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# # Pydantic model for input validation
# class PostCreate(BaseModel):
#     title: str
#     content: str
#     published: bool = True

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/test")
async def test_posts(db:Session = Depends(get_db)):
    return {"status" :"success"}


