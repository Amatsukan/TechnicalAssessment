import sys
import os
import unittest

sys.path.insert(0, os.path.realpath('./') + '/..')

from pyramid import testing
from data_for_tests import *
from pyramid_server import *
from config import *

class APITest(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def testAddBook(self):
        n_of_books = len(bs.books)
        request = testing.DummyRequest()
        request.matchdict = book1
        response = add_book(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(bs.books), n_of_books+1)

    def testCleanBooks(self):
        request = testing.DummyRequest()
        response = clean(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(bs.books), 0)

    def testChangeOrderAscending(self):
        request = testing.DummyRequest()
        request.matchdict = {'ord':'asc'}
        response = chan_ord(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bs.strategy.reverse, False)

    def testChangeOrderDescending(self):
        request = testing.DummyRequest()
        request.matchdict = {'ord':'desc'}
        response = chan_ord(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bs.strategy.reverse, True)

    def testConfigsWithoutComposition(self):
        request = testing.DummyRequest()
        request.matchdict = {'first_strategy':'title'}
        response = sort_config_1(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bs.strategy.__class__.__name__, Title_sort().__class__.__name__)

        request.matchdict = {'first_strategy':'author'}
        response = sort_config_1(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bs.strategy.__class__.__name__, Author_sort().__class__.__name__)

        request.matchdict = {'first_strategy':'year'}
        response = sort_config_1(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bs.strategy.__class__.__name__, Year_sort().__class__.__name__)

    def testConfigsYearComposition(self):
        request = testing.DummyRequest()
        request.matchdict = {'first_strategy':'year', 'second_strategy':'title'}
        response = sort_config_2(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bs.strategy.__class__.__name__, Year_sort().__class__.__name__)
        self.assertEqual(bs.strategy.composition.__class__.__name__, Title_sort().__class__.__name__)
        
        request = testing.DummyRequest()
        request.matchdict = {'first_strategy':'year', 'second_strategy':'author'}
        response = sort_config_2(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bs.strategy.__class__.__name__, Year_sort().__class__.__name__)
        self.assertEqual(bs.strategy.composition.__class__.__name__, Author_sort().__class__.__name__)

    def testConfigsAuthorComposition(self):
        request = testing.DummyRequest()
        request.matchdict = {'first_strategy':'author', 'second_strategy':'title'}
        response = sort_config_2(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bs.strategy.__class__.__name__, Author_sort().__class__.__name__)
        self.assertEqual(bs.strategy.composition.__class__.__name__, Title_sort().__class__.__name__)
        
        request = testing.DummyRequest()
        request.matchdict = {'first_strategy':'author', 'second_strategy':'year'}
        response = sort_config_2(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bs.strategy.__class__.__name__, Author_sort().__class__.__name__)
        self.assertEqual(bs.strategy.composition.__class__.__name__, Year_sort().__class__.__name__)

    def testConfigsTitleComposition(self):
        request = testing.DummyRequest()
        request.matchdict = {'first_strategy':'title', 'second_strategy':'year'}
        response = sort_config_2(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bs.strategy.__class__.__name__, Title_sort().__class__.__name__)
        self.assertEqual(bs.strategy.composition.__class__.__name__, Year_sort().__class__.__name__)
        
        request = testing.DummyRequest()
        request.matchdict = {'first_strategy':'title', 'second_strategy':'author'}
        response = sort_config_2(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(bs.strategy.__class__.__name__, Title_sort().__class__.__name__)
        self.assertEqual(bs.strategy.composition.__class__.__name__, Author_sort().__class__.__name__)

    def testAddAllBooks(self):
        n_of_books = len(bs.books)
        for book in books:
            request = testing.DummyRequest()
            request.matchdict = book
            response = add_book(request)
            self.assertEqual(response.status_code, 200)
        self.assertEqual(len(bs.books), n_of_books+len(books))

    def testSortTitleAscending(self):
        bs.clean()

        for book in books:
            request = testing.DummyRequest()
            request.matchdict = book
            response = add_book(request)

        request = testing.DummyRequest()
        request.matchdict = {'first_strategy':'title'}
        response = sort_config_1(request)

        request.matchdict = {'ord':'ascendent'}
        response = chan_ord(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(bs.strategy.__class__.__name__, Title_sort().__class__.__name__)

        response = sort_books(request)

        sortedOk = create_bookshelf_by_list(TitleAsc)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(bs), str(sortedOk))

    def testSortAuthorAscendingTitleDescending(self):
        bs.clean()

        for book in books:
            request = testing.DummyRequest()
            request.matchdict = book
            response = add_book(request)

        request = testing.DummyRequest()

        request.matchdict = {'first_strategy':'author', 'second_strategy' : 'title'}
        sort_config_2(request)

        bs.strategy.asc_order(False)
        bs.strategy.composition.desc_order(False)

        self.assertEqual(bs.strategy.reverse, False)

        self.assertEqual(bs.strategy.composition.reverse, True)

        response = sort_books(request)

        sortedOk = create_bookshelf_by_list(AuthorAscTitleDesc)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(bs), str(sortedOk))

    def testSortEditionDescAuthorDescTitleAsc(self):
        bs.clean()

        for book in books:
            request = testing.DummyRequest()
            request.matchdict = book
            response = add_book(request)

        request = testing.DummyRequest()

        request.matchdict = {'first_strategy':'ed_year', 'second_strategy' : 'author', 'third_strategy' : 'title'}
        sort_config_3(request)

        bs.strategy.desc_order(True)
        bs.strategy.composition.composition.asc_order(False)

        self.assertEqual(bs.strategy.reverse, True)
        self.assertEqual(bs.strategy.composition.reverse, True)
        self.assertEqual(bs.strategy.composition.composition.reverse, False)

        response = sort_books(request)

        sortedOk = create_bookshelf_by_list(EditionDescAuthorDescTitleAsc)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(bs), str(sortedOk))

    def testSortEmptySet(self):
        bs.clean()

        request = testing.DummyRequest()
        response = sort_books(request)

        sortedOk = create_bookshelf_by_list(empty)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(bs), str(sortedOk))

    def testSortNullSet(self):
        request = testing.DummyRequest()
        bs.Null();
        self.assertEqual(bs.books, None)
        
        self.assertRaises(SortingServiceException, sort_books, request, True)#test exception
        
        response = sort_books(request)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()