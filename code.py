# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TthVqg8plY1n0nVepGPGFpFmbdv_R_P9
"""

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.issued = False
        self.borrower = None

    def issue_book(self, borrower):
        if not self.issued:
            self.issued = True
            self.borrower = borrower
            print(f"Book '{self.title}' issued to {borrower}.")
        else:
            print(f"Book '{self.title}' is already issued to {self.borrower}.")

    def return_book(self):
        if self.issued:
            print(f"Book '{self.title}' returned by {self.borrower}.")
            self.issued = False
            self.borrower = None
        else:
            print(f"Book '{self.title}' was not issued.")

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Issued: {self.issued}, Borrower: {self.borrower if self.borrower else 'None'}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def issue_book(self, isbn, borrower):
        for book in self.books:
            if book.isbn == isbn:
                book.issue_book(borrower)
                return
        print(f"Book with ISBN {isbn} not found in the library.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.return_book()
                return
        print(f"Book with ISBN {isbn} not found in the library.")

    def display_available_books(self):
        available_books = [book for book in self.books if not book.issued]
        if available_books:
            print("Available books in the library:")
            for book in available_books:
                print(book)
        else:
            print("No books available in the library.")

    def display_issued_books(self):
        issued_books = [book for book in self.books if book.issued]
        if issued_books:
            print("Issued books and their borrowers:")
            for book in issued_books:
                print(book)
        else:
            print("No books are currently issued.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Display Available Books")
        print("5. Display Issued Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)

        elif choice == '2':
            isbn = input("Enter ISBN of the book to issue: ")
            borrower = input("Enter borrower's name: ")
            library.issue_book(isbn, borrower)

        elif choice == '3':
            isbn = input("Enter ISBN of the book to return: ")
            library.return_book(isbn)

        elif choice == '4':
            library.display_available_books()

        elif choice == '5':
            library.display_issued_books()

        elif choice == '6':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

