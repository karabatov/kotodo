from pymongo import Connection
from bson import ObjectId
from datetime import datetime

connection = Connection()
db = connection.kotodo

def get_items(username):
    uid = db.users.find_one({'user': username})[u'_id']
    return db.items.find({'o': uid})

def add_item(text, owner):
    uid = db.users.find_one({'user': owner})[u'_id']
    newitemid = db.items.insert({'o': uid, 't': text, 'ts': 0, 'ss': []})
    return db.items.find_one({'_id': newitemid})

def remove_item(itemid):
    return db.items.remove({'_id': ObjectId(itemid)})

def timer_start(itemid):
    item = db.items.find_one({'_id': ObjectId(itemid)})
    item[u'cs'] = datetime.utcnow()
    item[u'tr'] = True
    db.items.save(item)
    return item.get('ts', 0)

def timer_stop(itemid):
    item = db.items.find_one({'_id': ObjectId(itemid)})
    delta = datetime.utcnow() - item.get('cs', datetime.utcnow())
    deltasec = delta.days * 86400 + delta.seconds
    item[u'ts'] += deltasec
    item[u'tr'] = False
    item[u'ss'].append({'s': item.get('cs', datetime.utcnow()), 'd': deltasec})
    db.items.save(item)
    return item.get('ts', 0)

def hms(seconds):
    hours = seconds / 3600
    seconds -= 3600*hours
    minutes = seconds / 60
    seconds -= 60*minutes
    return "%02dh %02dm %02ds" % (hours, minutes, seconds)

def dlt(before):
    delta = datetime.utcnow() - before
    return delta.days * 86400 + delta.seconds
