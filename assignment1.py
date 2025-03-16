print("Enter first number: ")
num1 = input()
print("Enter operator: ")
op = input()
print("Enter second number: ")
num2 = input()

if op== "+":
    print("The sum is: ", int(num1) + int(num2))
elif op == "-":
    print("The difference is: ", int(num1) - int(num2))
elif op == "*":
    print("The product is: ", int(num1) * int(num2))
elif op == "/":
    print("The quotient is: ", int(num1) / int(num2))
else:
    print("Invalid operator")