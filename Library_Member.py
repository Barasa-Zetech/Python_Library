## Python inheritance program of class named "LibraryMember" with the following attributes and methods:


class LibraryItem:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
class Book(LibraryItem):
    def __init__(self, title, author, publication_year):
        super().__init__(title, author, publication_year)
        self.borrowed = False
    def borrow_book(self):
        self.borrowed = True
    def return_book(self):
        self.borrowed = False
    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publication Year:", self.publication_year)
        print("Borrowed:", "Yes" if self.borrowed else "No")
class LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
    def borrow_book(self, book):
        self.borrowed_books.append(book)
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
    def display_info(self):
        print("Member ID:", self.member_id)
        print("Name:", self.name)
        print("Borrowed Books:")
        if self.borrowed_books:
            for book in self.borrowed_books:
                print("- Title:", book.title)
        else:
            print("- None")

# Create a Book instance
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
# Create a LibraryMember instance
member1 = LibraryMember(1, "John Doe")
# Borrow the book
member1.borrow_book(book1)
member1.display_info()
# Return the book
member1.return_book(book1)
member1.display_info()


