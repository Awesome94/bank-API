from flask import Flask, request, g
from config import BaseConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv, find_dotenv

# create APP
app = Flask(__name__)
load_dotenv(find_dotenv())

app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
ma = Marshmallow(app)

migrate = Migrate(app, db)

from app import routes, models
