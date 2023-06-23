from flask import Flask, render_template, url_for, request, flash, redirect
import secret
from forms import FormLogin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = secret.secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = secret.db_ri

database = SQLAlchemy(app)

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        #realizou login
        flash(f'Login feito com sucesso para o email: {form_login.username.data}', 'alert-success')
        #redirecionando para pagina filhos
        return redirect(url_for('filhos'))
    return render_template('login.html', form_login=form_login)

if __name__ == '__main__':
    app.run(debug=True)