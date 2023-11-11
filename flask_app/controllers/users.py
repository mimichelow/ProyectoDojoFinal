from flask_app import app
from flask import render_template, redirect,request, session, flash, url_for
from flask_bcrypt import Bcrypt

from models.user import User

@app.route("/login", methods="POST")
def login(email,password):
    if (user_id:=User.check_login(email=email, password=password)):
        user= User.get_user_by_id(user_id)
        session['id']= user["id"]
        session['fname'] = user["fname"]
        session["lname"] = user["lname"]
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('dashboard'))
@app.route("/logout", methods=["POST"])
def logout():
    session.clear
    return redirect(url_for("index"))
        