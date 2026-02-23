#Name : William Karanja
# Date : 23/02/2026
# Program to show iheritance in python

class Animal():
    def __init__(self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self,weight):
        weight = 1.1 * weight
        print(f"T he animals weight {weight} in kgs")

    def eat(self,food):
        print("The animal eats {food}")




class Dog(Animal):
    def __init__(self,colour,height,breed):
        super().__init__(species,weight,food)
        self.colour = colour
        self.height = height
        self.breed = breed


    def barks(self):
        print("The animal barks woof woof")


class Horse(Animal):
    def __init__(self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food

    
    def neigs(self):
        print("The animal neighs")