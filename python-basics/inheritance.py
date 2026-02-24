# student.py

class Student:
    def __init__(self, student_id, name, course, phone):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.phone = phone
        self.grade = None

    def assign_course_grade(self, new_course, grade):
        self.course = new_course
        self.grade = grade

    def display(self):
        return [self.student_id, self.name, self.course, self.phone, self.grade]

class Animal():
    def __init__(self, species, weight, food):
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self):
        self.weight = 1.1 * self.weight
        print(f"The animal's weight is now {self.weight} kgs")

    def eat(self):
        print(f"The animal eats {self.food}")


class Dog(Animal):
    def __init__(self,species, weight, food, colour, height, breed):
        super().__init__(species, weight, food)
        self.colour = colour
        self.height = height
        self.breed = breed

    def barks(self):
        print("The dog barks woof woof")


class Horse(Animal):
    def __init__(self, species, weight, food):
        super().__init__(species, weight, food)

    def neighs(self):
        print("The horse neighs")