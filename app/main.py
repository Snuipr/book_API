from app import utils_db
from app.schemas import Book, User
from fastapi import FastAPI
from typing import Optional


app = FastAPI()

@app.get("/book/")
def get_book(book_id: Optional[int] = None, book_name: Optional[str] = None,
             category: Optional[str] = None, book_year: Optional[int] = None,
             author: Optional[str] = None):
    return utils_db.get_books(book_id, book_name, category, book_year, author)

@app.get("/book_text/")
def get_book_text(book_name: str):
    return utils_db.get_book_text(book_name)

@app.post("/add_book")
def add_book(book_body: Book.Book_add):
    return utils_db.add_book(book_body)

@app.post("/add_book_text")
def add_book_text(book_body: Book.Book_text):
    return utils_db.add_book_text(book_body)

@app.post("/register")
def add_user(user_body: User):
    return utils_db.add_user(user_body)

@app.put("/update_book")
def update_book(book_body: Book.Book_update):
    return utils_db.update_book(book_body)

@app.put("/update_book_text")
def update_book_text(book_body: Book.Book_text):
    return utils_db.update_book_text(book_body)

@app.put("/authorization")
def authorization_user(user_body: User):
    return utils_db.authoriz_user(user_body)

@app.delete("/delete_user")
def del_user(user_body: User):
    return utils_db.delete_user(user_body)

@app.delete("/delete_book")
def del_book(del_body: Book.Book_delete):
    return utils_db.delete_book(del_body)