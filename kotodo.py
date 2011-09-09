import bottle
from bottle import redirect, request, response, template, view, route, get, post, error, Bottle
bottle.debug(True)

from ksecret import secret
from kauth import create_user, check_user

app = Bottle()

@app.route('/')
def index():
    username = request.get_cookie('U', secret=secret())
    password = request.get_cookie('P', secret=secret())
    if check_user(username, password):
        return template('todo')
    else:
        return template('login', error=None)

@app.post('/login')
def postlogin():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_user(username, password):
        response.set_cookie('U', username, secret=secret())
        response.set_cookie('P', password, secret=secret())
        redirect('/')
    else:
        return template('login', error='Wrong username or password. Please try again.')

@app.error(404)
def notfound(error):
    return "Error 404!!1: %s" % error

@app.get('/register')
def getregister():
    return template('reg')

@app.post('/register')
def postregister():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if create_user(username, password):
        response.set_cookie("U", username, secret=secret())
        response.set_cookie("P", password, secret=secret())
        redirect('/')

def ret_kotoapp():
    return app
