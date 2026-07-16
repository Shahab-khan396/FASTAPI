from sqlalchemy import text, create_engine, MetaData

engine = create_engine('sqlite:///users.db', echo=True)

# 1. Reflect metadata and get the table
meta = MetaData()
meta.reflect(engine)
books = meta.tables['books']

# 2. Create the update statement
# Fix: Use 'non-fiction' (with hyphen) to match your data
stmt = books.update().where(books.c.genre == 'non-fiction').values(genre='sci-fi')

# 3. Execute within a connection context AND commit
with engine.begin() as conn:  # engine.begin() auto-commits on success
    result = conn.execute(stmt)
    print(f"Rows updated: {result.rowcount}")

    # 4. Verify the update
    select_sql = text('SELECT * FROM books')
    result = conn.execute(select_sql)
    
    print("\n--- Updated Records ---")
    for record in result:
        print(record)   