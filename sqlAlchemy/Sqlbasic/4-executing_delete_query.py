from sqlalchemy import create_engine, MetaData, text

engine = create_engine('sqlite:///users.db', echo=True)
meta = MetaData()
meta.reflect(engine)
books = meta.tables['books']

# 1. Start the connection context
with engine.begin() as conn:
    # --- DELETE Operation ---
    delete_stmt = books.delete().where(books.c.book_price > 300)
    result = conn.execute(delete_stmt)
    print(f"Rows deleted: {result.rowcount}")

    # --- SELECT Operation (MUST be inside the 'with' block) ---
    sql = text('SELECT * FROM books')
    result = conn.execute(sql)
    
    print("\n--- Remaining Records ---")
    for record in result:
        print(record)

# 2. Connection is automatically closed here. 
# You cannot run conn.execute() after this point.   