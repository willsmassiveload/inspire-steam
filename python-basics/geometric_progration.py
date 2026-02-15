#Name : William Karanja
# Date : 13/02/2026
# Program to calculate geometric progration

#Calculating nth term

a = int (input("Enter the firts term :"))
r = int (input("Enter the common ratio :"))
n = int (input("Enter the number of terms :"))

Tn = a * (r**(n-1))
sum_gp = a*(r**n-1)
print("Geometric Progression")
print("Sum of GP",sum_gp)