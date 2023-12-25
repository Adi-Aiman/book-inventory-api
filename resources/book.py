from flask import  request, make_response
from flask_smorest import  Blueprint,abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from models.book import BooksModel , db



book_B= Blueprint("user", __name__ ,description="book Operations")

# POST method : Add new book
# GET  method : Return all books in the table
@book_B.route('/books')
class BOOK(MethodView):
    def get(self):
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
    
    def post(self):
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
        
#GET method : return a specific book
#PUT method : update a specific book
#DELETE method : delete a specific book
@book_B.route('/books/<string:book_id>')
class BOOK_ID(MethodView):
    def get(self,book_id):
        book = BooksModel.query.get_or_404(book_id)
        response = {
            "isbn": book.isbn,
            "title": book.title,
            "author": book.author,
            "year_published": book.year_published,
            "genre": book.genre
        }
        return {"message": "success", "book": response}
    def put(self,book_id):
        book = BooksModel.query.get_or_404(book_id)
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
    def delete(self,book_id):
        book = BooksModel.query.get_or_404(book_id)
        try:
            db.session.delete(book)
            db.session.commit()
        except SQLAlchemyError:
                return abort(make_response({'message':'An Error Occured While Deleting The Book'},500))
        
        return {"message": f"Book {book.title} successfully deleted."}
    
@book_B.route('/books/test/<test>')
class BOOK_TEST(MethodView):
    def get(self,test):
         return make_response({"message":test},200)