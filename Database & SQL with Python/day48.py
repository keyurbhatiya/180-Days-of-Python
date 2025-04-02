# Day 48: ORM Concepts (SQLAlchemy & Django ORM) 

'''
In this day, we will learn about Object-Relational Mapping (ORM) concepts in Python. ORM is a way to map Python objects to database tables and vice versa.
'''

# ORM Concepts

''''
Object-Relational Mapping (ORM) is a way to map Python objects to database tables and vice versa.
'''

# Example

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey,sessionmaker

# Create a SQLAlchemy engine
engine = create_engine("sqlite:///mydatabase.db")

# Create a base class for declarative models
Base = declarative_base()

# Define a model class
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    def __repr__(self): 
        return f"User(id={self.id}, name={self.name}, email={self.email}, password={self.password})"

# Create the database tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()