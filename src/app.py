import os
from flask import Flask, request, jsonify
from database import db  # Importando o db de src/database.py
from models.user import User  # Importando o modelo de User
from flask_login import LoginManager

app = Flask(__name__)

# Caminho para o diretório onde o banco de dados será criado (diretório 'instance')
instance_path = os.path.join(os.getcwd(), 'instance')

# Garantir que o diretório exista
if not os.path.exists(instance_path):
  os.makedirs(instance_path)

# Configurações do Flask
app.config['SECRET_KEY'] = "your_secret_key"
# Usando caminho relativo para o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(instance_path, "database.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
# Inicializando a extensão db
db.init_app(app)
login_manager.init_app(app)

@app.route('/login', methods=["POST"])
def login():
  data = request.json
  username = data.get("username")
  password = data.get("password")

  if username and password:
    # Login
    user = User.query.filter_by(username=username).first()  # Correção aqui

    if user and user.password == password:
      return jsonify({"message": "Autenticação realizada com sucesso!"})

  return jsonify({"message": "Credenciais inválidas"}), 400


# Criando as tabelas no banco de dados, se ainda não existirem
if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run(debug=True)
