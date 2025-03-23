# Day 36: Async Programming with asyncio 

'''
In this day, we will learn about asynchronous programming using asyncio in Python. Asyncio is a library that allows you to write asynchronous code in Python.
''' 

# Async Programming

''''
Async programming is a way to write code that can execute concurrently, which means that multiple tasks can be executed at the same time.
'''

# Example

import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(main())
