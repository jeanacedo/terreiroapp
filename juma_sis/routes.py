from flask import render_template, redirect, url_for, flash, request
from juma_sis import app, database
import juma_sis.forms as fm
from juma_sis.models import Filhos
from datetime import datetime

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/filhos', methods=['GET', 'POST'])
def filhos():
    form_filho = fm.RegistroFilho()
    data_str_nascimento = f'{form_filho.nascimento_ano.data}-{form_filho.nascimento_mes.data}-{form_filho.nascimento_dia.data}'
    data_nascimento = datetime.strptime(data_str_nascimento, "%Y-%m-%d")
    data_str_inicio = f'{form_filho.inicio_ano.data}-{form_filho.inicio_mes.data}-{form_filho.inicio_dia.data}'
    data_inicio = datetime.strptime(data_str_inicio, "%Y-%m-%d")
    if form_filho.validate_on_submit():
        filho = Filhos(nome=form_filho.nome.data, nascimento=data_nascimento, inicio=data_inicio, orixa1=form_filho.orixa1.data,
                       orixa2=form_filho.orixa2.data, orixa3=form_filho.orixa3.data, telefone=form_filho.telefone.data,
                       email=form_filho.email.data, rg=form_filho.rg.data, cpf=form_filho.cpf.data, rua=form_filho.rua.data,
                       ncasa=form_filho.ncasa.data, complemento=form_filho.complemento.data, bairro=form_filho.bairro.data,
                       cidade=form_filho.cidade.data, uf=form_filho.uf.data)
        database.session.add(filho)
        database.session.commit()
    return render_template('filhos.html', form_filho=form_filho)

@app.route('/giras')
def giras():
    return render_template('giras.html')

@app.route('/financeiro')
def mensalidades():
    return render_template('mensalidades.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = fm.FormLogin()
    if form_login.validate_on_submit():
        #realizou login
        flash(f'Login feito com sucesso para o email: {form_login.username.data}', 'alert-success')
        #redirecionando para pagina filhos
        return redirect(url_for('filhos'))
    return render_template('login.html', form_login=form_login)