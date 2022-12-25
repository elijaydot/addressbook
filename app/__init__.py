from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_paginate import Pagination, get_page_parameter
import os

file_path = os.path.abspath(os.getcwd()) + "/addressbook.db"

app = Flask(__name__)
# paginate = Pagination(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_path

db = SQLAlchemy(app)

from app import routes

app.secret_key = 'xdeSUPERDALTON129484ppornsub4aihJVjbHVtcPbn{UvCTv;nPvYvpHCUycEZEcob'

