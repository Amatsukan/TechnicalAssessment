from pyramid_server import *
import os

ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    port = int(os.environ.get('PORT', 17995))  #default is 17995
else:
    port = 3000

    
if __name__ == '__main__':
	print("running in localhost:{}".format(port))
	run('0.0.0.0', port)