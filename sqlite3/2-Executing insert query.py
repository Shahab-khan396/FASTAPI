        
# ----------------------------------------------------------
                    # Example 2: Executing insert query
# --------------------------------------------------------------
from sqlalchemy import text,create_engine


engine = create_engine('sqlite:///users.db', echo=True)

# 1. Define data as a LIST of dictionaries (not a tuple)
data = [
    { "book_id": 6, "book_price": 400, "genre": "fiction", "book_name": "yoga is science" },
    { "book_id": 7, "book_price": 800, "genre": "non-fiction", "book_name": "alchemy tutorials" },
]

# 2. Write the insert statement with named parameters (:book_id, etc.)
statement = text("""
    INSERT INTO books (book_id, book_price, genre, book_name) 
    VALUES (:book_id, :book_price, :genre, :book_name)
""")

# 3. Execute within the connection context
with engine.begin() as conn:  # engine.begin() auto-commits
    # Option A: Bulk insert (Recommended) - Pass the whole list at once
    conn.execute(statement, data)
    
    # Option B: Loop (If you specifically need to loop)
    # for line in data:
    #     conn.execute(statement, line)  # Pass dict directly, NO **

    # 4. Select query MUST be inside the 'with' block
    select_sql = text('SELECT * FROM books')
    result = conn.execute(select_sql)
    
    print("\n--- All Records ---")
    for record in result:
        print(record)   