class Book:
    total_books = 0

    @classmethod
    def get_total_books(cls):
        """Returns the total number of books."""
        cls.total_books += 1

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.get_total_books()

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

print(f"Total books: {Book.total_books}")  # Output: Total books: 2
        