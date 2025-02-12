# Packages import
from fastapi import FastAPI
from typing import Optional

# Application imports
from api.v1.books import books_router
from schemas.posts import Post

app = FastAPI()

# Include routers
app.include_router(books_router, prefix="/books", tags=["books"])


@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}


@app.get("/greet/{name}")
async def greet(name: str) -> dict:
    return {"message": f"Hello {name}"}


@app.get("/greet")
async def greet_query(name: Optional[str] = None) -> dict:
    return {"message": f"Hello {name}"}


@app.post("/create_post")
async def create_post(post: Post) -> dict:
    try:
        return {
            "message": post.dict(),
        }
    except Exception as e:
        print(f"Error while creating post: {e}")
        return {"error": e}
