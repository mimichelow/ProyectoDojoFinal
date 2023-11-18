from flask_app import app
from flask import render_template, redirect,request,session,flash,url_for
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import user
from flask_app.models import chat
from flask_app.models import message

class Reaction:
    def __init__(self, data):
        self.content = data['reaction']
        self.timestamp = data['message_id']

    @classmethod
    def get_by_message(cls,data):
        query = 'select * from reactions where message_id=%(message_id)s;'
        result = connectToMySQL().query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return None
        
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO reactions (reaction, message_id) VALUES (%(reaction)s, %(message_id)s);'
        return connectToMySQL().query_db(query, data)
    @classmethod
    def update(cls,data):
        query = 'update reactions set reaction=%(reaction)s where message_id= %(message_id)s;'
        return connectToMySQL().query_db(query, data)