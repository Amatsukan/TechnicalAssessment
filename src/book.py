import json
from sort_strategy import *

class SortingServiceException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def create_book_by_dict(book_dict):
    title = ('%(title)s' % book_dict)
    author = ('%(author)s' % book_dict)
    year = ('%(ed_year)s' % book_dict)
    return Book(title, author, year)

class Book:
    def __init__(self, title, author, ed_year):
        self.title   = title
        self.author  = author
        self.ed_year = ed_year

    def __str__(self):
        string = "Title={}, Author={}, Year={}".format(self.title, self.author, self.ed_year)
        return string

def create_bookshelf_by_list(book_dict_list):
    bs = Bookshelf()
    for book_dict in book_dict_list:
        title = ('%(title)s' % book_dict)
        author = ('%(author)s' % book_dict)
        year = ('%(ed_year)s' % book_dict)
        bs.add_book(Book(title, author, year))
    return bs

class Bookshelf:
    def __init__(self):
        self.books = OrderedSet()
        self.strategy = Title_sort().setComposition(Author_sort())#default sort composition, title and author

    def set_order(self, order_str):
        if(order_str == "desc"):
            self.strategy.desc_order()
        else:
            self.strategy.asc_order()

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.add(book)
        else:
            raise TypeError('Only books in bookshelf!')

    def sort(self):
        try:
            if(self.books == None):
                raise SortingServiceException('The book set can\'t be null')
        except CompareWithNullException as e:
            self.books = self.strategy.sort(self.books)
        
    def clean(self):
        try:
            if self.books == None:
                self.books = OrderedSet()
        except CompareWithNullException as e:
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

    def __eq__(self, other):
        eq = len(self.books) == len(other.books)
        
        if eq:
            eq &= self.books.map == other.books.map

        return eq
