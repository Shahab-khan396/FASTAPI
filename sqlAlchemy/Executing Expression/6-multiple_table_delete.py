# Import necessary packages
from sqlalchemy import create_engine, MetaData, Table, Column, Numeric, Integer, String, text,delete

# Create the database engine
engine = create_engine('sqlite:///book.db', echo=True)

# Create a MetaData object
meta = MetaData()

# Reflect existing tables (optional if you are creating them below)
# meta.reflect(bind=engine) 

# Define table schemas
books = Table(
    'books', meta,
    Column('book_id', Integer, primary_key=True),
    Column('book_price', Numeric),
    Column('genre', String),
    Column('book_name', String)
)

book_publisher = Table(
    'book_publisher', meta,
    Column('publisher_id', Integer, primary_key=True),
    Column('publisher_name', String),
    Column('publisher_estd', Integer),
)

# Create all tables
meta.create_all(engine)

# Prepare Data for Books
book_statements = [
    {"book_name": "Think and grow Rich", "book_price": 200, "genre": "non-fiction"},
    {"book_name": "Atomic habit", "book_price": 220, "genre": "fiction"},  # Fixed typo: ']fiction' -> 'fiction'
    {"book_name": "Rich dad and poor dad", "book_price": 250, "genre": "non-fiction"},
    {"book_name": "The psychology of money", "book_price": 300, "genre": "sci-fi"}
]

# Prepare Data for Publishers (Bulk Insert List)
publisher_data = [
    {"publisher_id": 1, "publisher_name": "Oxford", "publisher_estd": 1900},
    {"publisher_id": 2, "publisher_name": "Stanford", "publisher_estd": 1910},
    {"publisher_id": 3, "publisher_name": "MIT", "publisher_estd": 1920},
    {"publisher_id": 4, "publisher_name": "Springer", "publisher_estd": 1930},
    {"publisher_id": 5, "publisher_name": "Packt", "publisher_estd": 1940},
]

# Execute everything in a single transaction
with engine.begin() as conn:
    # 1. Insert Books
    conn.execute(books.insert(), book_statements)
    
    # 2. Insert Publishers (Single Bulk Statement)
    conn.execute(book_publisher.insert(), publisher_data)
    
    # 3. Query and Print Results
    query = text('SELECT * FROM books')
    result = conn.execute(query)
    
    print("\n--- Books Table ---")
    for record in result:
        print(record)

    # Query Publishers to verify
    pub_query = text('SELECT * FROM book_publisher')
    pub_result = conn.execute(pub_query)
    
    print("\n--- Publishers Table ---")
    for record in pub_result:
        print(record)   
        
    print("\n--- before delete Table ---")   
    from sqlalchemy import select

    delete_stmt = delete(books).where(
    books.c.book_id.in_(
        select(book_publisher.c.publisher_id).where(
            book_publisher.c.publisher_name == "Oxford"
        )
    )
)


    conn.execute(delete_stmt)
    print("\n--- After Deletion ---")
    result = conn.execute(query)
    for record in result:
        print(record)