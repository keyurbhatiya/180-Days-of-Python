'''
2. Library Management System
Create a library management system with the following:

Classes & Attributes
Book


title

author

isbn (unique identifier)
is_available (default is True)

LibraryMember

name
member_id
borrowed_books (List of borrowed books)

Methods:

borrow_book(book, library) – Borrows a book if available
return_book(book, library) – Returns a borrowed book
Library

books (List of available books)
members (List of registered members)

Methods:

add_book(book) – Adds a book to the library
remove_book(book) – Removes a book from the library
register_member(member) – Registers a new member

'''


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book, library):
        if book in library.books and book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book, library):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow '{book.title}'")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed '{book.title}' from the library.")
        else:
            print("Book not found in the library.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Registered member: {member.name}")


# Example Usage
library = Library()

# Adding books
book1 = Book("Python Programming", "John Doe", "123456789")
book2 = Book("Data Science", "Jane Smith", "987654321")

library.add_book(book1)
library.add_book(book2)

# Registering members
member1 = LibraryMember("Alice", "M001")
library.register_member(member1)

# Borrowing and returning books
member1.borrow_book(book1, library)
member1.return_book(book1, library)
