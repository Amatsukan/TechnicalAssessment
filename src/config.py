from book import *
from sort_strategy import *

bs = Bookshelf()

def getStrategy(strategy_str):
    if(strategy_str == "author"):
        return Author_sort()#sort by author
    if(strategy_str == "title"):
        return Title_sort() #sort by title
    else:
        return Year_sort()  #sort by edition year

def any_of(segment_name, *allowed):
    def predicate(info, request):
        if info['match'][segment_name] in allowed:
            return True
    return predicate

f_strategy = any_of('first_strategy','author', 'title', 'ed_year')
s_strategy = any_of('second_strategy','author', 'title', 'ed_year')
t_strategy = any_of('third_strategy','author', 'title', 'ed_year')
orders = any_of('ord','desc', 'asc')
