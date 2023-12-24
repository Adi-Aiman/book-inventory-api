import os

from flask import Flask, request, redirect, make_response 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_smorest import abort
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from sqlalchemy.exc import SQLAlchemyError



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql://book_inventory_api_user:kDtYxkAwQOAn1t6F3fXLGZNqq5Rk0YCc@dpg-cm2it6ta73kc73eij540-a.singapore-postgres.render.com/book_inventory_api"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
#app.config["API_TITLE"] = "Book Inventory REST API"
#app.config["API_VERSION"] = "v1"
#app.config["OPENAPI_VERSION"] = "3.0.3"
#app.config["OPENAPI_URL_PREFIX"] = "/"
#app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
#app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
#api = Api(app)

SWAGGER_URL = '/help'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/openapi.json'  # Our API url (can of course be a local resource)


swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Book Inventory API"
    }    
)

app.register_blueprint(swaggerui_blueprint)

db = SQLAlchemy(app)
migrate = Migrate(app, db) 


class BooksModel(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer(), primary_key=True)
    isbn = db.Column(db.String() ,unique=True, nullable=True)
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
	return redirect("/help")#{"book": "API"}



# POST method : Add new book
# GET  method : Return all books in the table
@app.route('/books', methods=['POST', 'GET'])
def handle_books():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_book = BooksModel( isbn=data['isbn'],title=data['title'], author=data['author'], year_published=data['year_published'],genre=data['genre'])

            try:
                db.session.add(new_book)
                db.session.commit()
            except SQLAlchemyError:
                return abort(make_response({'message':'An Error Occured While Inserting The Book'},500))

            return make_response({"message": f"book {new_book.title} has been added successfully."},201)
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
@app.route('/books/<book_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_book(book_id):
    book = BooksModel.query.get_or_404(book_id)

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
        try:
            db.session.add(book)
            db.session.commit()
        except SQLAlchemyError:
                return abort(make_response({'message':'An Error Occured While Updating The Book'},500))
        
        return make_response({"message": f"Book {book.title} successfully updated"},200)

    elif request.method == 'DELETE':
        try:
            db.session.delete(book)
            db.session.commit()
        except SQLAlchemyError:
                return abort(make_response({'message':'An Error Occured While Deleting The Book'},500))
        
        return {"message": f"Book {book.title} successfully deleted."}

if __name__ == '__main__':
    app.run(debug=True)