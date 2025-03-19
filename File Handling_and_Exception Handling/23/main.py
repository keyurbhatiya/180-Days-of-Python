# Day 23: Working with CSV and JSON Files


# CSV (Comma-Separated Values) Files

''''
CSV (Comma-Separated Values) files are text files that store data in a tabular format, where each row represents a record and each column represents a field.

'''

# JSON (JavaScript Object Notation) Files

''''
JSON (JavaScript Object Notation) files are text files that store data in a human-readable format. They are often used to exchange data between different programming languages and platforms.
'''

# Working with CSV and JSON Files

'''
In this day, we will learn how to work with CSV and JSON files in Python.

'''
# Example


import csv
import json

'''
CSV Files functions
reader(): This function is used to read data from a CSV file. It returns a reader object that can be used to iterate over the rows of the file.
writer(): This function is used to write data to a CSV file. It returns a writer object that can be used to write rows to the file.

'''
# Working with CSV files
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


'''
json files functions
load(): This function is used to read data from a JSON file. It returns a Python object that represents the data in the file.
dump(): This function is used to write data to a JSON file. It takes a Python object as an argument and writes it to the file in JSON format.

'''

# Working with JSON files
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)

with open('data.json', 'w') as file:
    data = {'name': 'Keyur', 'age': 21}
    json.dump(data, file)


# Summary

'''
In this day, we learned how to work with CSV and JSON files in Python. We used the csv and json modules to read and write data in these file formats.
'''