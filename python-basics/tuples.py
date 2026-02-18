#Name : William Karanja
# Date : 18/02/2026
# Program to show tuples in python
# tuples of fruits

fruits = ("Avocado","Kiwi","Apples","Mango","Banana","Orange")

print(len(fruits))
print(fruits[0])
print(fruits[4])
print(fruits[-6])

# error ->fruits.append("Guava")

fruits_list = list(fruits)

fruits_list.append("Guava")
print(fruits_list)