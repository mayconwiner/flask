from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, length

class FormCriarConta(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), length(8,120), EqualTo('confirmar_senha', message='As senhas devem ser iguais')])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), length(8,120), EqualTo('senha', message='As senhas devem ser iguais')])
    botao_submit_criarconta = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), length(8,120)])
    botao_submit_login = SubmitField('Entrar')
    
