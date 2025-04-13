'''
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

'''

file_name = 'sample.txt'

try:
    file1 = open(file_name, 'r')
    reading_file = file1.read()
    print(reading_file)
    file1.close()
except FileNotFoundError:
    print("Error: The file {} was not found.".format(file_name))