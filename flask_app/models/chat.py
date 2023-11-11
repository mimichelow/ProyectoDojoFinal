from flask_app import app
from flask import render_template, redirect,request,session,flash,url_for
from config.mysqlconnection import connectToMySQL

from flask_app.models.user import User
from flask_app.models.message import Message

class Chat:
    def __init__(self, data):
        self.user1_id = data["user1_id"]
        self.user2_id = data["user2_id"]
    
    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM chats WHERE id = %(id)s;"
        data = {"id": id}
        result = connectToMySQL().query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return None
    
    @classmethod
    def get_all_by_user(cls, user_id):
        query = "SELECT * FROM chats WHERE user1_id = %(user_id)s OR user2_id = %(user_id)s;"
        data = {"user_id": user_id}
        results = connectToMySQL().query_db(query, data)
        if results:
            return [cls(result) for result in results]
        else:
            return []
    
    def save(self):
        query = "INSERT INTO chats (user1_id,user2_id) VALUES (%(user1_id)s, %(user2_id)s);"
        data = {
            "user1_id": self.user1_id,
            "user2_id": self.user2_id,
        }
        return connectToMySQL().query_db(query, data)