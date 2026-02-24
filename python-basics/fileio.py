#Name : William Karanja
# Date : 23/02/2026
# Program to perform file operation in python

# create new file
new_file = open("student_data.txt","r+")

#write new file
new_file.write(" {Student name : William Kabebe , ID:22136659 , email:willsmassiveload67@gmail.com }")
new_file.close()
# Read from the new file
new_file = open("student_data.txt","r+")

data = new_file.read()

print(data)

new_file.close()


# Delete file
# us os module
import os
os.remove("remove.txt")

# delete a folder
os.rmdir("folder")
