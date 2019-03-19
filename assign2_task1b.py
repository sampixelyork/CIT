## Sam York
## CIT229975

## Assignment 2: Task 1b - count number of words in a file

import re

#load a text file
text_file = open("example_text.txt")
text_data = text_file.read()

#split data into a word list at either a space or newline or carriage return
result = re.split(r"[\s\r\n]+", text_data)

#print the length of word list
print(len(result))

