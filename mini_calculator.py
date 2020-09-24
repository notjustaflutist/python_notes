num1 = float(input("Enter first number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter second number: "))

if op == "+" or op == "add":
    print(num1 + num2)
elif op == "-" or op == "subtract":
    print(num1 - num2)
elif op == "/" or op == "divide":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("undefined")
elif op == "*" or op == "multiply":
    print(num1 * num2)
else:
    print("Invalid operator")