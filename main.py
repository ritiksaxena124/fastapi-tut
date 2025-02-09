from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}


@app.get("/greet/{name}")
async def greet(name: str) -> dict:
    return {"message": f"Hello {name}"}


@app.get("/greet")
async def greet_query(name: Optional[str] = None) -> dict:
    return {"message": f"Hello {name}"}


class Book(BaseModel):
    title: str
    author: str


@app.post("/books")
async def add_book(book: Book) -> dict:
    return {
        "message": f"Book '{book.title}' whose author is '{book.author}' is added to library",
    }
