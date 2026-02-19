#Name : William Karanja
# Date : 19/02/2026
# Program to run same instructions


def cook_egg():
    oil = "20ml"
    pan = True
    moto = True
    eggs = 2

    print(f"The pan is {pan}, and the fire is {moto},\ add {oil} amount of oil and cook {eggs} eggs")


cook_egg()

print("Here is statement 1")

print("Here is statement 2")

cook_egg()

print("Here is statement 3")

# Ride fare creating function

def create_fare(route,distance,is_rush_hour):
    fare = distance * 10
    if is_rush_hour == True:
        fare = fare * 1.5
    print(f"Your fare to {route} is {fare}")

    return fare
   
rush_hour = True
returned_fare = create_fare("Juja-Allsops",7,rush_hour)
print(f"The fare returned is: {returned_fare}")  

# Passing a list as a parameter
def write_all_interests(interests):
    for interest in interests:
        print(f"I am interested in {interest}")

all_interests = ("Hiking","Eating","Watching Anime")

write_all_interests(all_interests)       