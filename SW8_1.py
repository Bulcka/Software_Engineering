class Book:
    def __init__(self, title, author):
        self.title = title 
        self.author = author 


my_book = Book("1984", "George Orwell")


print(f"Book title: {my_book.title}")
print(f"Author: {my_book.author}")
