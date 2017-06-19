from ordered_set import *

class Sort_strategy:

    def sort(self, books):
        pass

    def setComposition(self,composition):
        self.composition = composition
        return self

    def cleanComposition(self,composition):
        self.composition = None
        return self

    def desc_order(self, recursive = True):
        self.reverse = True; 
        if(self.composition != None and recursive):
            self.composition.desc_order(recursive)

    def asc_order(self, recursive = True):
        self.reverse = False;
        if(self.composition != None and recursive):
            self.composition.asc_order(recursive)

class Title_sort(Sort_strategy):
    def __init__(self, composition = None, reverse = False):
        self.composition = composition
        self.reverse = reverse
        self.id = "TITLE SORT"

    def sort(self, books):
        if(self.composition == None):
            return OrderedSet(sorted(books, key = lambda x: x.title, reverse = self.reverse))
        else:
            return OrderedSet(sorted(self.composition.sort(books), key = lambda x: x.title, reverse = self.reverse)) 

class Author_sort(Sort_strategy):
    def __init__(self, composition = None, reverse = False):
        self.composition = composition
        self.reverse = reverse
        self.id = "AUTHOR SORT"

    def sort(self, books):
        if(self.composition == None):
            return OrderedSet(sorted(books, key = lambda x: x.author, reverse = self.reverse))
        else:
            return OrderedSet(sorted(self.composition.sort(books), key = lambda x: x.author, reverse = self.reverse)) 

class Year_sort(Sort_strategy):
    def __init__(self, composition = None, reverse = False):
        self.composition = composition
        self.reverse = reverse
        self.id = "YEAR SORT"

    def sort(self, books):
        if(self.composition == None):
            return OrderedSet(sorted(books, key = lambda x: x.ed_year, reverse = self.reverse))
        else:
            return OrderedSet(sorted(self.composition.sort(books), key = lambda x: x.ed_year, reverse = self.reverse)) 