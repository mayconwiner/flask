# Flask

Flask é um framework de aplicação web leve [WSGI]. Ele é projetado
para tornar o início rápido e fácil, com capacidade de expansão para
aplicações complexas. Começou como um wrapper simples em torno de [Werkzeug]
e [Jinja], e se tornou um dos mais populares Python web
estruturas de aplicação.

O Flask oferece sugestões, mas não impõe nenhuma dependência ou
layout do projeto. Cabe ao desenvolvedor escolher as ferramentas e
bibliotecas que desejam usar. Existem muitas extensões fornecidas pelo
comunidade que facilita a adição de novas funcionalidades.

[WSGI]: https://wsgi.readthedocs.io/
[Werkzeug]: https://werkzeug.palletsprojects.com/
[Jinja]: https://jinja.palletsprojects.com/

## Um exemplo simples 

```python 
# salve isso como app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
```

```
$ flask run
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Atenção

Este é um exemplo do basico de flask para fins de estudo, podendo ser alterado conforme necessario, para instalação das bibliotecas utilize o arquivo 
requiriments.txt
