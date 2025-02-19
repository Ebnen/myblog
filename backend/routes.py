from flask import Flask, render_template, url_for, flash, redirect
from werkzeug.security import check_password_hash
from data import session
from  form import registration, login
from flask_login import login_user
from flask_login import LoginManager, UserMixin, logout_user,current_user, login_required,login_user
from rare import User, Post

app = Flask(__name__)
log_direct = LoginManager(app) 
app.config['SECRET_KEY'] = '08033191820eE'

gists=[
    {
        'Name': 'obinna eze',
        'title': 'My feelings',
        'content': 'I hate this world',
        'date': '12-09-2013'
    },
    {
        'Name': 'legis sam',
        'title': 'My feelings',
        'content': 'i love this girl',
        'date': '12-09-2015'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', gists=gists, title='My Perception')

@app.route("/about")
def about():
    return render_template("about.html", title='About-info')

@app.route('/templates/reg', methods=['GET','POST'])
def reg():
    yam = registration()
    if yam.validate_on_submit():
        user = User(name=yam.name.data,username=yam.username.data,email=yam.email.data,password=yam.password.data)
        session.add(user)
        session.commit()
        flash(f'Account created for {yam.name.data}!', 'success')
        return redirect(url_for('sucess'))
    return render_template('reg.html', title='Registration', yam=yam)


@app.route('/log', methods=['GET','POST'])
def log():
    sign = login()
    if sign.validate_on_submit():
        user = session.query(User).filter_by(username=sign.username.data).first()
        if user and check_password_hash(user.password, sign.password.data):
            login_user(user, remember=sign.remember.data)
            return redirect(url_for("home"))
        else:
            flash('incorrect login credential try again', 'grape')
    return render_template('log.html', title='login', sign=sign)


@app.route('/sucess')
def sucess():
    yam = registration()
    return render_template('sucess.html', title='sucess', yam=yam)


if __name__ == '__main__':
    app.run(debug=True)