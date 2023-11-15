from flask_app import app
from flask import render_template, redirect,request, session, flash, url_for
from flask_bcrypt import Bcrypt
from flask_app.models.user import User 
from flask import request
from werkzeug.utils import secure_filename
import os
app.config['UPLOAD_FOLDER'] = './flask_app/static/uploads'

bcrypt = Bcrypt(app)

@app.route('/index')
def index():
    if 'id' in session:
        return redirect('/dashboard')
    else:
        return  render_template('register_login.html')

@app.route('/login', methods=['POST'])
def signin():
    email = request.form.get('email')
    pswrd = request.form.get('pswrd')
    if (user_id:=User.check_login(email=email, pswrd=pswrd)):
        user= User.get_user_by_id(user_id)
        session['id']= user.id
        session['fname'] = user.fname
        session['lname'] = user.lname
        return redirect('/dashboard')
    else:
        return redirect('/dashboard')
    

@app.route("/logout", methods=["GET","POST"])
def logout():
    session.clear()
    return redirect ('/')


@app.route('/user/profile')
def profile():
    if session.get('id') == None:
        return redirect('/')
    user = User.get_user_by_id(session['id'])
    return render_template('edit_profile.html',user=user)


@app.route('/edit_profile', methods=['POST'])
def edit_profile():
    if not User.validate_entry2(request.form):
        return redirect('/user/profile')
    data = {'fname': request.form.get('fname'),
            'lname':request.form.get('lname'),
            'email':request.form.get('email'),
            'nick':request.form.get('nick'),
            'id':session['id']
            }
    profile_picture = request.files.get('profilePicture')
    if profile_picture:
        filename = secure_filename(profile_picture.filename)
        profile_picture.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        data['picture']=filename
    else:
        data['picture']='user.webp'
    User.update(data)
    return redirect('/user/profile')



@app.route('/signup', methods=['POST'])
def signup():
    if not User.validate_entry(request.form):
        return redirect('/')
    data = {
    'email' : request.form.get('email')
            }
    user=User.getbyemail(data)
    if user is not None:
        flash(['Email address has been already registered!',0])
        return redirect('/')
    data = {
    'fname' : request.form.get('fname'),
    'lname' : request.form.get('lname'),
    'email' : request.form.get('email'),
    'pswrd' : bcrypt.generate_password_hash(request.form.get('pswrd'))
            }
    userid=User.save(data)
    data['user_id'] = userid
    login = User.create_login(data)
    session['id']= userid
    session['fname'] = data['fname']
    session['lname'] = data['lname']
    return redirect('/dashboard')
