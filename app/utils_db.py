import psycopg2
from app.schemas import Book, User
from typing import Optional

def get_books(book_id: Optional[int] = None, book_name: Optional[str] = None,
             category: Optional[str] = None, book_year: Optional[int] = None,
             author: Optional[str] = None):
    try:
        conn = psycopg2.connect(dbname="API", user="postgres", password="1", host="localhost", port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        result = []
        filter_result = cursor.fetchall()
        cursor.close()
        conn.close()
        if book_id:
            filter_result = [book for book in filter_result if book[0] == book_id]
        if book_name:
            filter_result = [book for book in filter_result if book[2] == book_name]
        if category:
            filter_result = [book for book in filter_result if book[3] == category]
        if book_year:
            filter_result = [book for book in filter_result if book[4] == book_year]
        if author:
            filter_result = [book for book in filter_result if book[5] == author]
        cursor.close()
        conn.close()
        if filter_result:
            for book in filter_result:
                result.append({
                        "id": book[0],
                        "user_id": book[1],
                        "book_name": book[2],
                        "category": book[3],
                        "book_year": book[4],
                        "author": book[5]
                })
        return result
    except Exception as error:
        raise error

def add_books(add_body: Book.Book_add):
    try:
        conn = psycopg2.connect(dbname="API", user="postgres", password="1", host="localhost", port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_name = %s AND password = %s", (add_body.user_name, add_body.password))
        result = cursor.fetchall()
        if not result:
            cursor.close()
            conn.close()
            return "Неверный логин или пароль"
        cursor.execute("SELECT * FROM books WHERE book_name = %s", (add_body.book_name,))
        result = cursor.fetchall()
        if result:
            cursor.close()
            conn.close()
            return "Эта книга уже существует"
        cursor.execute("INSERT INTO books(user_name, book_name, category, book_year, author)"
                       "VALUES(%s, %s, %s, %s, %s)",
                       (add_body.user_name, add_body.book_name, add_body.category, add_body.book_year, add_body.author))
        conn.commit()
        cursor.close()
        conn.close()
        return "Книга успешно добавлена"
    except Exception as error:
        raise error

def update_book(update_body: Book.Book_update):
    try:
        conn = psycopg2.connect(dbname="API", user="postgres", password="1", host="localhost", port="5432")
        cursor = conn.cursor()
        conn.autocommit = True
        cursor.execute("SELECT * FROM users WHERE user_name = %s  AND password = %s",
                       (update_body.user_name, update_body.password))
        result = cursor.fetchall()
        if not result:
            cursor.close()
            conn.close()
            return "Неверный логин или пароль"
        else:
            cursor.execute("SELECT * FROM books WHERE user_name = %s AND book_name = %s",
                           (update_body.user_name, update_body.book_name))
            result = cursor.fetchall()
            if result:
                if update_body.new_category:
                    cursor.execute("UPDATE books SET category = %s WHERE book_name = %s",
                                   (update_body.new_category, update_body.book_name))
                if update_body.new_book_year:
                    cursor.execute("UPDATE books SET book_year = %s WHERE book_name = %s",
                                   (update_body.new_book_year, update_body.book_name))
                if update_body.new_author:
                    cursor.execute("UPDATE books SET author = %s WHERE book_name = %s",
                                   (update_body.new_author, update_body.book_name))
                if update_body.new_book_name:
                    cursor.execute("UPDATE books SET book_name = %s WHERE book_name = %s",
                                   (update_body.new_book_name, update_body.book_name))
                cursor.close()
                conn.close()
                return f"Успешно обновлено {update_body.book_name}"
            cursor.close()
            conn.close()
            return "Вы не владелец книги или такой книги не существует"
    except Exception as error:
        raise error

def delete_book(del_body: Book.Book_delete):
    try:
        conn = psycopg2.connect(dbname="API", user="postgres", password="1", host="localhost", port="5432")
        cursor = conn.cursor()
        conn.autocommit = True
        cursor.execute("SELECT * FROM users WHERE user_name = %s  AND password = %s",
                       (del_body.user_name, del_body.password))
        result = cursor.fetchall()
        if not result:
            cursor.close()
            conn.close()
            return "Неверный логин или пароль"
        else:
            cursor.execute("SELECT * FROM books WHERE user_name = %s AND book_name = %s",
                           (del_body.user_name, del_body.book_name))
            result = cursor.fetchall()
            if result:
                cursor.execute("DELETE FROM books WHERE user_name = %s AND book_name = %s",
                               (del_body.user_name, del_body.book_name))
                cursor.close()
                conn.close()
                return f"Вы успешно удалили книгу - {del_body.book_name}"
            cursor.close()
            conn.close()
            return "Вы не владелец книги или такой книги не существует"
    except Exception as error:
        raise error

def add_books_info(add_body: Book.Book_info):
    try:
        conn = psycopg2.connect(dbname="API", user="postgres", password="1", host="localhost", port="5432")
        cursor = conn.cursor()
        conn.autocommit = True
        cursor.execute("SELECT * FROM users WHERE user_name = %s  AND password = %s",
                       (add_body.user_name, add_body.password))
        result = cursor.fetchall()
        if not result:
            cursor.close()
            conn.close()
            return "Неверный логин или пароль"
        else:
            cursor.execute("SELECT * FROM books WHERE user_name = %s AND book_name = %s",
                           (add_body.user_name, add_body.book_name))
            result = cursor.fetchall()
            if result:
                cursor.execute("INSERT INTO books_text(user_name, password, book_text) VALUES(%s, %s, %s)",
                               (add_body.user_name, add_body.password, add_body.book_text))
                cursor.close()
                conn.close()
                return f"Вы успешно добавили текст в книгу - {add_body.book_name}"
            cursor.close()
            conn.close()
            return "Вы не владелец книги или такой книги не существует"
    except Exception as error:
        raise error

def add_users(add_body: User):
    try:
        conn = psycopg2.connect(dbname="API", user="postgres", password="1", host="localhost", port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_name = %s", (add_body.user_name,))
        result = cursor.fetchall()
        if result:
            cursor.close()
            conn.close()
            return "Этот пользователь уже существует"
        cursor.execute("INSERT INTO users(user_name, password) VALUES(%s, %s)",
                       (add_body.user_name, add_body.password))
        conn.commit()
        cursor.close()
        conn.close()
        return "Пользователь успешно добавлен"
    except Exception as error:
        raise error

def authoriz_user(user_body: User):
    try:
        conn = psycopg2.connect(dbname="API", user="postgres", password="1", host="localhost", port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_name = %s AND password = %s",
                       (user_body.user_name, user_body.password))
        result = cursor.fetchall()
        if result:
            cursor.close()
            conn.close()
            return "Вы успешно авторизовались"
        return "Неверный логин или пароль"
    except Exception as error:
        raise error

def delete_user(del_body: User):
    try:
        conn = psycopg2.connect(dbname="API", user="postgres", password="1", host="localhost", port="5432")
        cursor = conn.cursor()
        conn.autocommit = True
        cursor.execute("SELECT * FROM users WHERE user_name = %s  AND password = %s",
                       (del_body.user_name, del_body.password))
        result = cursor.fetchall()
        if not result:
            cursor.close()
            conn.close()
            return "Неверный логин или пароль"
        cursor.execute("DELETE FROM books WHERE user_name = %s", (del_body.user_name,))
        cursor.execute("DELETE FROM users WHERE user_name = %s", (del_body.user_name,))
        cursor.close()
        conn.close()
        return (f"Вы успешно удалили пользователя - {del_body.user_name},\n "
                f"Все книги пользователя {del_body.user_name} были удалены.")
    except Exception as error:
        raise error
