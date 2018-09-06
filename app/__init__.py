from flask import Flask, request, g
from config import BaseConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv, find_dotenv

# create APP
app = Flask(__name__)
load_dotenv(find_dotenv())

@app.route('/v1')
def index():
    return request.base_url

app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import routes, models
