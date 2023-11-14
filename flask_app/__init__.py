from flask import Flask
from flask import redirect, url_for, session, render_template
from flask_cors import CORS



app = Flask(__name__)
CORS(app) ###########To avoid issues with blocked by CORS policy
app.secret_key = "Whatsdown es la mejor app"

