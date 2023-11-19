from flask_app import app
from flask import session, redirect, url_for, flash, render_template,request,jsonify
from flask_app.models.chat import Chat 
from flask_app.models.message import Message 
from flask_app.models.user import User
from datetime import datetime
from datetime import date

@app.route('/')
@app.route('/dashboard', methods=['GET', 'POST'])
def chats_dashboard():
    if 'id' in session:
        data = {'user_id' : session['id']}
        all_chats = Chat.get_all_by_user(data)
        Chat.selectionSort(all_chats)
        all_chats.reverse()
        return render_template('chats_dashboard.html',all_chats=all_chats)
    else:
        return redirect(url_for('index'))
    
@app.route('/chats_dash_ajax')
def chats_dash_ajax():
    data = {'user_id' : session['id']}
    all_chats = Chat.get_all_by_user_json(data)
    for x in all_chats:
        if x['timestamp'] != None:
            date_now=date.today()
        if x['timestamp'].month==date_now.month and x['timestamp'].day==date_now.day and x['timestamp'].year==date_now.year:
            x['timestamp'] = x['timestamp'].strftime('%H:%M')
        else:
            x['timestamp'] = x['timestamp'].strftime('%m/%d/%Y')
    return jsonify(all_chats)


@app.route('/chats/<int:id>')
def view_chat(id):
    if session.get('id') == None:
        return redirect('/')
    chat = Chat.get_by_id(id)
    if session['id'] != chat.user1_id.id and session['id'] != chat.user2_id.id:
        return redirect('/')
    session['chat-id'] = id
    if chat.user2_id.id == session['id']:
        chat.user1_id, chat.user2_id = chat.user2_id, chat.user1_id
    Message.update_seen({'user_id':session['id'],'chat_id':id})
    return render_template('chat_view.html',chat_id=id,chat=chat)

@app.route('/create_chat', methods=['POST'])
def create_chat():
    reciever=User.get_user_by_email(request.form['email'])
    if reciever is None:
        flash("The email you entered is not registered in our database")
        return redirect(url_for('chats_dashboard'))
    data={
    'user1_id':session['id'],
    'user2_id':reciever.id
    }
    chat_id=Chat.save(data)

    return redirect(url_for('view_chat',id=chat_id))