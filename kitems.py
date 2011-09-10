from pymongo import Connection

connection = Connection()
db = connection.kotodo

def get_items(username):
    uid = db.users.find_one({'user': username})[u'_id']
    return db.items.find({'owner': uid})

def add_item(text, owner):
    uid = db.users.find_one({'user': owner})[u'_id']
    newitemid = db.items.insert({'owner': uid, 'text': text})
    return db.items.find_one({'_id': newitemid})

def hms(seconds):
    hours = seconds / 3600
    seconds -= 3600*hours
    minutes = seconds / 60
    seconds -= 60*minutes
    return "%02dh %02dm %02ds" % (hours, minutes, seconds)
