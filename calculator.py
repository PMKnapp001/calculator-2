"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    user_tokens = (input("Enter your arithmetic expression: ")).split(" ")

    if user_tokens[0] == "q":
        quit()

    elif user_tokens[0]== "+": 
        num1 =float(user_tokens[1])
        num2 =float(user_tokens[2])
        print(add(num1,num2))

    elif user_tokens[0] == "-":
        num1 = float(user_tokens[1])
        num2 = float(user_tokens[2])
        print(subtract(num1, num2))

    elif user_tokens[0] == "*":
        num1 = float(user_tokens[1])
        num2 = float(user_tokens[2])
        print(multiply(num1, num2))

    elif user_tokens[0] == "/":
        num1 = float(user_tokens[1])
        num2 = float(user_tokens[2])
        print(divide(num1,num2))

    elif user_tokens[0] == "square":
        num1 = float(user_tokens[1])
        print(square(num1))

    elif user_tokens[0] == "cube":
        num1 = float(user_tokens[1])
        print(cube(num1))
    
    elif user_tokens[0] == "power":
        num1 = float(user_tokens[1])
        num2 = float(user_tokens[2])
        print(power(num1,num2))
        
    elif user_tokens[0] == "mod":
        num1 = float(user_tokens[1])
        num2 = float(user_tokens[2])
        print(mod(num1,num2))