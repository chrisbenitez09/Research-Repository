num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % 2 == 0 or num1 % 3 == 0:
    print(num1 * num2)
else:
    print(num1 + num2)