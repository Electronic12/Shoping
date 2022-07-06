from flask import render_template, request, Blueprint
from main.models import Admin

users = Blueprint('users', __name__)

@users.route('/jora/')
def jora():
    return 'Jora'
