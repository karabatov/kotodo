import bottle
from bottle import route, error, Bottle
#debug(True)

app = Bottle()

@app.route('/')
def index():
    return "Hello World!"

@app.route('/hello/:name')
def hello(name):
    return "Hello, %s" % name

@app.error(404)
def notfound(error):
    return "Error 404!!1: %s" % error

def ret_kotoapp():
    return app