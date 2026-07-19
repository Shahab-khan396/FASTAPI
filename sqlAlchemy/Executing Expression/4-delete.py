from sqlalchemy import create_engine, MetaData, select,text,update
# Create the engine
engine = create_engine('sqlite:///book.db', echo=True)

metadata = MetaData()
metadata.reflect(bind=engine)  # ✅ Correct usage

# Access the 'books' table
Books = metadata.tables['books']

delete=Books.delete().where(Books.c.genre=='Ajeeba')


with engine.begin() as conn:
    conn.execute(delete)
    sql = text('select * from Books')
    result=conn.execute(sql).fetchall()
    
    for record in result:
        print('\n', record)