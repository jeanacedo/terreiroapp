from flask import render_template, redirect, url_for, flash, request
from juma_sis import app, database
from juma_sis.forms import FormLogin

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