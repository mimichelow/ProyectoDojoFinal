from flask_app import app
from flask import render_template, redirect,request,session,flash,url_for
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import user
from flask_app.models import message

class Chat:
    def __init__(self, data):
        self.id = data['id']
        self.user1_id = data['user1_id']
        self.user2_id = data['user2_id']
    
    @classmethod
    def get_by_id(cls, id):
        query = 'SELECT * FROM chats WHERE id = %(id)s;'
        data = {'id': id}
        result = connectToMySQL().query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return None
    
    @classmethod
    def get_all_by_user(cls, data):
        query = 'SELECT * FROM chats WHERE user1_id = %(user_id)s OR user2_id = %(user_id)s;'
        results = connectToMySQL().query_db(query, data)
        all_chats = []
        if results:
            for chat in results:
                new_chat = cls(chat)
                data_user1 = {
                    'id' : chat["user1_id"]
                }
                user1 = user.User.get_user_by_id(data_user1)
                new_chat.user1_id = user1
                data_user2 = {
                    'id' : chat["user1_id"]
                }
                user1 = user.User.get_user_by_id(data_user1)
                new_chat.user1_id = user1
                all_chats.append(new_chat)
            return all_chats
        else:
            return []
    
    def save(self):
        query = 'INSERT INTO chats (user1_id,user2_id,created_at,updated_at) VALUES (%(user1_id)s, %(user2_id)s,now(),now());'
        data = {
            'user1_id': self.user1_id,
            'user2_id': self.user2_id,
        }
        return connectToMySQL().query_db(query, data)