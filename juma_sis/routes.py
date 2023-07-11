from flask import render_template, redirect, url_for, flash, request
from juma_sis import app, database, bcrypt
import juma_sis.forms as fm
from juma_sis.models import Filhos, Responsavel, Usuario
from datetime import datetime
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/filhos', methods=['GET', 'POST'])
@login_required
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
        if form_filho.nomeresp and Responsavel.query.filter_by(cpf=form_filho.cpfresp.data).all() == []:
            responsavel = Responsavel(nome=form_filho.nomeresp.data, cpf=form_filho.cpfresp.data, telefone=form_filho.telefoneresp.data)
            database.session.add(responsavel)
            database.session.commit()
            filho = Filhos.query.filter_by(cpf=form_filho.cpf.data).first()
            idresponsavel = Responsavel.query.filter_by(cpf=form_filho.cpfresp.data).first().idresp
            filho.idresp = int(idresponsavel)
            database.session.commit()
        else:
            filho = Filhos.query.filter_by(cpf=form_filho.cpf.data).first()
            idresponsavel = Responsavel.query.filter_by(cpf=form_filho.cpfresp.data).first().idresp
            filho.idresp = int(idresponsavel)
            database.session.commit()
        flash(f'Cadastro de {form_filho.nome.data} feito com sucesso', 'alert-success')
        return redirect(url_for('filhos'))
    return render_template('filhos.html', form_filho=form_filho)

@app.route('/giras', methods=['GET', 'POST'])
@login_required
def giras():
    form_gira = fm.RegistroGiras()
    form_presenca = fm.RegistroPresenca()
    return render_template('giras.html', form_gira=form_gira, form_presenca=form_presenca)

@app.route('/financeiro', methods=['GET', 'POST'])
@login_required
def mensalidades():
    return render_template('mensalidades.html')

@app.route('/deitagem', methods=['GET', 'POST'])
@login_required
def deitagem():
    form_deitagem = fm.RegistroDeitagem()
    return render_template('deitagem.html', form_deitagem=form_deitagem)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = fm.FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter(Usuario.username == form_login.username.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.remember.data)
            flash(f'Login feito com sucesso para o email: {form_login.username.data}', 'alert-success')
            next_par = request.args.get('next')
            if next_par:
                return redirect(next_par)
            else:
                return redirect(url_for('home'))
        else:
            flash(f'Email ou senha inválidos', 'alert-danger')
    return render_template('login.html', form_login=form_login)

@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html')

@app.route('/perfil_filho')
@login_required
def perfil_filho():
    return render_template('perfil_filho.html')

@app.route('/sair')
def sair():
    logout_user()
    flash(f'Logout feito com sucesso', 'alert-success')
    return redirect(url_for('home'))