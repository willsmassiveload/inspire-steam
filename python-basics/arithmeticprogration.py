#Name : William Karanja
# Date : 13/02/2026
# Program to calculate arithmetic progration

# Calculating nth term

a = int (input("Enter the firts number :"))
n = int (input("Enter the number of terms :"))
d = int (input("Enter the common differenc :"))

nth_term = a + (n-1) * d
Sn = (n/2) * (2 * a + (n-1) * d)
print(f"The nth term is : {nth_term}")
print(f"The sum of the numbers is : {Sn}")

