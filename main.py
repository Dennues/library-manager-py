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

    # update
    update_parser = sub.add_parser("update", help="Aktualisiert ein Buch")
    update_parser.add_argument("id", type=int, help="ID des Buches")
    update_parser.add_argument("--title")
    update_parser.add_argument("--author")
    update_parser.add_argument("--year", type=int)

    # delete
    delete_parser = sub.add_parser("delete", help="Löscht ein Buch")
    delete_parser.add_argument("id", type=int, help="ID des Buches")

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

    elif args.cmd == "update":
        success = lib.update_book(args.id, args.title, args.author, args.year)
        if success:
            print(f"Buch {args.id} wurde aktualisiert.")
        else:
            print(f"Buch {args.id} konnte nicht aktualisiert werden.")

    elif args.cmd == "delete":
        success = lib.delete_book(args.id)
        if success:
            print(f"Buch {args.id} wurde gelöscht.")
        else:
            print(f"Buch {args.id} konnte nicht gefunden werden.")
    
if __name__ == "__main__":
    main()
