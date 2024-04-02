from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from models import Section, User


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


@app.route('/sections')
def sections():
    all_sections = Section.query.all()
    return render_template('sections.html', sections=all_sections)


@app.route('/sections/<int:section_id>')
def topics(section_id):
    section = Section.query.get_or_404(section_id)
    return render_template('topics.html', section=section)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
        return render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




if __name__ == '__main__':
    app.run(debug=True)
