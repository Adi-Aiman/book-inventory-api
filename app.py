import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql://book_inventory_api_user:kDtYxkAwQOAn1t6F3fXLGZNqq5Rk0YCc@dpg-cm2it6ta73kc73eij540-a.singapore-postgres.render.com/book_inventory_api"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class BooksModel(db.Model):
    __tablename__ = 'books'

    isbn = db.Column(db.String(), primary_key=True)
    title = db.Column(db.String())
    author = db.Column(db.String())
    year_published = db.Column(db.Integer())
    genre = db.Column(db.String())
    

    def __init__(self, isbn, title, author,year_published,genre):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year_published = year_published
        self.genre = genre

    def __repr__(self):
        return f"<Book {self.title}>"


@app.route('/')
def hello():
	return {"hello": "world"}

if __name__ == '__main__':
    app.run(debug=True)