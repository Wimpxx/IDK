operator = input("What operator do you want to use [+|-|*|/]: ")

num1 = int(input("What is the first number you want to use: "))
num2 = int(input("What is the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Choose from the avalaible operators!")

print(f"Your result is {result}")
