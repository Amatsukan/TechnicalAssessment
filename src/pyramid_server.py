#!/usr/bin/python3
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config
from pyramid.response import Response
from config import *


@view_config(route_name='sort')
def sort_books(request, test_without_try_except = False):
    if test_without_try_except:
        bs.sort()
        return Response( str(bs) )
    else:
        try:
            bs.sort()
            return Response( str(bs) )
        except SortingServiceException as e:
            return Response( str(e) )

@view_config(route_name='sort_config1')
def sort_config_1(request):

    first_strategy = ('%(first_strategy)s' % request.matchdict)
    bs.strategy = getStrategy(first_strategy)

    return Response( "New config, strategy = {}!!!".format(bs.strategy.__class__.__name__))

@view_config(route_name='sort_config2')
def sort_config_2(request):

    first_strategy = ('%(first_strategy)s' % request.matchdict)
    second_strategy = ('%(second_strategy)s' % request.matchdict)

    bs.strategy = getStrategy(first_strategy)
    bs.strategy.setComposition( getStrategy(second_strategy) )

    return Response( "New config, strategy = {} composed with {}!!!".format(
        bs.strategy.__class__.__name__,
        bs.strategy.composition.__class__.__name__
        ))

@view_config(route_name='sort_config3')
def sort_config_3(request):
    first_strategy = ('%(first_strategy)s' % request.matchdict)
    second_strategy = ('%(second_strategy)s' % request.matchdict)
    third_strategy = ('%(third_strategy)s' % request.matchdict)

    bs.strategy = getStrategy(first_strategy)
    bs.strategy.setComposition( getStrategy(second_strategy) )
    bs.strategy.composition.setComposition( getStrategy(third_strategy) )

    return Response( "New config!!!")

@view_config(route_name='clean')
def clean(request):
    bs.clean()
    return Response('The Bookshielf has been cleaned!')

@view_config(route_name='list')
def list(request):
    return Response(bs.list())

@view_config(route_name='add')
def add_book(request):
    book = create_book_by_dict(request.matchdict)
    bs.add_book(book)
    return Response( "New book has been added on shelf: {}".format(str(book)) )

@view_config(route_name='change_order')
def chan_ord(request):
    order = ('%(ord)s' % request.matchdict)
    bs.set_order(order)
    return Response( "The new sorting order is: {}".format(order) )

def setup():
    config = Configurator()
    config.add_route('sort', '/sort')
    config.add_route('sort_config3', '/sort_config/{first_strategy}/{second_strategy}/{third_strategy}', custom_predicates=(f_strategy,s_strategy,t_strategy,) )
    config.add_route('sort_config2', '/sort_config/{first_strategy}/{second_strategy}', custom_predicates=(f_strategy,s_strategy,) )
    config.add_route('sort_config1', '/sort_config/{first_strategy}', custom_predicates=(f_strategy,) )
    config.add_route('change_order', '/order/{ord}', custom_predicates=(orders,) )
    config.add_route('clean', '/clean')
    config.add_route('list', '/list')
    config.add_route('add', '/add/{title}/{author}/{ed_year}')
    config.scan()
    return config

def run(ip, port):
    app = setup().make_wsgi_app()
    server = make_server(ip, port, app)
    server.serve_forever()
