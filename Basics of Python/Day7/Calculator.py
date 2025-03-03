# Day 7: Practice Mini-Projects (Calculator, Simple Interest Calculator)


# Calculator
print("Calculator")


num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

operator = input("Enter the operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    result = num1 / num2

else:
    print("Invalid operator")

print("Result:", result)

