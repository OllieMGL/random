one_piece = {"episodes" : 1013,
             "rating" : 10/10,
             "best character" : "luffy", 
            "Who should watch it?": "Harry"}

user_input = input("What would you like to look for?: ")
if user_input in one_piece:
    print("It is in the list")
    
else:
    print("not found")