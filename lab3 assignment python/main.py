# main.py
from inventory import LibraryInventory
from book import Book
 
def menu():
    print("\n--- Library Inventory Manager ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")
 
def main():
    inventory = LibraryInventory()
 
    while True:
        menu()
        choice = input("Enter choice: ")
 
        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            inventory.add_book(Book(title, author, isbn))
            print("Book added.")
 
        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.issue():
                inventory.save_books()
                print("Book issued.")
            else:
                print("Cannot issue.")
 
        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.return_book():
                inventory.save_books()
                print("Book returned.")
            else:
                print("Cannot return.")
 
        elif choice == "4":
            inventory.display_all()
 
        elif choice == "5":
            title = input("Enter title to search: ")
            results = inventory.search_by_title(title)
            for b in results:
                print(b)
            if not results:
                print("No books found.")
 
        elif choice == "6":
            print("Goodbye!")
        
            break
        
        else:
            print("Invalid choice")


if __name__ == "__main__":
 main()