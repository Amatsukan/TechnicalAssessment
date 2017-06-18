from ordered_set import *

class Sort_strategy:
    def sort(self, books):
        pass

class Tilte_sort(Sort_strategy):
    def __init__(self, composition = None, reverse = False):
        self.composition = composition
        self.reverse = reverse

    def sort(self, books):
        if(self.composition == None):
            return OrderedSet(sorted(books, key = lambda x: x.title, reverse = self.reverse))
        else:
            return OrderedSet(sorted(self.composition.sort(books), key = lambda x: x.title, reverse = self.reverse)) 

class Author_sort(Sort_strategy):
    def __init__(self, composition = None, reverse = False):
        self.composition = composition
        self.reverse = reverse

    def sort(self, books):
        if(self.composition == None):
            return OrderedSet(sorted(books, key = lambda x: x.author, reverse = self.reverse))
        else:
            return OrderedSet(sorted(self.composition.sort(books), key = lambda x: x.author, reverse = self.reverse)) 

class Year_sort(Sort_strategy):
    def __init__(self, composition = None, reverse = False):
        self.composition = composition
        self.reverse = reverse

    def sort(self, books):
        if(self.composition == None):
            return OrderedSet(sorted(books, key = lambda x: x.year, reverse = self.reverse))
        else:
            return OrderedSet(sorted(self.composition.sort(books), key = lambda x: x.year, reverse = self.reverse)) 