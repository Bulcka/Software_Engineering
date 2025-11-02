class Publication:
    def info(self):
        pass 

class Book(Publication):
    def info(self):
        print("This is a printed book.")

class Magazine(Publication):
    def info(self):
        print("This is a monthly magazine.")

class Newspaper(Publication):
    def info(self):
        print("This is a daily newspaper.")


publications = [Book(), Magazine(), Newspaper()]
for p in publications:
    p.info()
