import sys
import os

# Adiciona o diretório 'src' ao caminho de importação
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from flask import Flask, request, jsonify
from database import db  # Certifique-se de que o caminho de importação está correto
from models.user import User  # Certifique-se de que o caminho de importação está correto
from flask_login import LoginManager, login_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash  # Para verificar e gerar senhas criptografadas

# Criação da aplicação Flask
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
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

@app.route('/login', methods=["POST"])
def login():
  data = request.json

  username = data.get("username")
  password = data.get("password")

  if username and password:
    user = User.query.filter_by(username=username).first()
    if not user:
      return jsonify({"message": "Usuário não encontrado"}), 404

    if check_password_hash(user.password, password): 
      login_user(user)  
      return jsonify({"message": "Autenticação realizada com sucesso!"})
    else:
      print("Senha incorreta")  

  return jsonify({"message": "Credenciais inválidas"}), 400

@app.route('/register', methods=["POST"])
def register():
  data = request.json
  print(f"Dados recebidos para cadastro: {data}") 

  username = data.get("username")
  password = data.get("password")

  if username and password:
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
      return jsonify({"message": "Usuário já existe!"}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuário criado com sucesso!"}), 201

  return jsonify({"message": "Dados inválidos"}), 400

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run(debug=True)
