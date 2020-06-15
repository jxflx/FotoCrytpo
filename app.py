from flask import Flask, request, session, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from views import *

import os

app = Flask(__name__)

dbdir = 'sqlite:///' + os.path.abspath(os.getcwd()) + '/database.db'

app.config['SQLALCHEMY_DATABASE_URI'] = dbdir
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = '+q#\.V7_\cdFmFBQ_zTmys&ZWA@6Wx'
newUser = None
pin = randint(1000, 9999)


class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key = True
    )
    username = db.Column(
        db.String(50),
        nullable = False
    )
    password = db.Column(
        db.String(100),
        nullable = False
    )
    email = db.Column(
        db.String(50),
        nullable = False
    )


@app.route('/')
def index():
    return indexView()

@app.route('/encrypt', methods=['GET', 'POST'])
def encryptFile():
    return encryptView()

@app.route('/login', methods=["GET", "POST"])
def login():
    return loginView()


@app.route('/signup', methods=["GET", "POST"])
def signup():
    return signupView()



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)