## Book organizator

class Book:
    def __init__(self, title, authors, rating, read):
        self.title = title
        self.authors = authors
        self.set_rating(rating)
        self.read = read
    
    def set_rating(self, value):
        if value >= 1.0 and value <= 10.0:
            self.rating = value
        
    def set_read(self, value):
        if value == "tak":
            self.read = True
        else:
            self.read = False

class BookBot:
    def __init__(self):
        self.shelve = []

##------------------ADD---------------------------------     
    def add_book(self, title, authors, rating, read):
        b = Book(title, authors, rating, read)
        self.shelve.append(b)
    
    def add_boo_from_input(self):
        title = input("Tytuł :")
        authors = input("Autorzy :")
        rating = float(input("Ocena :"))
        read = input("Przeczytana? :")
        
        if read == "tak":
            read = True
        else:
            read = False
            
        self.add_book(title, authors, rating, read)
        
##------------------SET---------------------------------        
    def set_book_rating(self, book_index, rating):
        book = self.shelve[book_index]
        book.set_rating(rating)
    
    def set_book_read(self, book_index, read):
        book = self.shelve[book_index]
        book.set_read(read)        

##------------------PRINT--------------------------------     
    def print_book(self, indeks):
        book = self.shelve[indeks]
        print("{:4} | {:70} | {:30} | {:4} | {:5}".format(indeks, book.title, book.authors, book.rating, book.read))

    def print_all_books(self):
        for index in range(len(self.shelve)):
            self.print_book(index)
    

        
bot = BookBot()

bot.add_book("Bitcoin dla zaawansowanych", "Antonopoulos Andreas M.", 9.0, False)
bot.add_book("Giełda podstawy inwestowania", "Adam Zaręba", 7.5, False)
bot.add_book("Analiza fundamentalna.Standing finansowy i wycena przedsiębiorstwa", "Artur Sajnóg", 6.0, True)
bot.add_book("Tales od Mystery and Imagination", "Edgar Allan Poe", 9.5, True)

bot.print_all_books()
