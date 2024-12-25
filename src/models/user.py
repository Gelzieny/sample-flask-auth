import sys
import os

# Adiciona o diretório 'src' ao caminho de importação
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from flask_login import UserMixin
from database import db  # Importando o db corretamente

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # ID do usuário, chave primária
    username = db.Column(db.String(80), nullable=False, unique=True)  # Nome de usuário
    password = db.Column(db.String(120), nullable=False)  # Senha criptografada

    def __repr__(self):
        return f'<User {self.username}>'

    # Método para verificar se a senha fornecida é válida
    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)