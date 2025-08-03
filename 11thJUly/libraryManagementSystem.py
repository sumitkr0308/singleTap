class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued_to = None  # None means the book is available

    def is_available(self):
        return self.issued_to is None

    def display(self):
        status = "Available" if self.is_available() else f"Issued to {self.issued_to}"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print("Book added successfully!")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                book.display()

    def lend_book(self, title, borrower):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available():
                    book.issued_to = borrower
                    print(f"Book '{title}' has been issued to {borrower}.")
                    return
                else:
                    print(f"Book '{title}' is already issued to {book.issued_to}.")
                    return
        print(f"Book '{title}' not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_available():
                    print(f"Book '{title}' returned by {book.issued_to}.")
                    book.issued_to = None
                    return
                else:
                    print(f"Book '{title}' was not issued.")
                    return
        print(f"Book '{title}' not found.")


# Main menu
library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(title, author)
    elif choice == '2':
        library.display_books()
    elif choice == '3':
        title = input("Enter book title to lend: ")
        borrower = input("Enter borrower name: ")
        library.lend_book(title, borrower)
    elif choice == '4':
        title = input("Enter book title to return: ")
        library.return_book(title)
    elif choice == '5':
        print("Exiting Library System.")
        break
    else:
        print("Invalid choice. Try again.")
