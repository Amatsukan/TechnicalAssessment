#!/usr/bin/python
from pyramid_server import *
import os
import sys

argc = len(sys.argv)

if argc == 2:
    port = sys.argv[1]
else:
	port=3000

    
if __name__ == '__main__':
	print("running in localhost:{}".format(port))
	run('0.0.0.0', port)