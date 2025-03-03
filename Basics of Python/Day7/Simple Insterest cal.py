# Day 7: Practice Mini-Projects (Calculator, Simple Interest Calculator)


# Simple Interest Calculator

print("Simple Interest Calculator")

principal = float(input("Enter the principal amount: "))

rate = float(input("Enter the rate of interest: "))

time = float(input("Enter the time period in years: "))

simple_interest = (principal * rate * time) / 100

total_amount = principal + simple_interest

print("Total Amount:", total_amount)
print("Simple Interest:", simple_interest)

