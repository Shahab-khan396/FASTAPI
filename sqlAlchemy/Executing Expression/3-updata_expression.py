from sqlalchemy import create_engine, MetaData, select,text,update
# Create the engine
engine = create_engine('sqlite:///book.db', echo=True)

metadata = MetaData()
metadata.reflect(bind=engine)  # ✅ Correct usage

# Access the 'books' table
Books = metadata.tables['books']

u=update(Books)
u=u.values({'book_name':'Think and grow Rich'})
u=u.where(Books.c.book_id==3)
with engine.begin() as conn:
    conn.execute(u)
    sql = text('select * from Books')
    result=conn.execute(sql).fetchall()
    
    for record in result:
        print('\n', record)



# --------------------------------------------------
# Example 2
# ----------------------------------------------------

stmt=Books.update().where(Books.c.genre== 'non-fiction').values(genre = 'Ajeeba')

with engine.begin() as conn:
    result=conn.execute(stmt)
    query=text('select * from Books')
    result=conn.execute(query).fetchall()
    for records in result:
        print('\n',records)

