from flask import Flask, request, g
from config import BAseConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(BAseConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
