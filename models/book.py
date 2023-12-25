from db import db

class BooksModel(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer(), primary_key=True)
    isbn = db.Column(db.String() ,unique=True, nullable=True)
    title = db.Column(db.String(),nullable=False)
    author = db.Column(db.String(), nullable=False)
    year_published = db.Column(db.Integer(), nullable=True)
    genre = db.Column(db.String(), nullable=True)
    

    def __init__(self, isbn, title, author,year_published,genre):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year_published = year_published
        self.genre = genre

    def __repr__(self):
        return f"<Book {self.title}>"