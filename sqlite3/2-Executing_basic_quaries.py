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
        
        
        
