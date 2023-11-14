from flask_app import app
from flask import session, redirect, url_for, flash, render_template,jsonify,request
from flask_app.models.chat import Chat 
from flask_app.models.message import Message 

@app.route('/messages')
def users():
    print(session['chat-id'])
    data = {'id': session['chat-id']}
    return jsonify(Message.get_all_by_chat_id(data))

@app.route('/new_message' , methods=['POST'])
def new_message():
    print(request.form)
    data = {"chat_id": request.form.get('chat_id'),
            "content": request.form.get('content'),
            'user_id': request.form.get('user_id')}
    Message.save(data)
    return jsonify(Message.get_last_json())
