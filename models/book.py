from db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class BooksModel(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer(), primary_key=True)
    isbn = db.Column(db.String() ,unique=True, nullable=True)
    title = db.Column(db.String(),nullable=False)
    author = db.Column(db.String(), nullable=False)
    year_published = db.Column(db.Integer(), nullable=True)
    genre = db.Column(db.String(), nullable=True)
    student_id = db.Column(UUID(as_uuid=True), db.ForeignKey("student.student_id"),default=None, unique=False,nullable=True)
    student = db.relationship("StudentsModel", back_populates="book")
    

    def __init__(self, isbn, title, author,year_published,genre):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year_published = year_published
        self.genre = genre

    def __repr__(self):
        return f"<Book {self.title}>"