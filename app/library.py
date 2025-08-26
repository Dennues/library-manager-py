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
    

    # Ändern von Bucheigenschaften anhand der ID (z.B. pyton main.py update 1 --author "der Erste" --year 1002)

    def update_book(self, book_id: int, title: str | None = None, author: str | None = None, year: int | None = None) -> bool:
        with get_connection() as conn:
            # Nur Felder updaten, die übergeben wurden
            updates, values = [], []
            if title:
                updates.append("title = ?")
                values.append(title)
            if author:
                updates.append("author = ?")
                values.append(author)
            if year is not None:
                updates.append("year = ?")
                values.append(year)

            if not updates:
                return False  # nichts zu ändern

            values.append(book_id)
            sql = f"UPDATE books SET {', '.join(updates)} WHERE id = ?"
            cursor = conn.execute(sql, values)
            return cursor.rowcount > 0

    # Buch anhand der ID löschen

    def delete_book(self, book_id: int) -> bool:
        with get_connection() as conn:
            cursor = conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
            return cursor.rowcount > 0
            
