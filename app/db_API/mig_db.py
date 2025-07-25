import psycopg2

def create_db():
    print("Создание базы данных")
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1", host="localhost", port="5432")
    conn.autocommit = True
    cursor = conn.cursor()
    try:
        cursor.execute('CREATE DATABASE "API"')
        print("База данных создана")
    except psycopg2.errors.DuplicateDatabase:
        print("База данных 'API' уже существует.")
    finally:
        cursor.close()
        conn.close()

def delete_table():
    conn = psycopg2.connect(dbname="API", user="postgres", password="1", host="localhost", port="5432")
    conn.autocommit = True
    cursor = conn.cursor()
    delete_books_table = '''DROP TABLE IF EXISTS books'''
    delete_books_info_table = '''DROP TABLE IF EXISTS books_text'''
    delete_users_table = '''DROP TABLE IF EXISTS users'''
    print("Начало удаления таблицы с книгами")
    cursor.execute(delete_books_table)
    print("Таблица с книгами успешно удалена")
    print("Начало удаления таблицы с текстом книг")
    cursor.execute(delete_books_info_table)
    print("Таблица с текстом книг успешно удалена")
    print("Начало удаления таблицы пользователей")
    cursor.execute(delete_users_table)
    print("Таблица пользователей успешно удалена")
    cursor.close()
    conn.close()

def create_table():
    conn = psycopg2.connect(dbname="API", user="postgres", password="1", host="localhost", port="5432")
    conn.autocommit = True
    cursor = conn.cursor()
    create_books_table = '''
        CREATE TABLE IF NOT EXISTS books(
            id BIGINT GENERATED ALWAYS AS IDENTITY,
            user_name VARCHAR(50) NOT NULL,
            book_name VARCHAR(50) NOT NULL,
            category VARCHAR(50),
            book_year BIGINT DEFAULT 0,
            author VARCHAR(50) NOT NULL)'''
    create_books_text_table = '''
        CREATE TABLE IF NOT EXISTS books_text(
            book_name VARCHAR(50) NOT NULL,
            user_name VARCHAR(50) NOT NULL,
            book_text TEXT NOT NULL)'''
    create_users_table = '''
        CREATE TABLE IF NOT EXISTS users(
        user_name VARCHAR(50) PRIMARY KEY,
        password VARCHAR(50) NOT NULL)'''
    print("Создание таблицы книг")
    cursor.execute(create_books_table)
    print("Таблица книг создана")
    print("Создание таблицы с текстом книг")
    cursor.execute(create_books_text_table)
    print("Таблица с текстом книг создана")
    print("Создание таблица пользователей")
    cursor.execute(create_users_table)
    print("Таблица пользователей создана")
    cursor.close()
    conn.close()

create_db()
delete_table()
create_table()