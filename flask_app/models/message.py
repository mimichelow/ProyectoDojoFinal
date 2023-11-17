from flask_app import app
from flask import render_template, redirect,request,session,flash,url_for
from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime
from flask_app.models import user
from flask_app.models import chat
from flask_app.models import reaction

class Message:
    def __init__(self, data):
        self.content = data['content']
        self.timestamp = data['timestamp']
        self.chat_id = data['chat_id']
        self.user_id = session['id']
        
    @classmethod
    def get_all_by_chat_id(cls, data):
        query = 'SELECT * FROM messages as t1 left join chats as t2 on t1.chat_id=t2.id left join users as t3 on user_id=t3.id left join users as t4 on t2.user2_id=t4.id left join reactions as t5 on t1.id=t5.message_id WHERE t1.chat_id = %(id)s ORDER BY timestamp asc;'
        return connectToMySQL().query_db(query, data)
        
    @classmethod
    def get_all_by_user_id(cls, user_id):
        query = 'SELECT * FROM messages WHERE user_id = %(user_id)s ORDER BY timestamp DESC;'
        data = {'user_id': user_id}
        return connectToMySQL().query_db(query, data)
        
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO messages (content, timestamp, chat_id,user_id) VALUES (%(content)s, now(), %(chat_id)s,%(user_id)s);'
        return connectToMySQL().query_db(query, data)
    
    @classmethod
    def get_last_json(cls):
        query = "SELECT * FROM messages ORDER BY timestamp DESC LIMIT 1;"
        results = connectToMySQL().query_db(query)
        return results