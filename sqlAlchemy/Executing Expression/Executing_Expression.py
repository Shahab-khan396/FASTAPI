# import necessary packages
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Numeric, insert, Integer, VARCHAR, update, text, delete, select   
from sqlalchemy.engine import result

# establish connections
engine = create_engine('sqlite:///book.db', echo=True)
# initialize the Metadata Object
meta = MetaData()
meta.reflect(engine)

# create a table schema
books = Table(
    'books', meta,
    Column('book_id', Integer, primary_key=True),
    Column('book_price', Numeric),
    Column('genre', VARCHAR),
    Column('book_name', VARCHAR),
    extend_existing=True
)

meta.create_all(engine)
# insert records into the table
# Create tables if they don't exist
meta.create_all(engine)

# Prepare Data
statements = [
    books.insert().values(book_name='Think and grow Rich', book_price=200, genre='non-fiction'),
    books.insert().values(book_name='Atomic habit', book_price=220, genre=']fiction'),
    books.insert().values(book_name='Rich dad and poor dad', book_price=250, genre='non-fiction'),
    books.insert().values(book_name='The psychology of money', book_price=300, genre='sci-fi')
]

# Execute Inserts WITH Commit
with engine.begin() as conn: # ✅ Use engine.begin() to auto-commit
    for stmt in statements:
        conn.execute(stmt)

        
