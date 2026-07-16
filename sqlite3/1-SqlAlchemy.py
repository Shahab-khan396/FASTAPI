# '''

# basic Of SQLite3 with SQLAlchemy

# '''


# import sqlalchemy as db

# # Defining the Engine
# engine = db.create_engine('sqlite:///users.db', echo=True)

# # Create the Metadata Object
# metadata_obj = db.MetaData()

# # Define the profile table

# # database name
# profile = db.Table(
#     'profile',                                        
#     metadata_obj,                                    
#     db.Column('email', db.String, primary_key=True),  
#     db.Column('name', db.String),                    
#     db.Column('contact', db.Integer),                
# )

# # Create the profile table
# metadata_obj.create_all(engine)


# -------------------------------------------------------------
                # SQLAlchemy Core - SQL Expressions
# -------------------------------------------------------------

# Creating table for demonstration

from sqlalchemy import create_engine, MetaData, Table, Column, Numeric, Integer, VARCHAR

# 1. Establish connection
engine = create_engine('sqlite:///users.db', echo=True)

# 2. Initialize Metadata (Corrected Instance Call)
meta = MetaData()
# Note: If 'books' table already exists in the DB, this reflects it. 
# If not, this does nothing until create_all is called.
meta.reflect(engine) 

# 3. Define Table Schema
# If the table was reflected above, this variable points to the reflected table.
# If not, it creates a new definition.

if 'books' not in meta.tables:
    books = Table(
            'books',
            meta,
            Column('book_id', Integer, primary_key=True),
            Column('book_name', VARCHAR), # Removed accidental space in column name
            Column('book_price', Numeric),
            Column('genre', VARCHAR),
            
        )

# Create table if it doesn't exist
meta.create_all(engine)

# 4. Prepare Data (Fixed Duplicate ID)
statements = [
    books.insert().values(book_id=1, book_name='Think and grow Rich', book_price=200, genre='non-fiction'),
    books.insert().values(book_id=2, book_name='Atomic habit', book_price=220, genre='non-fiction'),
    books.insert().values(book_id=3, book_name='Rich dad and poor dad', book_price=250, genre='non-fiction'),
    books.insert().values(book_id=4, book_name='The psychology of money', book_price=300, genre='non-fiction') # Changed ID to 4
]

# 5. Execute within Connection Context (SQLAlchemy 2.0 Standard)
with engine.begin() as conn:
    for stmt in statements:
        conn.execute(stmt)   
        
        
from sqlalchemy import text
from sqlalchemy import create_engine
text('Your SQL quaries')

# ---------------------------------------------------
            # Example 1:  Executing basic query
# ----------------------------------------------------

from sqlalchemy import text


engine = create_engine('sqlite:///users.db', echo=True)

with engine.connect() as connection:
    result = connection.execute(text("select * from books where books.book_price > 230"))
    for row in result:
        print("Output:", row)
          
    
