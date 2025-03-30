# Day 38: Introduction to APIs (REST, SOAP) 

'''
In this day, we will learn about APIs (Application Programming Interfaces) and their different types, such as REST (Representational State Transfer) and SOAP (Simple Object Access Protocol).
'''

# APIs

''''
An API (Application Programming Interface) is a set of rules and protocols that allow different software components to communicate with each other.
'''

# REST (Representational State Transfer)

''''
REST (Representational State Transfer) is a architectural style for building web services that use HTTP requests to transfer data between clients and servers.
'''

# SOAP (Simple Object Access Protocol)

''''
SOAP (Simple Object Access Protocol) is a protocol for exchanging structured data between applications.
'''

# Example


import requests

url = "https://api.example.com/data"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
    
