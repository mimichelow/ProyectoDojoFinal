from flask_app import app
from flask import session, redirect, url_for, flash, render_template

from models.chat import Chat 
from models.message import Message


@app.route("/dashboard/")
def chats_dashboard():
    if 'id' in session:
        return url_for('chats_dashboard.html')
    else:
        return redirect(url_for('index'))
    
@app.route("/chats/<int:id>")
def view_chat(id):
    chat = Chat.get_by_id(id)
    if session['id'] != chat.user1_id and session['id'] != chat.user2_id:
        return redirect(url_for('dashboard'))
    messages = Message.get_all_by_chat_id(id)
    return render_template('chat_view.html', messages=messages)
