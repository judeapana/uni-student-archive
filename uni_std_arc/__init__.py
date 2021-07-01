from flask import Flask
from uni_std_arc.ext import _maintenance, _login, _migrate, _ma, _db, _rq, _bcrypt, _mail


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    _db.init_app(app)
    _maintenance.init_app(app)
    _login.init_app(app)
    _migrate.init_app(app, _db)
    _ma.init_app(app)
    _rq.init_app(app)
    _bcrypt.init_app(app)
    _mail.init_app(app)
    return app
