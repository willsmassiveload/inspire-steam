#Name : William Karanja
# Date : 16/02/2026
# Program to calculate income tax

salary = int(input("Enter your gross salary:"))



if salary < 50000:
    tax_rate = 2.5
elif salary <= 100000:
    tax_rate = 4.5
else:
    tax_rate = 7.5
tax = (tax_rate * salary) / 100
net_salary = salary - tax
print(f"Gross salary = {salary}")
print(f"Tax Rate Applied = {tax_rate}%") 
print (f"Tax = {tax}")
print(f"Net salary = {net_salary}")
