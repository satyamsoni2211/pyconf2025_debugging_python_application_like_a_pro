from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from service import create_book, get_books, get_book, update_book, delete_book

router = APIRouter()


@router.post("/books/")
def add_book(title: str, author: str, db: Session = Depends(get_db)):
    return create_book(db, title, author)


@router.get("/books/")
def list_books(db: Session = Depends(get_db)):
    return get_books(db)


@router.get("/books/{book_id}")
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.put("/books/{book_id}")
def edit_book(book_id: int, title: str, author: str, db: Session = Depends(get_db)):
    book = update_book(db, book_id, title, author)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/books/{book_id}")
def remove_book(book_id: int, db: Session = Depends(get_db)):
    book = delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
