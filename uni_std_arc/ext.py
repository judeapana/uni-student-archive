from flask_rq2 import RQ
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_maintenance import Maintenance

_maintenance = Maintenance()
_login = LoginManager()
_migrate = Migrate()
_ma = Marshmallow()
_db = SQLAlchemy()
_rq = RQ()
_bcrypt = Bcrypt()
_mail = Mail()
