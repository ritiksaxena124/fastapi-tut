from fastapi import APIRouter
from constants.books import books
books_router = APIRouter()

@books_router.get('')
async def get_books():
    return books