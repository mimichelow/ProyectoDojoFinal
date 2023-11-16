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
        Chat.selectionSort(all_chats)
        all_chats.reverse()
        return render_template('chats_dashboard.html',all_chats=all_chats)
    else:
        return redirect(url_for('index'))

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
    return render_template('chat_view.html',chat_id=id,chat=chat)

@app.route('/create_chat')
def create_chat():
    return render_template('create_chat.html')