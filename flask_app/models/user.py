from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template, redirect,request,session,flash,url_for
from flask_app.config.mysqlconnection import connectToMySQL
from deepface import DeepFace
from datetime import datetime
import re
from flask_app.models import message
from flask_app.models import chat
import numpy as np
import json


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX= re.compile(r'[a-zA-Z]+$') 
PASSWORD_REGEX= re.compile(r'^(?=.{8,})(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.fname = data['fname']
        self.lname = data['lname']
        self.nick = data['nick']
        self.email = data['email']
        self.picture = data['picture']
        self.dark_mode="NO"
    
    @classmethod
    def get_user_by_id(cls, id):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        data = {'id': id}
        result = connectToMySQL().query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return None

    @classmethod
    def get_user_by_email(cls, email):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        data = {'email': email}
        result = connectToMySQL().query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return None


    @classmethod
    def check_login(cls, email, pswrd):
        query = 'SELECT users.id, users.email, logins.pwd FROM users LEFT JOIN logins ON users.id = logins.users_id WHERE email =  %(email)s;'
        data = {'email': email}
        result = connectToMySQL().query_db(query, data)
        if result and Bcrypt().check_password_hash(result[0]['pwd'], pswrd):
            return result[0]['id']
        else:
            flash(['Invalid Email/Password',1])
            return None
        
    @classmethod
    def create_login(cls, data):
        query = 'INSERT INTO logins (pwd, users_id) VALUES (%(pswrd)s, %(user_id)s);'
        return connectToMySQL().query_db(query, data)
    
    @classmethod
    def store_embeddings(cls, user_id, embeddings):
        embeddings_json = json.dumps(embeddings)
        query = 'UPDATE logins SET embeddings = %(embeddings)s WHERE users_id = %(user_id)s;'
        data = {'embeddings': embeddings_json, 'user_id': user_id}
        return connectToMySQL().query_db(query, data)
    
    @classmethod
    def check_facial_login(cls, embedding):
        query = 'SELECT users_id, embeddings FROM logins;'
        results = connectToMySQL().query_db(query)
        for user in results:
            if user['embeddings']:
                user_embedding = json.loads(user['embeddings'])
                user_embedding = user_embedding['embedding']
                cosine_similarity = np.dot(user_embedding, embedding) / (np.linalg.norm(user_embedding) * np.linalg.norm(embedding))
                if cosine_similarity > 0.60:
                    return user['users_id']
        return None
    
    @classmethod
    def save(cls,data):
        data['nick'] = data['fname'][0:1] + data['lname'] 
        query = 'INSERT INTO users (fname, lname, nick , email, picture,created_at) VALUES (%(fname)s, %(lname)s, %(nick)s ,%(email)s,"user.webp", now());'
        return connectToMySQL().query_db(query, data)
    
    @classmethod
    def update(cls,data): 
        query = 'UPDATE users SET fname = %(fname)s, lname = %(lname)s, nick = %(nick)s, email = %(email)s, `created_at` = now(), picture = %(picture)s WHERE id = %(id)s;'
        return connectToMySQL().query_db(query, data)
    

    @staticmethod
    def validate_entry(data):
        is_valid = True
        if len(data['fname']) <2:
            flash(['The first name should have at least 2 characters',0])
            is_valid= False
        if not NAME_REGEX.match(data['fname']):
            flash(['Your first name should not have numbers',0])
            is_valid= False
        if len(data['lname']) <2:
            flash(['The last name should have at least 2 characters',0])
            is_valid= False
        if not NAME_REGEX.match(data['lname']):
            flash(['Your last name should not have numbers',0])
            is_valid= False
        if not EMAIL_REGEX.match(data['email']): 
            flash(['Invalid email address!',0])
            is_valid = False
        if len(data['pswrd']) <8:
            flash(['The password should have at least 8 characters',0])
            is_valid = False
        if data['pswrd_confirm'] !=data['pswrd']:
            flash(['The password confirmation is not matching with the original password',0])
            is_valid= False
        if not PASSWORD_REGEX.match(data['pswrd']):
            flash(['Your password should have at least 8 characters with at least one lowercase and one uppercase ASCII character and also at least one character from the set @#$%^&+=, plus a number',0])
            is_valid= False
        return is_valid


    @staticmethod
    def validate_entry2(data):
        is_valid = True
        if len(data['fname']) <2:
            flash(['The first name should have at least 2 characters',1])
            is_valid= False
        if not NAME_REGEX.match(data['fname']):
            flash(['Your first name should not have numbers',1])
            is_valid= False
        if len(data['lname']) <2:
            flash(['The last name should have at least 2 characters',1])
            is_valid= False
        if not NAME_REGEX.match(data['lname']):
            flash(['Your last name should not have numbers',1])
            is_valid= False
        if not EMAIL_REGEX.match(data['email']) or data['email']=='': 
            flash(['Invalid email address!',1])
            is_valid = False
        if len(data['nick']) <5:
            flash(['The nick name should have at least 5 characters',1])
            is_valid= False
        return is_valid



    @classmethod
    def getbyemail(cls, data):
        query = 'select * from users where email = %(email)s;'
        mysql = connectToMySQL()
        result = mysql.query_db(query, data)
        if len(result) > 0:
            return cls(result[0])
        else:
            return None
    
    @classmethod
    def getDarkMode(cls, id):
        query = f'select dark_mode from users where id = {id};'
        mysql = connectToMySQL()
        result = mysql.query_db(query)
        return result
    @classmethod
    def changeDarkMode(cls,data):
        query = 'UPDATE users SET dark_mode=%(mode)s WHERE id = %(id)s;'
        mysql = connectToMySQL()
        result = mysql.query_db(query,data)
        return result

