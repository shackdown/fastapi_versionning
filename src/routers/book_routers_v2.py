import json
from fastapi import APIRouter
from models.book_models_v2 import Book

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "not found"}},
)

@router.get("/{book_id}", response_model=Book)
async def get_book(book_id):
    books = []
    with open("data/book_v2.json", "r") as file:
        books = json.load(file)
    
    return Book.model_validate(books[book_id])
