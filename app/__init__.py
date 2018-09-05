from flask import Flask, request, g
from config import BaseConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# create APP
app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import routes, models
