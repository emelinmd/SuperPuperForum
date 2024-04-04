from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from forms import RegistrationForm, LoginForm
from flask import flash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
from extensions import db

db.init_app(app)

with app.app_context():
    db.create_all()

from models import User, Section, Topic

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@app.route('/')
@app.route('/index')
def index():
    params = {
        'title': 'Супер'
    }
    return render_template("index.html", **params)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('upload.html')


@app.route('/ask_question', methods=['GET', 'POST'])
def ask_question():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('ask_question.html')


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('Email уже зарегистрирован.')
            return redirect(url_for('register_user'))
        new_user = User(email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Регистрация прошла успешно. Пожалуйста, войдите в систему.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неверный логин или пароль.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Вход', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    app.run(debug=True)
