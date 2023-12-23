import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_smorest import Api




app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql://book_inventory_api_user:kDtYxkAwQOAn1t6F3fXLGZNqq5Rk0YCc@dpg-cm2it6ta73kc73eij540-a.singapore-postgres.render.com/book_inventory_api"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class BooksModel(db.Model):
    __tablename__ = 'book'

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
	return {"book": "API"}

# POST method : Add new book
# GET  method : Return all books in the table
@app.route('/books', methods=['POST', 'GET'])
def handle_books():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_book = BooksModel(isbn=data['isbn'],title=data['title'], author=data['author'], year_published=data['year_published'],genre=data['genre'])

            db.session.add(new_book)
            db.session.commit()

            return {"message": f"book {new_book.title} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        books = BooksModel.query.all()
        results = [
            {
                "isbn": book.isbn,
                "title": book.title,
                "author": book.author,
                "year_published": book.year_published,
                "genre": book.genre
            } for book in books]

        return {"count": len(results), "books": results, "message": "success"}

#GET method : return a specific book
#PUT method : update a specific book
#DELETE method : delete a specific book
@app.route('/books/<book_isbn>', methods=['GET', 'PUT', 'DELETE'])
def handle_book(book_isbn):
    book = BooksModel.query.get_or_404(book_isbn)

    if request.method == 'GET':
        response = {
            "isbn": book.isbn,
            "title": book.title,
            "author": book.author,
            "year_published": book.year_published,
            "genre": book.genre
        }
        return {"message": "success", "book": response}

    elif request.method == 'PUT':
        data = request.get_json()
        book.isbn = data['isbn']
        book.title = data['title']
        book.author = data['author']
        book.year_published = data['year_published']
        book.genre = data['genre']

        db.session.add(book)
        db.session.commit()
        
        return {"message": f"Book {book.title} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(book)
        db.session.commit()
        
        return {"message": f"Book {book.title} successfully deleted."}

if __name__ == '__main__':
    app.run(debug=True)