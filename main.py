import argparse
from app.db import init_db
from app.library import Library

def main():
    parser = argparse.ArgumentParser(description="Library Manager CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # init-db
    sub.add_parser("init-db", help="Initialisiert die SQLite-Datenbank")

    # add
    add_parser = sub.add_parser("add", help="Fügt ein neues Buch hinzu")
    add_parser.add_argument("--title", required=True)
    add_parser.add_argument("--author", required=True)
    add_parser.add_argument("--year", type=int)

    # list
    sub.add_parser("list", help="Zeigt alle Bücher an")

    args = parser.parse_args()
    lib = Library()

    if args.cmd == "init-db":
        init_db()

    elif args.cmd == "add":
        book_id = lib.add_book(args.title, args.author, args.year)
        print(f"Buch hinzugefügt mit ID {book_id}")

    elif args.cmd == "list":
        books = lib.list_books()
        if not books:
            print("Keine Bücher in der Bibliothek.")
        for book in books:
            print(f"[{book.id}] {book.title} von {book.author} ({book.year})")

if __name__ == "__main__":
    main()
