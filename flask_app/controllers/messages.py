from flask_app import app
from flask import session, redirect, url_for, flash, render_template,jsonify,request
from flask_app.models.chat import Chat 
from flask_app.models.message import Message 


@app.route('/new_message' , methods=['POST'])
def new_message():
    if 'id' in session:
        form=dict(request.form)
        form['chat-id']=session['chat-id']
        #Chat-ID por ahora lo estoy poniendo en session pero esto se puede cambiar a una mejor implementacion
        Message.save(form)
        return jsonify(Message.get_last_json())
    else:
        return redirect(url_for('chats_dashboard'))
