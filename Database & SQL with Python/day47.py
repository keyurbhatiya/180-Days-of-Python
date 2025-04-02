# Day 47: Working with MySQL & SQLAlchemy  

'''
In this day, we will learn about working with MySQL and SQLAlchemy in Python. SQLAlchemy is a popular library for working with databases in Python.
'''

# Working with MySQL and SQLAlchemy

''''
MySQL is a popular open-source relational database management system. SQLAlchemy is a library for working with databases in Python.
'''

# Example

import mysql.connector
from sqlalchemy import create_engine

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

# Create a SQLAlchemy engine
engine = create_engine("mysql+mysqlconnector://username:password@localhost/mydatabase")

# Close the connection
conn.close()

# show all data in the database
import mysql.connector
from sqlalchemy import create_engine

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
)

# Create a SQLAlchemy engine
engine = create_engine("mysql+mysqlconnector://username:password@localhost/mydatabase")

# Read data from the database
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

print("Data read successfully.")

# Close the connection
conn.close()