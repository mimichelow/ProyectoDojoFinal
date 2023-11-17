from flask_app import app
from flask import session, redirect, url_for, flash, render_template,jsonify,request
from flask_app.models.chat import Chat 
from flask_app.models.message import Message 
from flask_app.models.reaction import Reaction


@app.route('/new_reaction' , methods=['GET', 'POST'])
def new_reaction():
        data = request.get_json()
        validator = Reaction.get_by_message(data)
        if validator is None:
                data['reaction'] = 1
                Reaction.save(data)
        else:
                if validator.content == 0:
                        data['reaction'] = 1
                        Reaction.update(data)
                elif validator.content == 1:
                        data['reaction'] = 2
                        Reaction.update(data)
                elif validator.content == 2:
                        data['reaction'] = 0
                        Reaction.update(data)
        return jsonify({'message': 'Reaction saved successfully'})