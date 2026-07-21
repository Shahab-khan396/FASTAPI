from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

base = declarative_base()

class Student(base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    # FIX: Change 'fee' to 'Fee' to match the class name
    fees = relationship('Fee', back_populates='student')

class Fee(base):
    __tablename__ = 'fees'
    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    student_id = Column(Integer, ForeignKey('student.id'))
    # FIX: Change 'student' to 'Student' to match the class name
    student = relationship('Student', back_populates='fees')

engine = create_engine('sqlite:///school.db', echo=True)
base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Rest of your code...
students = [
    Student(name='John Doe', age=20),
    Student(name='Jane Smith', age=22),
    Student(name='Bob Brown', age=25),
    Student(name='Alice Jones', age=23)
]

fees = [
    Fee(amount=5000),
    Fee(amount=6000),
    Fee(amount=4500),
    Fee(amount=5500)
]

for i in range(len(students)):
    students[i].fees.append(fees[i])
    session.add(students[i])

session.commit()

# Query
from sqlalchemy.orm import joinedload
students_list = session.query(Student).options(joinedload(Student.fees)).all()

for student in students_list:
    print(f'{student.name} ({student.age}):')
    for fee in student.fees:
        print(f'- {fee.amount}')   
        
        

# Query students and fees using a join
from sqlalchemy.orm import aliased

student=aliased(Student)
fee=aliased(Fee)
stmt= session.query(student,fee).join(fee,student.id==fee.student_id).order_by(student.name ).all()

for s, f in stmt:
    print(f'{s.name} ({s.age}): {f.amount}')