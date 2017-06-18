from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
from pyramid.response import Response

from book import *

bs = Bookshelf()

@view_config(route_name='sort')
def sort_books(request):
	try:
		bs.sort()
		return Response( str(bs) )
	except SortingServiceException as e:
		return Response( str(e) )

@view_config(route_name='clean')
def clean(request):
	bs.clean()
	return Response('The Bookshielf has been cleaned!')


@view_config(route_name='add')
def add_book(request):
	title = ('%(title)s' % request.matchdict)
	author = ('%(author)s' % request.matchdict)
	year = ('%(year)s' % request.matchdict)
	book = Book(title, author, year)
	bs.add_book(book)
	return Response( str(bs) )


if __name__ == '__main__':
	config = Configurator()
	config.add_route('sort', '/sort')
	config.add_route('clean', '/clean')
	config.add_route('add', '/add/{title}/{author}/{year}')
	config.scan()
	app = config.make_wsgi_app()
	server = make_server('0.0.0.0', 8080, app)
	server.serve_forever()