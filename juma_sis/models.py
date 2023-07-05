from juma_sis import database



class Usuario(database.Model):
    iduser = database.Column(database.Integer, primary_key=True, nullable=False)
    username = database.Column(database.String(30))
    role = database.Column(database.String(3), nullable=False, default='sup')
    senha = database.Column(database.Integer, nullable=False)

class Filhos(database.Model):
    matricula = database.Column(database.Integer, primary_key=True, nullable=False)
    nome = database.Column(database.String(60))
    nascimento = database.Column(database.Date, nullable=False)
    inicio = database.Column(database.Date)
    status = database.Column(database.String(8), nullable=False, default='ativo')
    hierarquia = database.Column(database.String(15), default='sem faixa')
    orixa1 = database.Column(database.String(8))
    orixa2 = database.Column(database.String(8))
    orixa3 = database.Column(database.String(8))
    telefone = database.Column(database.Integer)
    email = database.Column(database.String(60))
    rg = database.Column(database.Integer)
    cpf = database.Column(database.Integer, nullable=False)
    rua = database.Column(database.String(50))
    ncasa = database.Column(database.Integer)
    complemento = database.Column(database.String(10))
    bairro = database.Column(database.String(12))
    cidade = database.Column(database.String(10))
    uf = database.Column(database.String(2))
    idresp = database.Column(database.Integer, database.ForeignKey('responsavel.idresp'))
    img_filho = database.Column(database.String, default='padrao.jpg')
    mensalidade = database.relationship('Financeiro', backref='filhos', lazy=True)
    idgira = database.relationship('Gira', backref='filhos', lazy=True)
    iddeitagem = database.relationship('Deitagem', backref='filhos', lazy=True)
    idevfaixa = database.relationship('EvFaixa', backref='filhos', lazy=True)

class Financeiro(database.Model):
    idmensalidade = database.Column(database.Integer, primary_key=True)
    data = database.Column(database.Date)
    valor = database.Column(database.Numeric(5,2))
    status = database.Column(database.String(8), nullable=False, default='pendente')
    idfilho = database.Column(database.Integer, database.ForeignKey('filhos.matricula'), nullable=False)

class Assistencia(database.Model):
    idasistgira = database.Column(database.Integer, primary_key=True)
    data = database.Column(database.Date, nullable=False)
    qnt = database.Column(database.Integer, nullable=False)
    idgira = database.relationship('Gira', backref='assistencia', lazy=True)

class EvFaixa(database.Model):
    idevfaixa = database.Column(database.Integer, primary_key=True)
    ano = database.Column(database.Date, nullable=False)
    faixa = database.Column(database.String(15))
    idfilho = database.Column(database.Integer, database.ForeignKey('filhos.matricula'), nullable=False)

class Linha(database.Model):
    idlinha = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(16))
    idgira = database.relationship('Gira', backref='linha', lazy=True)

class Gira(database.Model):
    idgira = database.Column(database.Integer, primary_key=True)
    data = database.Column(database.Date, nullable=False)
    linha_id = database.Column(database.Integer, database.ForeignKey('linha.idlinha'), nullable=False)
    idfilho = database.Column(database.Integer, database.ForeignKey('filhos.matricula'), nullable=False)
    idassistencia = database.Column(database.Integer, database.ForeignKey('assistencia.idasistgira'), nullable=False)

class Orixa(database.Model):
    idorixa = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(16))
    iddeitagem = database.relationship('Deitagem', backref='orixa', lazy=True)

class Deitagem(database.Model):
    iddeitagem = database.Column(database.Integer, primary_key=True)
    ano = database.Column(database.Date, nullable=False)
    copol = database.Column(database.Text)
    orixaid = database.Column(database.Integer, database.ForeignKey('orixa.idorixa'), nullable=False)
    idfilho = database.Column(database.Integer, database.ForeignKey('filhos.matricula'), nullable=False)

class Responsavel(database.Model):
    idresp = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(60))
    telefone = database.Column(database.Integer)
    filhoid = database.relationship('Filhos', backref='responsavel', lazy=True)
