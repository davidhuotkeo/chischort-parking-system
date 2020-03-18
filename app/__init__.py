from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load views
from app.views import view

# Load database
from app.models import database

# Load utils
from app.utils import *

app.config.from_object("config.DevConfig")
