#Name : William Karanja
# Date : 23/02/2026
# Program to show classes in python

class Car():
    #attributes 0f the car
    def __init__(self,model,make,year,color):
     self.model = model
     self.make = make
     self.color = color
     self.year = year

    #print car details
    def print_details(self,model,make,color,year):
       print(f" {make} {model} of color {color} was manufactured in the year {year}")


#instantiate a class object

my_Car = Car("M5","BMW","Dark Blue","2021")
dads_Car = Car("Q3","Audi","White","2022")

my_Car.print_details("M5","BMW","Dark Blue","2021")
dads_Car.print_details("Q3","Audi","White","2022")