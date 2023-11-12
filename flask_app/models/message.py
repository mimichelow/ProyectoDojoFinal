from flask_app import app
from flask import render_template, redirect,request,session,flash,url_for
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import user
from flask_app.models import chat

class Message:
    def __init__(self, data):
        self.content = data['content']
        self.timestamp = data['timestamp']
        self.chat_id = data['chat_id']
        self.user_id = session['id']
        
    @classmethod
    def get_all_by_chat_id(cls, id):
        query = 'SELECT * FROM messages WHERE chat_id = %(id)s ORDER BY timestamp DESC;'
        data = {'id': id}
        return connectToMySQL().query_db(query, data)
        
    @classmethod
    def get_all_by_user_id(cls, user_id):
        query = 'SELECT * FROM messages WHERE user_id = %(user_id)s ORDER BY timestamp DESC;'
        data = {'user_id': user_id}
        return connectToMySQL().query_db(query, data)
        
    def save(self):
        query = 'INSERT INTO messages (content, timestamp, chat_id) VALUES (%(content)s, now(), %(chat_id)s);'
        data = {
            'content': self.content,
            'timestamp': self.timestamp,
            'chat_id': self.chat_id
        }
        return connectToMySQL().query_db(query, data)
    @classmethod
    def get_last_json(cls):
        query = "SELECT * FROM messages ORDER BY timestamp DESC LIMIT 1;"
        results = connectToMySQL().query_db(query)
        return results