import sys
import os

# Adiciona o diretório 'src' ao caminho de importação
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from flask_login import UserMixin
from database import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(80), nullable=False, default='user')

    def __repr__(self):
        return f'<User {self.username}>'

    def check_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, password)