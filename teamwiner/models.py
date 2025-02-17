from teamwiner import db
from datetime import datetime

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False)
    foto_perfil = db.Column(db.String(20), nullable=False, default='default.jpg')
    posts = db.relationship('post', backref='autor', lazy=True)
    cursos = db.Column(db.String, default='Não informado', nullable=False)

    # def __repr__(self):
    #     return f'<Usuario {self.nome}>'
    

class post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    corpo = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    # def __repr__(self):
    #     return f'<Post {self.titulo}>'
