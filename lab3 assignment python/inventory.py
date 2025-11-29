# inventory.py
import json
from pathlib import Path
from book import Book
 
class LibraryInventory:
    def __init__(self, file_path="books.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load_books()
 
 
    def load_books(self):
        try:
            if self.file_path.exists():
                with open(self.file_path, "r") as f:
                    data = json.load(f)
                    for b in data:
                        self.books.append(Book(**b))
        except Exception:
            print("Error: Could not read JSON file.")
 
    def save_books(self):
        try:
            data = [b.to_dict() for b in self.books]
            with open(self.file_path, "w") as f:
                json.dump(data, f, indent=4)
        except Exception:
            print("Error: Could not save file.")
 
   
    def add_book(self, book):
        self.books.append(book)
        self.save_books()
 
    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]
 
    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None
 
    def display_all(self):
        for book in self.books:
            print(book)
 
 
