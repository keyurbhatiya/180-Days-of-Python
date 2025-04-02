# Day 46: CRUD Operations with SQLite 

# In this day, we will learn about creating, reading, updating, and deleting data in a SQLite database.

# CRUD Operations

'''
Create (C): Adding new data to the database.'
'
Read (R): Retrieving data from the database.'
'
Update (U): Modifying existing data in the database.'

Delete (D): Removing data from the database.''
'''

# SQLite Example

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
print("Database created successfully.")
# Close the connection
conn.close()

# Insert data into the database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO users (name, email, password)
    VALUES (?, ?, ?)
''', ('John Doe', 'V1oB1@example.com', 'password123'))

conn.commit()
print("Data inserted successfully.")

# Read data from the database
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row)

print("Data read successfully.")

# Update data in the database
cursor.execute('''
    UPDATE users
    SET password = ?
    WHERE email = ?
''', ('newpassword123', 'V1oB1@example.com'))

conn.commit()

print("Data updated successfully.")

# Delete data from the database
cursor.execute('''
    DELETE FROM users
    WHERE email = ?
''', ('V1oB1@example.com',))

print("Data deleted successfully.")
conn.commit()

# Close the connection
conn.close()

# show all data in the database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

for row in rows:
    print(row)

print("Data read successfully.")
conn.close()