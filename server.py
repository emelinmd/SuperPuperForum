from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import Section

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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


if __name__ == '__main__':
    app.run(debug=True)
