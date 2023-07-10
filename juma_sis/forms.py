from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length
from juma_sis.models import Filhos
from juma_sis import app


class FormLogin(FlaskForm):
    username = StringField('Email', validators=[DataRequired(message='Campo obrigatório'), Email(message='Digite um email válido')])
    senha = PasswordField('Senha', validators=[DataRequired(message='Campo obrigatório')])
    remember = BooleanField('Lembrar acesso')
    button_submit = SubmitField('Login')

class RegistroFilho(FlaskForm):
    nome = StringField('Nome completo')
    nascimento_dia = StringField('Dia')
    nascimento_mes = StringField('Mês')
    nascimento_ano = StringField('Ano')
    inicio_dia = StringField('Dia')
    inicio_mes = StringField('Mês')
    inicio_ano = StringField('Ano')
    orixa1 = StringField('Orixá 1')
    orixa2 = StringField('Orixá 2')
    orixa3 = StringField('Orixá 3')
    telefone = StringField('Telefone')
    email = StringField('Email', validators=[Email(message='Email Inválido')])
    rg = StringField('RG')
    cpf = StringField('CPF', validators=[DataRequired(message='Campo obrigatório'), Length(min=11, max=11)])
    rua = StringField('Rua')
    ncasa = StringField('Número')
    complemento = StringField('Complemento')
    bairro = StringField('Bairro')
    cidade = StringField('Cidade')
    uf = StringField('UF')
    nomeresp = StringField('Responsável (se menor)')
    telefoneresp = StringField('Telefone responsável')
    button_submit = SubmitField('Cadastrar')

class RegistroGiras(FlaskForm):
    datagira_dia = StringField('Dia')
    datagira_mes = StringField('Mês')
    datagira_ano = StringField('Ano')
    assistencia = StringField('Quantidade de assistencia')
    linha1 = StringField('Primeira Linha')
    linha2 = StringField('Segunda Linha')
    button_submit = SubmitField('Cadastrar')

class RegistroPresenca(FlaskForm):
    submit = SubmitField('Presença')
class RegistroDeitagem(FlaskForm):
    datadeitagem_dia = StringField('Dia')
    datadeitagem_mes = StringField('Mês')
    datadeitagem_ano = StringField('Ano')
    orixa = StringField('Orixá')
    filho_deitagem = StringField('Filho que deitou')
    button_submit = SubmitField('Registrar')

with app.app_context():
    opcoes = Filhos.query.all()
    for opcao in opcoes:
        setattr(RegistroPresenca, f'opcao_{Filhos.matricula}', BooleanField(Filhos.nome))