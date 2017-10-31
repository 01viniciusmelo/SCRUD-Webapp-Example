"""
    SCRUD: Implemented using Python, Flask, SQLAlchemy, DataTables, JQuery, AJAX, JSON, and MySQL
"""

__version__ = 'v0.0.1'

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import conf

# Create application
app = Flask(__name__)
#Bootstrap(app)

app.config.from_object(conf)
print('>>>>>>>>', 'configuration = ', conf, ">>>>>>>>")
db = SQLAlchemy(app)
print('>>>>>>>>', db, '>>>>>>>>')

from app import views, models
