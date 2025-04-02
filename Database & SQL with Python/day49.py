# Day 49: NoSQL Databases (MongoDB with PyMongo)  

'''
In this day, we will learn about NoSQL databases and their different types, such as MongoDB with PyMongo.
'''

# NoSQL Databases

''''
NoSQL databases are non-relational databases that store data in a format that is different from the way it is stored in a relational database.
'''

# MongoDB with PyMongo

''''
MongoDB is a popular NoSQL database that is used for storing data in a document format. PyMongo is a library for working with MongoDB in Python.
'''

# Example

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create a database
db = client["mydatabase"]

# Create a collection
collection = db["mycollection"]

# Insert data into the collection
data = {"name": "John", "age": 30}
collection.insert_one(data)

# Read data from the collection
cursor = collection.find()
for document in cursor:
    print(document)

# Update data in the collection
collection.update_one({"name": "John"}, {"$set": {"age": 31}})

# Delete data from the collection
collection.delete_one({"name": "John"})
print("Data deleted successfully.")
# Close the connection
client.close()