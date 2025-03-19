# Day 28: Practice Project (Log File Analyzer)

# In this day, we will create a log file analyzer that reads a log file and performs various operations on it.


# Example

import re

def analyze_log_file(log_file):
    with open(log_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if re.search(r'ERROR', line):
                print(line.rstrip())
            elif re.search(r'WARNING', line):
                print(line.rstrip())
            elif re.search(r'INFO', line):
                print(line.rstrip())
            else:
                print(line.rstrip())

analyze_log_file('log.txt')


# Summary

'''
In this day, we learned how to read a log file and perform various operations on it. We used regular expressions to match different types of log messages.
'''
