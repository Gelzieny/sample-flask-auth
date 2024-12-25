<strong><h1 align="center"> API de autenticação </h1></strong>

<p align="justify">
Este projeto é uma API de autenticação simples desenvolvida com Flask. A API permite funcionalidades como login, registro, visualização e atualização de usuários, além de logout e exclusão de contas. Ele utiliza o Flask, Flask-Login, e SQLAlchemy para interação com o banco de dados SQLite.
</p>

## Funcionalidades

- **Cadastro de usuário**: Permite que novos usuários se registrem na aplicação.
- **Login**: Permite que um usuário se autentique.
- **Logout**: Permite que um usuário faça logout de sua conta.
- **Listagem de usuários**: Retorna todos os usuários registrados.
- **Atualização de dados do usuário**: Permite que o usuário logado altere seus dados.
- **Exclusão de conta**: Permite que um usuário exclua sua conta, mas não pode excluir sua própria conta.

## Tecnologias

- **Flask**: Micro-framework web para Python.
- **Flask-Login**: Gerenciamento de sessões de login.
- **SQLAlchemy**: ORM (Object Relational Mapper) para interação com o banco de dados.
- **Werkzeug**: Biblioteca para manipulação de senhas (hashing).


### Pré-requisitos

<p align="justify">Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:</p>

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=git,vscode,python,postman" />
</a>

### Clone o repositório

````bash
# Clone este repositório
$ git clone <https://github.com/Gelzieny/sample-flask-auth.git>

# Acesse a pasta do projeto no terminal/cmd
$ cd sample-flask-auth

````

### Configuração do Ambiente

````bash
# Crie e ative um ambiente virtual e Instale as dependências
# No Windows
$ python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt

# No Linux/Mac 
$ python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

````

### Executar projeto

````bash
# Para roda o projeto
$ python src/app.py
````