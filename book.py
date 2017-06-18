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
		self.books = set()
		self.rules = {}

	def add_book(self, book):
		if isinstance(book, Book):
			self.books.add(book)
		else:
			raise TypeError('Only books in bookshelf!')

	def sort(self):
		if(self.books == None):
			raise SortingServiceException('The book set can\'t be null')
		self.books = set(sorted(self.books, key=lambda x: x.title, reverse=True))

	def clean(self):
		self.books.clear()

	def __str__(self):
		string = "Books on shielf:    "
		for book in self.books:
			string = string + str( book ) + "    "
		return string
