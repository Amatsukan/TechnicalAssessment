from sort_strategy import *

class SortingServiceException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class Book:
    def __init__(self, title, author, ed_year):
        self.title   = title
        self.author  = author
        self.ed_year = ed_year

    def __str__(self):
        string = "Title={}, Author={}, Year={}".format(self.title, self.author, self.ed_year)
        return string

class Bookshelf:
    def __init__(self):
        self.books = OrderedSet()

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.add(book)
        else:
            raise TypeError('Only books in bookshelf!')

    def sort(self, strategy = Tilte_sort(Author_sort())):
        try:
            if(self.books == None):
                raise SortingServiceException('The book set can\'t be null')
        except CompareWithNullException as e:
            self.books = strategy.sort(self.books)
        
    def clean(self):
        self.books.clear()

    def Null(self):
        self.books = None

    def antiNull(self):
        self.books = OrderedSet()

    def list(self):
        if(len(self.books) == 0):
            return "There is no books on shelf!!!"

        string = "Books on shelf:<br>"
        for book in self.books:
            string = string + str( book ) + "<br>"
        return string

    def __str__(self):
        return self.list()
