
user_input = input("What range do you want?: ")

for i in range(int(user_input)):
    if i%3 == 0 and i%5 == 0:
        print("Fizz buzz,", end=" ")
    elif i%5 == 0:
        print("Buzz,", end=" ")
    elif i%3 == 0:
        print("Fizz,", end=" ")
    else:
        print(f"{i},", end=" ")
    
    