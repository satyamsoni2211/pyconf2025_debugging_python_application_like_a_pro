from sqlalchemy.orm import Session
from models import Book


def create_book(db: Session, title: str, author: str):
    book = Book(title=title, author=author)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_books(db: Session):
    # TODO: Fix this query
    query = db.query(Book.title)
    return query.all()


def get_book(db: Session, book_id: int):
    # TODO: Fix this query
    book = db.query(Book).filter(book_id == book_id).first()
    return book


def update_book(db: Session, book_id: int, title: str, author: str):
    book = db.query(Book).filter(Book.id == book_id).one_or_none()
    if not book:
        return None
    # TODO: Fix this update
    book.title = author
    book.author = title
    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return None
    db.delete(book)
    db.commit()
    return book
