#Name : William Karanja
# Date : 13/02/2026
# Program to show forloop
import math

for x in range(0,360,30):
    print(math.cos(x))
    print(math.sin(x))
    print(math.tan(x))

    
for i in range(10,0,-1):
    print(i)

for angle in range(-180,181,30):
    radians = math.radians(angle)
sin_value = math.sin(radians)
print("sin(",angle,") =",round(sin_value,4))


for angle in range(-180,180,30):
    radians = math.radians(angle)
    cos_value = math.cos(radians)
    print("cos(",angle,") = ",round(cos_value,4))

for angle in range(-180,180,30):
    radians = math.radians(angle)
    tan_value = math.tan(radians)
    print("tan(",angle,") = ",round(tan_value,4))


for angle in range(-180,180,30):
    radians = math.radians(angle)
    print("Angle",angle)
    print("sin =",round(math.sin(radians),4))
    print("cos =",round(math.sin(radians),4))
    print("tan =",round(math.sin(radians),4))
    print()   


       
  


    
    

    


