from flask import render_template, redirect, url_for, flash
from juma_sis import app, database
import juma_sis.forms as fm
from juma_sis.models import Filhos, Gira, Financeiro, Responsavel
from datetime import datetime
from wtforms import BooleanField

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/filhos', methods=['GET', 'POST'])
def filhos():
    form_filho = fm.RegistroFilho()
    if form_filho.validate_on_submit():
        data_str_nascimento = f'{form_filho.nascimento_ano.data}-{form_filho.nascimento_mes.data}-{form_filho.nascimento_dia.data}'
        data_nascimento = datetime.strptime(data_str_nascimento, "%Y-%m-%d")
        data_str_inicio = f'{form_filho.inicio_ano.data}-{form_filho.inicio_mes.data}-{form_filho.inicio_dia.data}'
        data_inicio = datetime.strptime(data_str_inicio, "%Y-%m-%d")
        filho = Filhos(nome=form_filho.nome.data, nascimento=data_nascimento, inicio=data_inicio, orixa1=form_filho.orixa1.data,
                       orixa2=form_filho.orixa2.data, orixa3=form_filho.orixa3.data, telefone=form_filho.telefone.data,
                       email=form_filho.email.data, rg=form_filho.rg.data, cpf=form_filho.cpf.data, rua=form_filho.rua.data,
                       ncasa=form_filho.ncasa.data, complemento=form_filho.complemento.data, bairro=form_filho.bairro.data,
                       cidade=form_filho.cidade.data, uf=form_filho.uf.data)
        database.session.add(filho)
        database.session.commit()
    if form_filho.nomeresp:
        responsavel = Responsavel(nome=form_filho.nomeresp.data, cpf=form_filho.cpfresp.data,
                                  telefone=form_filho.telefoneresp.data)
        database.session.add(responsavel)
        database.session.commit()
        filho = Filhos.query.filter_by(cpf=form_filho.cpf.data).first()
        idresponsavel = Responsavel.query.filter_by(cpf=form_filho.cpfresp.data).first().idresp
        filho.idresp = int(idresponsavel)
        database.session.commit()
    return render_template('filhos.html', form_filho=form_filho)

@app.route('/giras', methods=['GET', 'POST'])
def giras():
    form_gira = fm.RegistroGiras()
    form_presenca = fm.RegistroPresenca()
    return render_template('giras.html', form_gira=form_gira, form_presenca=form_presenca)

@app.route('/financeiro', methods=['GET', 'POST'])
def mensalidades():
    return render_template('mensalidades.html')

@app.route('/deitagem', methods=['GET', 'POST'])
def deitagem():
    form_deitagem = fm.RegistroDeitagem()
    return render_template('deitagem.html', form_deitagem=form_deitagem)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = fm.FormLogin()
    if form_login.validate_on_submit():
        #realizou login
        flash(f'Login feito com sucesso para o email: {form_login.username.data}', 'alert-success')
        #redirecionando para pagina filhos
        return redirect(url_for('filhos'))
    return render_template('login.html', form_login=form_login)