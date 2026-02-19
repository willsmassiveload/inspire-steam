#Name : William Karanja
# Date : 19/02/2026
# Program to show objects in python

class Human:
    #Fisrt we define the attributes of Human beings
    type = "Mammal"
    legs = 2 
    brain = True
    warm_blooded = True
    city = "Nairobi"

    # We then create a constructor for the class_object
    # The constructor will be used to create copies of this object
    def __init__(self,name,age):
        self.name = name
        self.human_age = age

    def tell_story(self):
        print(f"Hello,I am {self.name} Here is a story")
        print("There was once an old witch in the forest she was believe to eat children and youths who went woundering in the forest but the holy knight slayed the witch",self.name)    

# Create the humans
william = Human("William",20)
nate = Human("Nate",19)

# Let the humans created do things
william.tell_story()
print("William's age is:",william.human_age)
 
# Modify one of the objects , without modifying other objects
print("Nate's location:", nate.city)
print("William's location:", william.city)

nate.city = "Kiambu"

