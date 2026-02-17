#Name : William Karanja
# Date : 16/02/2026
# Program to display diamond and triangle

rows = 5

for i in range(rows):
    print(" " * (rows - i -1) + "*" *(2 * i - 1))

rows = 5 # You can change this number

# Upper part
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))

# Lower part
for i in range(rows - 2, -1, -1):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))

# Program to solve a quadratic equation
import math

# input values
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

# calculate discriminant
D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Two real roots:")
    print("x1 =", x1)
    print("x2 =", x2)

elif D == 0:
    x = -b / (2*a)
    print("One real root:")
    print("x =", x)

else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-D) / (2*a)
    print("Two complex roots:")
    print("x1 =", real_part, "+", imaginary_part, "i")
    print("x2 =", real_part, "-", imaginary_part, "i")


    

    







