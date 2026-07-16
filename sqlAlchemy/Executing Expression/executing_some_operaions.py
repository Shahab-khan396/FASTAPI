import sqlalchemy as db
from sqlalchemy import create_engine, MetaData, select,text

# Create the engine
engine = create_engine('sqlite:///book.db', echo=True)

# Reflect metadata from the database
meta = MetaData()
meta.reflect(bind=engine)  # ✅ Correct usage

# Access the 'books' table
Books = meta.tables['books']



# select All from books
# Build the query using SQLAlchemy 2.x style
query = select(Books)

# Execute the query
with engine.begin() as conn:
    result = conn.execute(query).fetchall()

# Print results
for record in result:
    print('\n', record)   
        




# Build the query using SQLAlchemy 2.x style
query = select(Books).where(Books.c.genre == 'non-fiction')

# Execute the query
with engine.begin() as conn:
    result = conn.execute(query).fetchall()

# Print results
for record in result:
    print('\n', record)   
        



# Build the query using SQLAlchemy 2.x text
sql = text('SELECT * from BOOKS WHERE BOOKS.book_price > 230')


# Execute the query
with engine.begin() as conn:
    result = conn.execute(sql).fetchall()

# Print results
for record in result:
    print('\n', record)   
        