from pydantic import BaseModel, Field
from typing import Optional


class Book():
    class Book_add(BaseModel):
        user_name: str = Field(..., min_length=5, max_length=50, description="Логин", examples=[None])
        password: str = Field(..., min_length=5, max_length=50, description="Пароль", examples=[None])
        book_name: str = Field(..., min_length=3, max_length=50, description="Название книги", examples=[None])
        category: str = Field(..., min_length=4, max_length=50, description="Категория книги", examples=[None])
        book_year: int = Field(..., ge=1600, description="Год выпуска книги", examples=[None])
        author: str = Field(..., min_length=5, max_length=50, description="Автор книги", examples=[None])

    class Book_update(BaseModel):
        user_name: str = Field(..., min_length=5, max_length=50, description="Логин", examples=[None])
        password: str = Field(..., min_length=5, max_length=50, description="Пароль", examples=[None])
        book_name: str = Field(..., min_length=3, max_length=50, description="Название книги", examples=[None])
        new_book_name: Optional[str] = Field(min_length=3, max_length=50, description="Новое название книги", examples=[None])
        new_category: Optional[str] = Field(min_length=4, max_length=50, description="Новая Категория книги", examples=[None])
        new_book_year: Optional[int] = Field(ge=1600, description="Новый год выпуска книги", examples=[None])
        new_author: Optional[str] = Field(min_length=5, max_length=50, description="Новый автор книги", examples=[None])

    class Book_delete(BaseModel):
        user_name: str = Field(..., min_length=5, max_length=50, description="Логин", examples=[None])
        password: str = Field(..., min_length=5, max_length=50, description="Пароль", examples=[None])
        book_name: str = Field(..., min_length=5, max_length=50, description="Название книги", examples=[None])

    class Book_info(BaseModel):
        user_name: str = Field(..., min_length=5, max_length=50, description="Логин", examples=[None])
        password: str = Field(..., min_length=5, max_length=50, description="Пароль", examples=[None])
        book_text: str = Field(..., description="Содержание книги", examples=["Тут должен быть текст"])

class User(BaseModel):
    user_name: str = Field(min_length=5, max_length=50, description="Логин", examples=[None])
    password: str = Field(min_length=5, max_length=50, description="Пароль", examples=[None])
