from flask_app import app
from flask import render_template, redirect,request,session,flash,url_for
from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime
from flask_app.models import user
from flask_app.models import message
from flask_app.models import reaction
from datetime import date



class Chat:
    def __init__(self, data):
        self.id = data['id']
        self.user1_id = data['user1_id']
        self.user2_id = data['user2_id']
        self.last_message = ''
        self.time = ''
    
    @classmethod
    def get_by_id(cls, id):
        query = 'SELECT * FROM chats as t1 left join users as t2 on t1.user1_id=t2.id left join users as t3 on t1.user2_id=t3.id WHERE t1.id = %(id)s;'
        data = {'id': id}
        result = connectToMySQL().query_db(query, data)
        if result:
            x = cls(result[0])
            data_user1 = {
                "id" : result[0]["user1_id"],
                "fname" : result[0]["fname"],
                "lname" : result[0]["lname"],
                "nick" : result[0]["nick"],
                "email" : result[0]["email"],
                "picture" : result[0]["picture"]}
            data_user2 = {
                "id" : result[0]["user2_id"],
                "fname" : result[0]["t3.fname"],
                "lname" : result[0]["t3.lname"],
                "nick" : result[0]["t3.nick"],
                "email" : result[0]["t3.email"],
                "picture" : result[0]["t3.picture"]}
            x.user1_id = user.User(data_user1)
            x.user2_id = user.User(data_user2)
            return x
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
                user1_data = {
                "id" : chat["user1_id"],
                "fname" : chat["fname"],
                "lname" : chat["lname"],
                "nick" : chat["nick"],
                "email" : chat["email"],
                "picture" : chat["picture"]}
                user2_data = {
                "id" : chat["user2_id"],
                "fname" : chat["t4.fname"],
                "lname" : chat["t4.lname"],
                "nick" : chat["t4.nick"],
                "email" : chat["t4.email"],
                "picture" : chat["t4.picture"]}
                new_chat.user1_id = user.User(user1_data)
                new_chat.user2_id = user.User(user2_data)
                if session['id'] == user2_data['id']:
                    x = new_chat.user1_id
                    new_chat.user1_id = new_chat.user2_id
                    new_chat.user2_id = x
                message_data = {
                'content' : chat['content'],
                'timestamp' : chat['timestamp'],
                'chat_id' : chat['chat_id']
                }
                new_chat.last_message = message.Message(message_data)
                
                if new_chat.last_message.timestamp != None:
                    date_now=date.today()
                    if new_chat.last_message.timestamp.month==date_now.month and new_chat.last_message.timestamp.day==date_now.day and new_chat.last_message.timestamp.year==date_now.year:
                        print('IM AM IN')
                        new_chat.last_message.timestamp = new_chat.last_message.timestamp.strftime('%H:%M')
                    # elif same_week(new_chat.last_message.timestamp):
                    #     new_chat.last_message.timestamp =new_chat.last_message.timestamp.strftime('%A') 
                    else:
                        new_chat.last_message.timestamp = new_chat.last_message.timestamp.strftime('%m/%d/%Y')
                    all_chats.append(new_chat)
                new_chat.time = new_chat.last_message.timestamp
            return all_chats
        else:
            return []
    
    def save(data):
        query = 'INSERT INTO chats (user1_id,user2_id,created_at,updated_at) VALUES (%(user1_id)s, %(user2_id)s,now(),now());'
        result=connectToMySQL().query_db(query, data)
        print("SAVE RESULT", result)
        return result
    
    @staticmethod
    def selectionSort(array):
        size = len(array)-1
        for ind in range(0,size): 
            min_index = ind
            for j in array[0:min_index+1]: 
                if array[min_index+1].time < j.time:
                    x= array.pop(min_index+1)
                    array.insert(min_index,x)
                    min_index = min_index -1


def same_week(dateString):
    '''returns true if a dateString in %Y%m%d format is part of the current week'''
    d1 = dateString
    d2 = datetime.today()
    return d1.isocalendar()[1] == d2.isocalendar()[1] and d1.year == d2.year  