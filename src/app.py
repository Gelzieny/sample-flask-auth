import sys
import os

# Adiciona o diretório 'src' ao caminho de importação
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from flask import Flask, request, jsonify
from database import db  # Certifique-se de que o caminho de importação está correto
from models.user import User  # Certifique-se de que o caminho de importação está correto
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash  # Para verificar e gerar senhas criptografadas
from sqlalchemy.exc import SQLAlchemyError

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


@app.route('/list-user', methods=["GET"])
@login_required  
def get_user():
  users = User.query.all()

  if not users:
    return jsonify({"message": "Nenhum usuário encontrado"}), 404

  users_data = []
  for user in users:
    users_data.append({
      "id": user.id,
      "username": user.username
    })

  return jsonify(users_data), 200

@app.route('/update-user', methods=["PUT"])
@login_required
def update_user():
  data = request.json

  if "username" in data:
    current_user.username = data["username"]

  if "password" in data:
    current_user.password = generate_password_hash(data["password"]) 

  db.session.commit()

  return jsonify({"message": "Dados atualizados com sucesso!"}), 200

@app.route('/logout', methods=["GET"])
@login_required 
def logout():
  if not current_user.is_authenticated:
    return jsonify({"message": "Você precisa estar autenticado para fazer logout."}), 401
  
  logout_user()
  return jsonify({"message": "Desconectado com sucesso!"}), 200

@app.route('/delete-user/<int:user_id>', methods=["DELETE"])
@login_required
def delete_user(user_id):

  if user_id == current_user.id:
    return jsonify({"message": "Você não pode excluir sua própria conta!"}), 400

  user = User.query.get(user_id)
  
  if not user:
    return jsonify({"message": "Usuário não encontrado"}), 404

  try:
    db.session.delete(user) 
    db.session.commit() 
    return jsonify({"message": "Usuário deletado com sucesso!"}), 200
  except SQLAlchemyError as e:
    db.session.rollback() 
    return jsonify({"message": f"Erro ao deletar o usuário: {str(e)}"}), 500

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run(debug=True)
