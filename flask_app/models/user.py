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
    def login(cls,email,password):
        pass
        
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
