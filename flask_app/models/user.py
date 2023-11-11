from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template, redirect,request,session,flash,url_for
from config.mysqlconnection import connectToMySQL

from flask_app.models.message import Message
from flask_app.models.chat import Chat



class User:
    def __init__(self, data):
        self.fname = data["fname"]
        self.lname = data["lname"]
        self.nick = data["nick"]
        self.email = data["email"]
        self.picture = data["picture"]
    
    @classmethod
    def get_user_by_id(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {"id": id}
        result = connectToMySQL().query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return None

    @classmethod
    def check_login(cls, email, password):
        query = "SELECT id, email, password FROM users LEFT JOIN logins ON users.id = logins.user_id WHERE email = %(email)s;"
        data = {"email": email}
        result = connectToMySQL().query_db(query, data)
        if result and Bcrypt().check_password_hash(result[0]['password'], password):
            return result[0]['id']
        else:
            return None
        
    @classmethod
    def create_login(cls, id, email, password):
        query = "INSERT INTO logins (email, password, user_id) VALUES (%(email)s, %(password)s, %(user_id)s);"
        data = {
            "email": email,
            "password": Bcrypt().generate_password_hash(password),
            "user_id": id
        }
        return connectToMySQL().query_db(query, data)
    
    def save(self):
        query = "INSERT INTO users (fname, lname, nick, email, picture) VALUES (%(fname)s, %(lname)s, %(nick)s, %(email)s, %(picture)s);"
        data = {
            "fname": self.fname,
            "lname": self.lname,
            "nick": self.nick,
            "email": self.email,
            "picture": self.picture
        }
        return connectToMySQL().query_db(query, data)
