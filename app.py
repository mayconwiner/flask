from flask import Flask , render_template, url_for, request, redirect, flash
from forms import FormCriarConta, FormLogin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

lista_usuarios = ['Maycon','João','Beatriz','José', 'Italo','Marina','Rosimar','Ourivan','Amanda','Lucas','Rafael']

app.config['SECRET_KEY'] = 'ee23664e6e55f0d81d5f553ee19afe09'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dti.db'

db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')  

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))
    
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)

 
if __name__ == '__main__':
    app.run(debug=True)



