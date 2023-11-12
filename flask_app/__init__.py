from flask import Flask
from flask import redirect, url_for, session, render_template




app = Flask(__name__)

app.secret_key = "Whatsdown es la mejor app"

