import sys 
import math 
import time
import random
num1 = 0
num2 = 0

def abilitieslist():
    print("The calculator can currently...")
    print("- +...Addition")
    print("- -...Subtraction")
    print("- *...Multiplication")
    print("- /...Division")
    print("- /-...Square Roots ")
    print("^...Powers")
    print("- randint...Returns A Random Number Between The Two Inputs -> randint 1 10")
    print("- rand...Returns A Random Number Between 0 and 1")
    print("- x fah... Converts fahreneit to celsius ")
    print("- x cel...Converts celsius to fahreneit")
    print("\n- note that you will have to leave a space inbetween each integer/word")
    input("////////////////////////////////////////////////////////////////////////////////////////")


retry = "y"
user_input = input("Do you want to see what the calculator can currently do? (y/n): ")
if user_input == "y":
    abilitieslist()
    
while retry == "y":
    print("\nPlease enter your equation in this format 1 + 1")
    equation = str(input(">>> "))
    num_array = equation.strip().split(" ")
    
    if num_array[0] == "help":
        abilitieslist()
        
    elif num_array[0] == "rand":
        output = [0, 1]
        answer = random.choice(output)
        print(">>> " + str(equation) + " = " + str(answer)+ "")    


    elif num_array[1] == "+":
        num1 = int(num_array[0])
        num2 = int(num_array[2])
        answer = num1 + num2
        print(">>> " + str(equation) + " = " + str(answer)+ "")

    elif num_array[1] == "-":
        num1 = int(num_array[0])
        num2 = int(num_array[2])
        answer = num1 - num2
        print(">>> " + str(equation) + " = " + str(answer)+ "")

    elif num_array[1] == "/":
        num1 = int(num_array[0])
        num2 = int(num_array[2])
        answer = float(num1) / float(num2)
        print(">>> " + str(equation) + " = " + str(answer)+ "")

    elif num_array[1] == "*":
        num1 = int(num_array[0])
        num2 = int(num_array[2])
        answer = num1 * num2
        print(">>> " + str(equation) + " = " + str(answer)+ "")
        
    elif num_array[0] == "/-":
        num1 = int(num_array[1])     
        answer = math.sqrt(num1)
        print(">>> The square root of " + str(num1) + " = " + str(answer)+ "")
        
    elif num_array[0] == "randint":
        num1 = int(num_array[1])
        num2 = int(num_array[2])
        output = list(range(num1, num2))
        answer = random.choice(output)
        print(">>> " + str(equation) + " = " + str(answer)+ "")
        
    elif num_array[1] == "fah":
        num1 = int(num_array[0])
        answer = (num1 - 32) * 5/9
        print("" + str(num1) + " fahrenheit in celsius is " + str(answer) + "°C")
        
    elif num_array[1] == "cel":
        num1 = int(num_array[0])
        answer = (num1 * 1.8) + 32
        print("" + str(num1) + "°C in fahrenheit is " + str(answer) + "°F")
        
    elif num_array[1] == "^":
        num1 = int(num_array[0])
        num2 = int(num_array[2])
        answer = num1 ** num2
        print(">>> " + str(equation) + " = " + str(answer)+ "")
        
        
    
        
        
        
        
        
    else:
        print("That is not a valid equation")
        
    retry = input("\nWould you like to submit another equation? (y/n): ") 
    if retry == "n":
        sys.exit()
    
        