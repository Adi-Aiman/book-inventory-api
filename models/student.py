from db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class StudentsModel(db.Model):
    __tablename__ = 'student'

    student_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String() ,unique=False, nullable=True)
    membership_start = db.Column(db.Date(),nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False )
    book = db.relationship("BooksModel", back_populates="student", lazy="dynamic")

    def __init__(self, name, membership_start,email):
        
        self.name = name
        self.membership_start = membership_start
        self.email = email
        

    def __repr__(self):
        return f"<Student {self.name}>"