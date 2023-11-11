from flask import Flask
from flask import redirect, url_for

app = Flask(__name__)

app.secret_key = "Whatsdown es la mejor app"

@app.route('')
@app.route('/index/')
def index():
    return redirect(url_for('register_login.html'))