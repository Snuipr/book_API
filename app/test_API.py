import pytest
import psycopg2
from httpx import ASGITransport, AsyncClient

from .main import app


def add_users():
    try:
        conn = psycopg2.connect(dbname="API", user="postgres", password="1", host="localhost", port="5432")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_name = %s", ("adm1",))
        result = cursor.fetchall()
        if result:
            cursor.close()
            conn.close()
            print("Этот пользователь уже существует")
        cursor.execute("INSERT INTO users(user_name, password) VALUES(%s, %s)",
                       ("adm1", "adm2"))
        conn.commit()
        cursor.close()
        conn.close()
        print("Пользователь успешно добавлен")
    except Exception as error:
        raise error


@pytest.mark.anyio
async def test_user():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/b")
