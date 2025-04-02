# Day 45: Introduction to Databases (SQLite, MySQL, PostgreSQL) 

'''
In this day, we will learn about databases and their different types, such as SQLite, MySQL, and PostgreSQL.
'''

# Databases

''''
A database is a collection of structured data that is organized and accessed in a way that allows for efficient storage, retrieval, and manipulation of data.
'''

# SQLite

''''
SQLite is a popular and lightweight database that is used for small to medium-sized applications.
'''

# MySQL

'''''
MySQL is a popular open-source relational database management system.
'''

# PostgreSQL

''''
PostgreSQL is a popular open-source relational database management system.
'''


# SQlite Example

import sqlite3

# Connect to the database
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()



# MySQL Example

# import mysql.connector

# # Connect to the database
# conn = mysql.connector.connect(
#     host="localhost",
#     user="username",
#     password="password",
#     database="mydatabase"
# )

# # Create a cursor object
# cursor = conn.cursor()

# # Create a table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTO_INCREMENT,
#         name TEXT NOT NULL,
#         email TEXT NOT NULL UNIQUE,
#         password TEXT NOT NULL
#     )
# ''')    

# # Commit the changes
# conn.commit()

# # Close the connection
# conn.close()


# PostgreSQL Example

# import psycopg2

# # Connect to the database
# conn = psycopg2.connect(
#     host="localhost",
#     database="mydatabase",
#     user="username",
#     password="password"
# )

# # Create a cursor object
# cursor = conn.cursor()

# # Create a table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id SERIAL PRIMARY KEY,
#         name TEXT NOT NULL,
#         email TEXT NOT NULL UNIQUE,
#         password TEXT NOT NULL
#     )
# ''')

# # Commit the changes
# conn.commit()

# # Close the connection
# conn.close()
