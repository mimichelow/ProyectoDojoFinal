from flask_app import app
from flask import render_template, redirect,request,session,flash,url_for
from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime
from flask_app.models import user
from flask_app.models import message


class Chat:
    def __init__(self, data):
        self.id = data['id']
        self.user1_id = data['user1_id']
        self.user2_id = data['user2_id']
        self.last_message = ''
        self.time = ''
    
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
        query = 'SELECT * FROM chats as t1 left join users as t3 on t1.user1_id=t3.id left join users as t4 on t1.user2_id=t4.id left join  ( SELECT m.* FROM messages m JOIN (SELECT chat_id, MAX(timestamp) AS latest_timestamp FROM messages GROUP BY chat_id) latest_messages ON m.chat_id = latest_messages.chat_id AND m.timestamp = latest_messages.latest_timestamp ) as t2 on t1.id=t2.chat_id WHERE t1.user1_id = %(user_id)s OR t1.user2_id = %(user_id)s;'
        results = connectToMySQL().query_db(query, data)
        all_chats = []
        if results:
            for chat in results:
                new_chat = cls(chat)
                print(chat)
                user1_data = {
                "id" : chat["user1_id"],
                "fname" : chat["fname"],
                "lname" : chat["lname"],
                "nick" : chat["nick"],
                "email" : chat["email"],
                "picture" : chat["picture"]}
                new_chat.user1_id = user.User(user1_data)
                user2_data = {
                "id" : chat["user2_id"],
                "fname" : chat["t4.fname"],
                "lname" : chat["t4.lname"],
                "nick" : chat["t4.nick"],
                "email" : chat["t4.email"],
                "picture" : chat["t4.picture"]}
                new_chat.user2_id = user.User(user2_data)
                message_data = {
                'content' : chat['content'],
                'timestamp' : chat['timestamp'],
                'chat_id' : chat['chat_id']
                }
                new_chat.last_message = message.Message(message_data)
                if new_chat.last_message.timestamp != None:
                    new_chat.last_message.timestamp = new_chat.last_message.timestamp.strftime('%Y-%m-%d-%H-%M-%S ')
                    all_chats.append(new_chat)
                new_chat.time = new_chat.last_message.timestamp
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
    
    @staticmethod
    def selectionSort(array):
        size = len(array)-1
        for ind in range(0,size): 
            print(f"Original loop {ind}--------------------------")
            min_index = ind
            for j in array[0:min_index+1]: 
                print(f"This is the pointer{array[min_index+1].time}")
                if array[min_index+1].time < j.time:
                    print("True")
                    x= array.pop(min_index+1)
                    array.insert(min_index,x)
                    min_index = min_index -1
                else:
                    print("False")
                print(array)


