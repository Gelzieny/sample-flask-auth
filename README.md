<strong><h1 align="center"> API de autenticação </h1></strong>


### Pré-requisitos

<p align="justify">Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:</p>

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=git,vscode,python,postman" />
</a>

### Clone o repositório

````bash
# Clone este repositório
$ git clone <https://github.com/Gelzieny/gerenciamento-tarefas.git>

# Acesse a pasta do projeto no terminal/cmd
$ cd gerenciamento-tarefas
````

### Configuração do Ambiente

````bash
# Crie e ative um ambiente virtual e Instale as dependências
# No Windows
$ python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt

# No Linux/Mac 
$ python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

# Criar todas as tabelas do banco de dados definidas nos modelos
$ db.create_all()

# Adiciona o novo usuário à sessão
$ db.session

# Confirma todas as mudanças feitas na sessão no banco de dados
$ db.session.commit()
````

#### Caso o corra um erro ao criar um banco executar os comandos a seguir

### Adicionar o caminho de src ao PYTHONPATH
````bash
# Windows (CMD):

$ set PYTHONPATH=src
$ set FLASK_APP=src.app
$ flask shell

# Windows (Powershell):
$ $env:PYTHONPATH = "src"
$ $env:FLASK_APP = "src.app"
$ flask shell


# Linux/Mac:
$ export PYTHONPATH=src
$ export FLASK_APP=src.app
$ flask shell
````