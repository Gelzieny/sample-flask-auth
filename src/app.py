import os
from flask import Flask, request, jsonify
from database import db  # Importando o db de src/database.py
from models.user import User  # Importando o modelo de User
from flask_login import LoginManager, login_user, current_user
from werkzeug.security import check_password_hash  # Usado para verificar senhas criptografadas

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
# View de login
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

@app.route('/login', methods=["POST"])
def login():
  data = request.json
  print(f"Dados recebidos: {data}") 

  username = data.get("username")
  password = data.get("password")

  if username and password:
    user = User.query.filter_by(username=username).first()
    if not user:
      print("Usuário não encontrado") 
      return jsonify({"message": "Usuário não encontrado"}), 404

    print(f"Usuário encontrado: {user.username}") 
    print("User", user.password, 'T', password)

    # Verificando a senha
    if check_password_hash(user.password, password):  
      print("Senha correta")  
      login_user(user)  
      return jsonify({"message": "Autenticação realizada com sucesso!"})
    else:
      print("Senha incorreta")  
  return jsonify({"message": "Credenciais inválidas"}), 400


if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run(debug=True)
