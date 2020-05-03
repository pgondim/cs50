from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)


class Books(db.Model):
    __tablename__ = "books"
    isbn = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.String, nullable=False)
    comentarios = db.relationship("Comentarios", backref="coment", lazy=True)

    def add_comentario(self, comentario, user_id):
        c = Comentarios(comentario=comentario, user_id = user_id, livro_isbn=self.isbn)
        db.session.add(c)
        db.session.commit()


class Comentarios(db.Model):
    __tablename__ = "comentarios"
    id = db.Column(db.Integer, primary_key=True)
    comentario = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    livro_isbn = db.Column(db.String, db.ForeignKey("books.isbn"), nullable=False)
