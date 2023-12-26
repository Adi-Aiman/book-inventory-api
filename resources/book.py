from flask import  request, make_response
from flask_smorest import  Blueprint,abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError
import json
import traceback
from models.book import BooksModel , db



book_B= Blueprint("book", __name__ ,description="book Operations")

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
            try:
                 data = json.loads(request.data, strict=False)
            except SQLAlchemyError:
                 return make_response({"error": "There are issue with the json content","code":415},415)
            try:
                 new_book = BooksModel( isbn=data['isbn'],title=data['title'], author=data['author'], year_published=data['year_published'],genre=data['genre'])
            except SQLAlchemyError:
                 return make_response({"error": "There are issue with the json content, check the keys","code":422},422)
            try:
                db.session.add(new_book)    ### should check the the content to make sure keys and values are valid.
                db.session.commit()
            except SQLAlchemyError:
                return abort(make_response({'message':f'An Error Occured While Inserting The Book {traceback.print_exc()} '},500))

            return make_response({"message": f"book {new_book.title} has been added successfully."},201)
        else:
            return make_response({"error": "The request payload is not in JSON format"},415)
        
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

@book_B.route('/books/borrow')
class BOOK_BORROW(MethodView):
    def get(self):
        books = BooksModel.query.all()
        borrowers=[]
        for x in books:
                if(x.student_id != None):
                    borrowers.append(x)
        results = [
            {   
                "isbn": borrower.isbn,
                "title": borrower.title,
                "author": borrower.author,
                "year_published": borrower.year_published,
                "genre": borrower.genre,
                "Student Name": borrower.student.name
            } for borrower in borrowers ]
        return {"count": len(results), "borrowers": results, "message": "success"}

@book_B.route('/books/borrow/<book_id>')
class BOOK_BORROW_ADD(MethodView):    
    def put(self,book_id):
        book = BooksModel.query.get_or_404(book_id)
        data = request.get_json()
        book.student_id = data['student_id']
        try:
            db.session.add(book)
            db.session.commit()
        except SQLAlchemyError:
                return abort(make_response({'message':'An Error Occured While Updating Borrowed Status'},500))
        return make_response({"message": f"Book {book.title} borrow status has been updated"},200)

          