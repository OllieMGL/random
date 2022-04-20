
user_input = input("What range do you want?: ")

for i in range(int(user_input)):
    if i%3 == 0 and i%5 == 0:
        print("Fizz buzz")
    elif i%5 == 0:
        print("Buzz")
    elif i%3 == 0:
        print("Fizz")
    else:
        print(i)
    
    
