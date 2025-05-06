class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

book1 = Book()
book1.increment_book_count()

book2 = Book()
book2.increment_book_count()

print("Total books:", Book.total_books)
