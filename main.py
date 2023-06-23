from flask import Flask, render_template
import secret
from forms import FormLogin

app = Flask(__name__)

app.config['SECRET_KEY'] = secret.secret_key

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/filhos')
def filhos():
    return render_template('filhos.html')

@app.route('/giras')
def giras():
    return render_template('giras.html')

@app.route('/financeiro')
def mensalidades():
    return render_template('mensalidades.html')

@app.route('/login')
def login():
    form_login = FormLogin()
    return render_template('login.html', form_login=form_login)

if __name__ == '__main__':
    app.run(debug=True)