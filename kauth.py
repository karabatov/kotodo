from mongauth import Mongauth
from pymongo import Connection

collection = Connection().kotodo.kauth
auth = Mongauth(collection)

def create_user(username, password):
    return auth.new(username, password)

def check_user(username, password):
    return auth.auth(username, password)
