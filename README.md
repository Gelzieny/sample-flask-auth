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
- **Docker**: Contêinerização para facilitar a execução do projeto em qualquer ambiente.


### Pré-requisitos

<p align="justify">Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:</p>

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=git,vscode,python,postman,docker" />
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

# Rodar o docker-compose
$ docker-compose up -d
````

### Executar projeto

````bash
# Para roda o projeto
$ python src/app.py
````


### Como usar:

1. Substitua o `usuario` e `repo-flask-auth` pelo nome correto de seu repositório.
2. Caso o seu projeto tenha algum arquivo `requirements.txt`, adicione a listagem de pacotes que o seu projeto usa, como `Flask`, `Flask-Login`, `SQLAlchemy`, etc.
3. O **README.md** descreve a instalação, uso das rotas da API, e a estrutura do diretório para facilitar o entendimento do seu projeto.

### Passos para rodar com Docker:

1. Certifique-se de que o Docker está instalado e em funcionamento na sua máquina.
2. Execute `docker-compose up --build` para construir e iniciar os contêineres.
3. A aplicação estará acessível em `http://127.0.0.1:5000/`.