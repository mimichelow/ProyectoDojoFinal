from flask_app import app
from flask import render_template, redirect,request, session, flash, url_for,jsonify
from flask_bcrypt import Bcrypt
from flask_app.models.user import User 
from flask import request
from werkzeug.utils import secure_filename
import os
from deepface import DeepFace

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

def create_face_embeddings(user_id, img):
    # toma la imagen de caras, y guarda los embeddings de la primera
    embeddings = DeepFace.represent(img)
    User.store_embeddings(user_id, embeddings[0])
    
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
    
    face_recognition_image = request.files.get('faceValidation')
    if face_recognition_image:
        file_path = face_recognition_image.filename
        create_face_embeddings(session['id'],file_path)
        os.remove(file_path)
        
    
    if profile_picture:
        filename = secure_filename(profile_picture.filename)
        profile_picture.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        data['picture']=filename
    
    else:
        data['picture']='user.webp'
    User.update(data)
    return redirect('/user/profile')


@app.route("/face/login", methods=["POST"])
def facial_login():
    login_image = request.files.get('loginImage')
    if login_image:
        img_path = secure_filename(login_image.filename)
        login_image.save(os.path.join(app.config['UPLOAD_FOLDER'], img_path))
        embeddings = DeepFace.represent(img_path)
        embeddings = embeddings.tobytes()
        user_id=User.check_facial_login(embeddings)
        os.remove(img_path)
        if user_id:
            session['id']=user_id
            return redirect(url_for('chats_dashboard'))
        else:
            flash("That face doesn't belong to any user.")
            return redirect(url_for('index'))

    
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

@app.route ('/dark_mode_load', methods=['GET', 'POST'])
def darkMode():
    id=int(session['id'])
    result=User.getDarkMode(id)
    print(result)
    return jsonify(result[0])

@app.route ('/dark_mode_change/<mode>', methods=['GET', 'POST'])
def darkModeChange(mode):
    data={
        "mode": mode,
        "id"  : session["id"]
    }
    result=User.changeDarkMode(data)
    return jsonify(result)