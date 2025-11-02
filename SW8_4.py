class Book:
    def __init__(self, title, author, year):
        self.__title = title    
        self.__author = author  
        self.__year = year      

    def info(self):
       
        print(f"'{self.__title}' by {self.__author}, {self.__year}")

    def set_year(self, new_year):
        
        self.__year = new_year


book = Book("Fahrenheit 451", "Ray Bradbury", 1953)
book.info()
book.set_year(1967)
book.info()
