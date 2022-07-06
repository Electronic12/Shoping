from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from main.config import Config
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import models

from main.user.routes import users
from main.admin.routes import admins
from main.products.routes import products
from main.main_ui.routes import main_ui

app.register_blueprint(products)
app.register_blueprint(admins)
app.register_blueprint(users)
app.register_blueprint(main_ui)
