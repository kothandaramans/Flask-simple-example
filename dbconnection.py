from sqlalchemy import create_engine
import os

db_name = 'book_authors.db'
prefix = 'sqlite:///'
BASE_DIR = prefix + os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, db_name)

def connect():
    db_connect = create_engine(db_path)
    return db_connect.connect()
    