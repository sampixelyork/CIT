## Sam York
## CIT229975

## Assignment 2: Task 2 - add a string to a file

#open or create a file to append
text_file = open("example_text.txt", "a+")

#ask the user for a sentence
user_string = str(input("Type something to add to a file: "))

#write users input to the opened text file preceeded by a new line
text_file.write("\n")
text_file.write(user_string)
text_file.close()


