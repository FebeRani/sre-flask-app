from flask import Flask
from flask_sqlalchemy import SQLAlchemy

hello = Flask(__name__)

hello.config['SQLALCHEMY_DATABASE_URI']="mysql://root:Feberani7@localhost/sre"
hello.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db=SQLAlchemy(hello)