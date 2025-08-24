from app.db import get_connection
from app.models import Book

# Funktionen für die Bücher

class Library:
    def add_book(self, title: str, author: str, year: int | None = None) -> int:
        with get_connection() as conn:
            cursor = conn.execute(
                "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
                (title, author, year)
            )
            return cursor.lastrowid  # ID des neuen Buchs

    def list_books(self) -> list[Book]:
        with get_connection() as conn:
            rows = conn.execute("SELECT id, title, author, year FROM books").fetchall()
            return [Book(id=row[0], title=row[1], author=row[2], year=row[3]) for row in rows]
