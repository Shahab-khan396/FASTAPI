from sqlalchemy import *

engine = create_engine("sqlite:///library.db", echo=True)

metadata = MetaData()

student = Table(
    "student",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("age", Integer),
    Column("dept", String),
)

metadata.create_all(engine)

with engine.begin() as conn:

    conn.execute(text("DELETE FROM student"))

    conn.execute(text("""
        INSERT INTO student(id,name,age,dept)
        VALUES
        (1,'Mitul Rao',20,'Comp'),
        (2,'Lochan Patel',17,'Comp'),
        (3,'Inderjeet Ahmad',17,'Mech'),
        (4,'Punita Gadhavi',25,'Civil'),
        (5,'Sarvesh Mishra',30,'Comp')
    """))

    print("\nStudents:\n")

    result = conn.execute(select(student))

    for row in result:
        print(row)

    print("\nUppercase Names:\n")

    query = select(
        label("name_uppercase", func.upper(student.c.name)),
        student.c.age
    ).where(student.c.age > 18)

    for row in conn.execute(query):
        print(row)

    print("\nDepartment Count:\n")

    query = select(
        label("student_count", func.count(student.c.dept)),
        student.c.dept
    ).group_by(student.c.dept)

    for row in conn.execute(query):
        print(row)