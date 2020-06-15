from flask import Flask, request, session, render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from cryptosteganography import CryptoSteganography
from double_auth import send_verfication
from random import randint
from app import *

import os

def indexView():
    if "username" in session:
        return render_template('home.html', username=session['username'])
    return render_template('index.html')

def encryptView():
    if request.method == 'POST':
        f = request.files['myfile']
        filename = f.filename
        f.save(f'./upload/{filename}')

        return 'Salvado!'

    return """
<form method="POST" enctype="multipart/form-data">
<input type="file" name="myfile">
<input type="submit" value="Upload">
</form> 
"""

def loginView():
    if request.method == "POST":
        user = User.query.filter_by(
            email=request.form["email"]
        ).first()

        if user and check_password_hash(user.password, request.form["password"]):
            session["username"] = user.username
            return redirect(url_for('index'))
        flash('Tus credenciales son inválidas, inténtalo de nuevo', 'danger')

    return render_template('login.html')

def signupView():
    global pin
    global newUser

    if request.method == "POST":
        if int(request.form['code']) > 0:
            usrcode = int(request.form['code'])
            if pin == usrcode:
                confirmedUser = User(
                    username = newUser['username'],
                    email    = newUser['email'],
                    password = newUser['password']
                )

                db.session.add(confirmedUser)
                db.session.commit()
                pin     = randint(1000, 9999)
                newUser = None
                return redirect(url_for('login'))
            else:
                flash('Incorrecto :(', 'danger')
                return render_template('confirm.html')
        else:
            hashed_pw = generate_password_hash(request.form["password"], method="sha256")
            newUser   = {
                'username': request.form["username"],
                'email': request.form["email"],
                'password': hashed_pw
            }

            send_verfication(pin, newUser['email'])

            flash("¡Te has registrado exitosamente!", "success")
            return render_template('confirm.html', mail=newUser['email'])

    return render_template('signup.html')
