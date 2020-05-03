import os

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models import *

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sucessocad", methods = ["post"])
def sucessocad():
    nome  = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha")
    user = Users(nome = nome, email = email, senha = senha)
    db.session.add(user)
    db.session.commit()
    return render_template("sucessocad.html", msg = "Usuário cadastrado com sucesso!!")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/livro", methods = ["POST"])
def status():
    email = request.form.get("loginEmail")
    senha = request.form.get("loginSenha")
    user = Users.query.filter_by(email = email).first()
    if (user == None):
        return render_template("login.html", msg = "E-mail não existe")
    if (user.senha != senha):
        return render_template("login.html", msg = "E-mail ou senha errado, tente novamente")

    #return render_template("status.html", msg = f"Bem-vindo {user.nome.title()}", user_id=user.id)  
    return render_template("buscar.html",user_id = user.id)

@app.route("/livro/<int:user_id>", methods = ["POST"])
def livro(user_id):
    tipoBusca = request.form.get("tipoBusca")
    busca = request.form.get("busca")
    if (tipoBusca =="tituloBusca"):
        livros = Books.query.filter_by(title=busca).all()
    if (tipoBusca == "isbnBusca"):
        livros = Books.query.filter_by(isbn=busca).all()
    if (tipoBusca == "autorBusca"):
        livros = Books.query.filter_by(author=busca).all()
    if (tipoBusca == "anoBusca"):
        livros = Books.query.filter_by(year=busca).all()
    return render_template("livros.html",user_id = user_id,livros=livros)

@app.route("/livro/<int:user_id>/<string:livro_isbn>")
def descricao(user_id,livro_isbn):
    livro = Books.query.filter_by(isbn=livro_isbn).first()
    comentarios = livro.comentarios
    return render_template("descricao.html",user_id = user_id, livro=livro, comentarios=comentarios)


@app.route("/livro/<int:user_id>/<string:livro_isbn>", methods = ["POST"])
def add_comentario(user_id,livro_isbn):
    comentario  = request.form.get("comentario")
    livro = Books.query.filter_by(isbn=livro_isbn).first()
    livro.add_comentario(comentario, user_id)
    comentarios = livro.comentarios
    return render_template("descricao.html",user_id = user_id,livro=livro, comentarios=comentarios)


