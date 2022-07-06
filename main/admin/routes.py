from flask import Blueprint

admins = Blueprint('admins', __name__)

@admins.route('/home/')
def home():
    return '///////////////////////////////'

