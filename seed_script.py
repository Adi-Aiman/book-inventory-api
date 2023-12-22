import pandas as pd
from sqlalchemy import create_engine


csv_file_path = "books.csv"
engine = create_engine("postgresql://book_inventory_api_user:kDtYxkAwQOAn1t6F3fXLGZNqq5Rk0YCc@dpg-cm2it6ta73kc73eij540-a.singapore-postgres.render.com/book_inventory_api")
with open(csv_file_path, 'r') as file:
    data_df = pd.read_csv(file, header=0)
data_df.to_sql(name='books', con=engine, index=False,  if_exists='replace')

