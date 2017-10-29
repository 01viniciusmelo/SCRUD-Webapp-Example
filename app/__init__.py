"""
    investments_app_2
    ~~~~~

    A portfolio management webapp based on mysql, flask, flask-admin, plotly and datatables.

    :copyright: (c) 2017 by Phil Blower.
    :license: BSD, see LICENSE for more details.
"""

__version__ = 'v0.2.4'

# v0.2.2. Added 3, 5, 10 year annualized returns
# v0.2.3. Minor updates to comments, descriptions and minor fixes
# v0.2.4. Enhanced error messages in helpers.py/_get_web_data

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import conf

# Create application
app = Flask(__name__)
Bootstrap(app)

app.config.from_object(conf)
print('>>>>>>>>', 'configuration = ', conf, ">>>>>>>>")
db = SQLAlchemy(app)
print('>>>>>>>>', db, '>>>>>>>>')

from app import views, models
