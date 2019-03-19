## Sam York
## CIT229975

## Assignment 2: Task 1a - count number of lines in a file

import re

#load a text file
text_file = open("example_text.txt")
text_data = text_file.read()

#variable for counting lines
line_count = 1

#checking all data for a newline
for i in text_data:
    if i == "\n":
        #increase counting lines by 1 for every 
        line_count += 1

#print the number of lines
print(line_count)
