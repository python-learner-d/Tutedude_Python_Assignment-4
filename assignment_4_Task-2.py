'''
Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

'''

file_name  = 'output.txt'
file = open(file_name, 'w')

content1 = input("Enter text to write to the file: ")

writing_file = file.write(content1)
file.close()
print("Data successfully written to {}\n".format(file_name))

file = open(file_name, 'a')

content2 = input("Enter additional text to append: ")

appending_file  = file.writelines(["\n",content2])
file.close()
print("Data successfully appended.\n")

file = open(file_name, 'r')

reading_file = file.read()
print("Final content of {}".format(file_name))
print(reading_file)
file.close()