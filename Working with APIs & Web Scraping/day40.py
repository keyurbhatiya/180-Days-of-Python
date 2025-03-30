# Day 40: Working with BeautifulSoup  

'''
In this day, we will learn about working with BeautifulSoup in Python. BeautifulSoup is a library for parsing HTML and XML documents.
'''

# Working with BeautifulSoup

''''
BeautifulSoup is a library for parsing HTML and XML documents. It allows you to navigate and extract data from the document.
'''

# Example

from bs4 import BeautifulSoup

html = "<html><body><h1>Hello, world!</h1></body></html>"

soup = BeautifulSoup(html, "html.parser")

print(soup.h1)

# Output
# <h1>Hello, world!</h1>