from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

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

if __name__ == '__main__':
    app.run(debug=True)
