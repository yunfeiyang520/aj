
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask import session as user_session, jsonify, redirect

from utils import status_code

import functools

db = SQLAlchemy()
session = Session()


def init_ext(app):

    db.init_app(app=app)
    session.init_app(app=app)


def get_db_uri(DATABASE):

    user = DATABASE.get('USER')
    passoword = DATABASE.get('PASSWORD')
    host = DATABASE.get('HOST')
    port = DATABASE.get('PORT')
    name = DATABASE.get('NAME')
    db = DATABASE.get('DB')
    driver = DATABASE.get('DRIVER')


    return '{}+{}://{}:{}@{}:{}/{}'.format(db, driver,
                                           user, passoword,
                                           host, port, name)

'''
验证用户是否登录状态
'''
def is_login(view_fun):
    @functools.wraps(view_fun)
    def decorator():
        try:
            if 'user_id' in user_session:
                return view_fun()
            else:
                return redirect('/user/login/')
        except Exception as e:
            return redirect('/user/login/')
    return decorator
