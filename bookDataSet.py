from dataclasses import dataclass
# Create a Library that can store books.
# These books can be borrowed returned and declared missing

# Tackle the first problem
from datetime import datetime, timedelta


@dataclass
class Book:
    """
    Book class
    """
    BORROW_TIME = 21
    returned_date = None

    title: str
    author: str
    rec_num: int
    loaned: bool = False
    missing: bool = False

    def borrowed(self):
        if self.loaned:
            print(f"You cannot borrow this book.\nIt will be available at {self.returned_date}")
            return None
        self.loaned = True
        self.returned_date = datetime.now() + timedelta(days=self.BORROW_TIME)
        return self.returned_date

    def returned(self):
        self.loaned = False
        self.returned_date = None
        return self.returned_date

    def is_missing(self):
        if self.borrowed() < datetime.now() and self.loaned:
            self.missing = True
        else:
            self.missing = False

    # def __repr__(self):
    #     return 'Title: {}, Author: {}'.format(self.title, self.author)


class Library:
    books = []

    def __init__(self, name: str):
        self.name = name

    def add_book(self, book: Book):
        book.rec_num = len(self.books)
        self.books.append(book)

    def get_book(self, book_id):
        return self.books[book_id]


# book1 = Book("Hunger Games", "some woman", 0)
# book1.borrowed()
# print(f"This book is {book1.loaned} the Library")
# print(f"This book can be borrowed for {Book.borrow_time} days")
# print(book1.borrowed())

if __name__ == "__main__":
    library = Library("Wolverton Library")
    # library.add_book(book1)

    for i in range(50):
        book = Book("Hunger Games", "some woman", i)
        library.add_book(book)

    book_got = library.get_book(24)
    print(book_got)
    print(f"Hi Dan, you have now borrowed ths book, you need to return it by {book_got.borrowed()}")
    print(f"Has this book been loaned? {book_got.loaned}")

    book_got.borrowed()
