class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year 
        self.pages = pages 

    def description(self):
        print(f"'{self.title}' by {self.author}, {self.year} ({self.pages} pages)")

my_book = Book("To Kill a Mockingbird", "Harper Lee", 1960, 281)
my_book.description()