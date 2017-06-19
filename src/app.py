from pyramid_server import *
import os

port = 80
if 'PORT' in os.environ
	port = os.environ['PORT']

if __name__ == '__main__':
	run('0.0.0.0', port)