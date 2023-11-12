from flask_app import app
from flask import session, redirect, url_for, flash, render_template
from flask_app.models.chat import Chat 
from flask_app.models.message import Message 


@app.route('/')
@app.route('/dashboard', methods=['GET', 'POST'])
def chats_dashboard():
    if 'id' in session:
        data = {'user_id' : session['id']}
        all_chats = Chat.get_all_by_user(data)
        print(all_chats)
        return render_template('chats_dashboard.html',all_chats=all_chats)
    else:
        return redirect(url_for('index'))

@app.route('/chats/<int:id>')
def view_chat(id):
    chat = Chat.get_by_id(id)
    if session['id'] != chat.user1_id and session['id'] != chat.user2_id:
        return redirect(url_for('dashboard'))
    session['chat-id'] = id
    messages = Message.get_all_by_chat_id(id)
    return render_template('chat_view.html', messages=messages,chat_id=id)
