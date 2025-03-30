# Day 39: Using the requests module 

'''
In this day, we will learn about using the requests module in Python. The requests module is a popular library for making HTTP requests in Python.'
'''

# Using the requests module

''''
The requests module is a popular library for making HTTP requests in Python. It allows you to send HTTP requests to a server and get back a response.'
'''

# Example

import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
