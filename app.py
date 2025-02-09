from flask import Flask , render_template, url_for
from forms import FormCriarConta, FormLogin

app = Flask(__name__)

lista_usuarios = ['Maycon','João','Beatriz','José', 'Italo','Marina','Rosimar','Ourivan','Amanda','Lucas','Rafael']

app.config['SECRET_KEY'] = 'ee23664e6e55f0d81d5f553ee19afe09'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')  

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login')
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    return render_template('login.html', formLogin=form_login, formCriarConta=form_criarconta)

 

if __name__ == '__main__':
    app.run(debug=True)
