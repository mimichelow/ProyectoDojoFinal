from flask import Flask
from flask import redirect, url_for, session, render_template

app = Flask(__name__)

app.secret_key = "Whatsdown es la mejor app"

@app.route('')
@app.route('/index/')
def index():
    if 'id' in session:
        return redirect(url_for('dashboard'))
    else:
        return  render_template('chats_dashboard.html')