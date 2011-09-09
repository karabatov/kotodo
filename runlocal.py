import bottle
from kotodo import ret_kotoapp

application = ret_kotoapp()

bottle.run(app=application, host='localhost', port=5000, reloader=True)
