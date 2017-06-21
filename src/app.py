#!/usr/bin/python
from pyramid_server import *
import os
import sys

argc = len(sys.argv)

if argc == 2:
    port = sys.argv[1]
else:
    port=3000


    """Book Sorter api
        ./app.py $PORT
    Args:
        Specific port
    """

    
if __name__ == '__main__':
    print("running in http://localhost:{}".format(port))
    run('0.0.0.0', int(port))