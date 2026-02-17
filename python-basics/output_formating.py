#Name : William Karanja
# Date : 17/02/2026
# Program to format the output in different styles

name = "William Karanja"

weight = 60 # weight in kgs

fav_team = "Liverpool"

height = 172.72 #heiht in cms

# 1. Format using printf (f"{}")

print(f"My name is {name} and I weigh {weight} kgs.")

# Using f string
msg = f"My name is {name} and I support {fav_team}"
print(msg)

#3 using {} and . format()

print("My name {0} and I am {1} cms tall".format(name,height))

# using output specifies %s -strings %f -float

import math
print("The value of pi is approximately")
print("I support %s" %fav_team)