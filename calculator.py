"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# repeat forever:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             (...etc.)


while True:
    user_input = input("Enter your equation: ")
    
    token = user_input.split(" ")
    if token[0] == 'q':
        print("Quit")
        break
    
    elif token[0] == "+":
        print(add(float(token[1]), float(token[2])))
    elif token[0] == "-":
        print(subtract(float(token[1]), float(token[2])))
    elif token[0] == "*":
        print(multiply(float(token[1]), float(token[2])))
    elif token[0] == "/":
        print(divide(float(token[1]), float(token[2])))
    elif token[0] == "square":
        print(square(float(token[1])))
    elif token[0] == "cube":
        print(cube(float(token[1])))
    elif token[0] == "pow":
        print(power(float(token[1]), float(token[2]))) 
    elif token[0] == "mod":
        print(mod(float(token[1]), float(token[2])))
