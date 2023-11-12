from flask_app import app
from flask import render_template, redirect,request, session, flash, url_for
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User 


@app.route('/index')
def index():
    if 'id' in session:
        return redirect('/dashboard')
    else:
        return  render_template('register_login.html')

@app.route('/login', methods=['POST'])
def signin():
    print(request.form)
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
    

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect ('/')


@app.route('/user/profile')
def profile():
    if session.get('id') == None:
        return redirect('/')
    return render_template('edit_profile.html')



@app.route('/signup', methods=['POST'])
def signup():
    print(request.form)
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
