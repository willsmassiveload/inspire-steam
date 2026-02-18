#Name : William Karanja
# Date : 18/02/2026
# Program to show lists in python
# List of friends
friends = ["Rachel","Pheobe","Rose","Chandler","Monica","Joy"]

print(friends)
friends.sort()
print(friends)

friends.reverse()
print(friends)
friends.append("Jack")
print(friends)
 
new_friends = ["William","Kehlani","Nate"]

print(len(new_friends))

# New list of students
students = friends + new_friends
print(students)

students.pop()
print(students)

students.insert(5,"Makayla")
print(students)

students.insert(9,"Vallary")
print(students)

students.extend("Josh")
print(students)

students.remove("Monica")
print(students)

new_students = students.copy()
print(new_students)