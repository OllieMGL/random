import time
import random
import sys

def time321():
    time.sleep(0.25)
    print("3...", end= ' ', flush=True)
    time.sleep(0.5)
    print("2...", end= ' ', flush=True)
    time.sleep(0.5) 
    print("1...",  end= ' ', flush=True)
    time.sleep(0.5)

    
def askForRetry():
    valid_input = False
    retry = False
    showing_stakes = False
    while valid_input == False:
        retry_input = input("Would you like to play again (y/n): ")
        if retry_input == "y":
            retry = True
            valid_input = True
            showing_stakes = True
        elif retry_input == "n":
            sys.exit()
        else:
            print("That is not a valid input.")
    return(retry)
        
    

#after the progam retrys ask the user if they would like to see the stakes again
def showing_stakes():
    see_odds = True
    while see_odds == True:
        user_input= input("Would you like to see the Stakes again?(y/n): ")
        
        if user_input == "y":
            time.sleep(0.25)
            print("a)3/1, ", end= ' ', flush=True)
            time.sleep(0.25)
            print("b)6/1, ", end= ' ', flush=True)
            time.sleep(0.25) 
            print("c)16/1",  end= ' ', flush=True)
            time.sleep(0.25)
            see_odds = False
        elif user_input == "n":
            see_odds = False
        else:
            print("That is not a valid statment") 
            see_odds = True
    
    
    

a = [1, 2, 3]
b = [1, 2, 3, 4, 5, 6]
c = list(range(1, 16))


input("Welcome too lose your money ...")

mode = input("What difficulty would you like to play on? \na) easy \nb) hard\n")

if mode == "a":
    money = 1000
    time.sleep(0.25)
    input("You have chosen easy mode, you start with 1000 currnecy...")
    time.sleep(0.5)
    print("Time to choose your stake")
    time.sleep(0.25)
    print("a)3/1, ", end= ' ', flush=True)
    time.sleep(0.25)
    print("b)6/1, ", end= ' ', flush=True)
    time.sleep(0.25) 
    print("c)16/1",  end= ' ', flush=True)
    time.sleep(0.25)
    retry = True
    winningsEA = 0
    loan_played = "holder"
    times_played = 0
    back_to_zero = "holder"
    
    while retry == True:
        time.sleep(0.5)
        if back_to_zero == True and money < 1:
            input("You have lost all your money whilst having a loan...")
            time.sleep(0.5)
            print("You have lost to the bank")
            sys.exit()
        
        if money < 1:
            input("\nYou do not have enough money to place another bet...")
            input_loan = input("Would you like to take a loan from the bank?(y/n): ")
            if input_loan == "n":
                print("You lost to the bank.")
                sys.exit()
            if input_loan == "y":
                loan_valid = True  
                input("You have chosen to take a loan...")
                
                while loan_valid == True:
                       loan_amount = input("How much would you like to have (max 100) ")
                    if loan_amount > 100:
                        print("That is too much.")
                        loan_valid = True
                            
                    elif loan_amount <= 100:
                        money = loan_amount + money
                        print(f"You have recieved {loan_amount} your total is now {money} ")
                        time.sleep(0.25)
                        pay_back = loan_amount * 1.5
                        print(f"You must pay back {pay_back} in five rounds")
                        print("This will be the only loan you recieve, use it wisely")
                        input("Please press enter to continue...")
                        loan_played = 0
                        back_to_zero = True
        
        
        
        
        if times_played > 0:
            showing_stakes()
        
        mode = input("Which do you want (a, b, c): ")
        
        
            
    
        if mode == "a":
                    
                
                
                
            answer = random.choice(a)
            time.sleep(0.25)
            print("You have chosen a)3/1")
            time.sleep(0.25)
            yay = 1
            while yay == 1:
                easyA = int(input("\nHow much would you like to bet?: "))
                if easyA > money:
                    print("You do not have enough to bet that much")
                else:
                    yay = 0
            time.sleep(0.25)
            print(f"You have bet {easyA}")
            time321()
            
            if answer == 1:
                money = easyA * 3 + money
                winningsEA = easyA * 3
                time.sleep(0.25)
                print(f"You have won {winningsEA}! ")
                time.sleep(0.75)
                print(f"Your total is now {money}")
                
                time.sleep(0.25)
                
                    


            elif answer != 1:
                money = int(money) - int(easyA)
                time.sleep(0.75)
                print(f"Oh no you have lost, your currnet balance is {money}")
                
                        
        if mode == "b":
            answer = random.choice(b)
            print("You have chosen b)6/1")
            yay1 = 1
            while yay1 == 1:
                easyB = str(input("\nHow much would you like to bet?: "))
                if int(easyB) > int(money):
                    print("You do not have enough to bet that much")
                else:
                    yay1 = 0
            print(f"You have bet {easyB}")
            time321()
            
            if answer == 1:
                money = int(easyB) * 6 + money
                winningsEB = easyB * 6 + easyB
                print(f"You have won {winningsEB}! ")
                print(f"Your total is now {money}")
                
                    


            elif answer != 1:
                money = int(money) - int(easyB)
                print(f"Oh no you have lost, your currnet balance is {money}")
                
                        
                        
                        
                        
        if mode == "c":
            answer = random.choice(c)
            print("You have chosen c)16/1")
            easyC = str(input("\nHow much would you like to bet?: "))
            print(f"You have bet {easyC}")
            time321()
            
            if answer == 1:
                money = int(easyC) * 16 + money
                winningsEC = easyC * 16 + easyC
                print(f"You have won {winningsEC}! ")
                print(f"Your total is now {money}")
                  
                    


            elif answer != 1:
                money = int(money) - int(easyC)
                print(f"Oh no you have lost, your currnet balance is {money}")
            
            if loan_played != "holder":
                loan_played = loan_played + 1
                turns_left = 5 - loan_played
                input(f"You have {turns_left} left to pay back the loan.")
                
                        
        times_played += 1 #times_played = times_played + 1                                          
        retry = askForRetry()
        
        
            
                        
            
                        
                        
                    
                    
                    
                
                
                    
#make it so that you can see the stakes after a retry use a function
            
            
            
            
