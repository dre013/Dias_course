from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user, login_required,logout_user
from flask import flash,request,render_template,redirect,url_for
from time import sleep

from application import db,app
from application.database import Login


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = request.form.get('rememberMe')
    if remember is  None:
        remember = False
    
    if username and password:
        user = Login.query.filter_by(username=username).first()
        login_user(user,remember=remember)
        if user and check_password_hash(user.password,password):
            login_user(user,remember=True)
            return recept()
        else:
            flash('Invalid username or password',category='error')
    else:
        flash('Please fill username or password',category='error')
    return render_template('login.html')


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'POST':
        if len(request.form['username'])!= 0:
            if len(request.form['password']) == len(request.form['password2']):
                if request.form['password'] == request.form['password2']:
                    hash = generate_password_hash(request.form.get('password'))
                    ses = Login(username = request.form['username'],password=hash)
                    if ses:
                        flash('Success registration',category='success')
                        db.session.add(ses)
                        db.session.commit()
                        sleep(2)
                        return redirect('/')
                    else:
                        flash('Error registration',category='error')
                        db.session.rollback()
                else:
                    flash('Password not same',category='error')
                    db.session.rollback()
            else:
                flash('Username is empty',category='error')
                db.session.rollback()
    return render_template('regist.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user
    return redirect(url_for('Hello World'))


@app.route('/recept/')
def recept():
    return render_template('recept.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html'),404


@app.route('/')
def index():
    return render_template('work.html')
