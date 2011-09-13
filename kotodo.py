import bottle
from bottle import redirect, request, response, template, view, route, get, post, error, Bottle, static_file
bottle.debug(True)

from ksecret import secret
from kauth import create_user, check_user
from kitems import get_items, add_item, remove_item, timer_start, timer_stop

app = Bottle()

@app.route('/static/:filename')
def server_static(filename):
    return static_file(filename, root='./static')

@app.get('/')
def index():
    username = request.get_cookie('U', secret=secret())
    password = request.get_cookie('P', secret=secret())
    if check_user(username, password):
        items = get_items(username)
        return template('todo', username=username, items=items)
    else:
        return template('login', error=None)

@app.post('/')
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

@app.post('/item/add')
def itemadd():
    text = request.forms.get('text')
    owner = request.forms.get('owner')
    newitem = add_item(text, owner)
    if newitem:
        return template('item', todo=newitem)

@app.post('/item/timer/start')
def timerstart():
    itemid = request.forms.get('itemid')
    if itemid:
        ts = timer_start(itemid)
        return str(int(ts))
    else:
        return '0'

@app.post('/item/timer/stop')
def timerstop():
    itemid = request.params.get('itemid', None)
    if itemid:
        ts = timer_stop(itemid)
        return str(int(ts))
    else:
        return 0
        
@app.post('/item/delete')
def itemdelete():
    itemid = request.params.get('itemid', None)
    if itemid:
        remove_item(itemid)
        return 'ok'
    else:
        return 'itemid not found'

def ret_kotoapp():
    return app
