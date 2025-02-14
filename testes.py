from app import app, db
from models import Usuario, Post

# with app.app_context():
#     db.create_all()
# with app.app_context():
#     usuario = Usuario(
#         username='Maycon', email='mayconwiner@gmail.com', senha='123456')

#     db.session.add(usuario)
#     db.session.commit()
# get usuarios
with app.app_context():
    usuarios = Usuario.query.all()
    print(usuarios)
