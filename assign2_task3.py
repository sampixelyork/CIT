## Sam York
## CIT229975

## Assignment 2: Task 3 - print all numbers in a text file

import re

#load a text file
text_file = open("example_text.txt")
text_data = text_file.read()

#split data into a number list at any non-digit
result = re.split(r"\D+", text_data)

#remove first and last list entry if blank
if result[0] == "":
    del result[0]
    
if result[-1] == "":
    del result[-1]

#print the number list
print(result)



