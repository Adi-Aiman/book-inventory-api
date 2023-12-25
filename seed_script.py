import os
from sqlalchemy import create_engine, Insert,inspect
from dotenv import load_dotenv
import csv
from models.book import BooksModel
load_dotenv()

csv_file_path = "books.csv"
engine = create_engine(os.getenv("DATABASE_URL"))

class Seeder():

    
    def seed_initial_values():
        print("Seeding the initial values into the Database")
        with open('books.csv', 'r', encoding="utf-8") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            next(csv_reader, None)  # skip the headers
            with engine.connect() as conn:
                for x in csv_reader:
                    result = conn.execute(Insert(BooksModel).values(isbn=x[0],title=x[1],author=x[2],year_published=x[3],genre=x[4]))
                
                conn.commit()

    def validate_table():
        if(inspect(engine).has_table("book")):
            print("Table Does Exist")
            return True
        else:
            print("Table Does NOT Exist")
            return False




    

