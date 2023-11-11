from flask_app import app
from flask_app.controllers import  users, chats, messages

chats_controllers = chats
users_controllers = users
messages_controllers = messages

if __name__== "__main__":
    app.run(debug=True)