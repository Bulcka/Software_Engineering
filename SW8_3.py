from SW8_2 import Book

class EBook(Book):
    def __init__(self, title, author, year, pages, file_size):
        super().__init__(title, author, year, pages) 
        self.file_size = file_size  

    def download(self):
        print(f"Downloading '{self.title}' ({self.file_size} MB)...")


ebook = EBook("Digital Fortress", "Dan Brown", 1998, 356, 5)
ebook.description()
ebook.download()
