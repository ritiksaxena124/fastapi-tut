# Packages import
from fastapi import FastAPI, Response, status, HTTPException
from typing import Optional
from uuid import uuid4

# Application imports
from api.v1.books import books_router
from schemas.posts import Post

app = FastAPI()

# Include routers
app.include_router(books_router, prefix="/books", tags=["books"])


posts = [
    {
        "id": "f1f4df8a-9f69-4f90-a1f5-7569cbeabe1d",
        "title": "Title 1",
        "content": "Content of post 1",
        "author": "Anonymous",
        "rating": 5,
    }
]


@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}


@app.get("/greet/{name}")
async def greet(name: str) -> dict:
    return {"message": f"Hello {name}"}


@app.get("/greet")
async def greet_query(name: Optional[str] = None) -> dict:
    return {"message": f"Hello {name}"}


@app.post("/create_post", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post) -> dict:
    try:
        new_post = post.dict()
        new_post["id"] = uuid4()
        posts.append(new_post)
        return {
            "data": posts,
        }
    except Exception as e:
        print(f"Error while creating post: {e}")
        return {"error": e}


@app.get("/posts")
async def get_posts():
    try:
        return {"data": posts}
    except Exception as e:
        print(f"Error in getting all posts: {e}")


@app.get("/posts/{post_id}")
async def get_post(post_id: str, response: Response):
    try:
        for post in posts:
            if post["id"] == post_id:
                return {"data": post}

        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Post with id: {post_id} doesn't exists"}
        # OR
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {post_id} doesn't exists",
        )
    except Exception as e:
        print(f"Error in getting post by id: {e}")
        return {"error": e}
