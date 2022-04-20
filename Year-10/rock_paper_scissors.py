import time
import random


same_guess = "oh"
retry = "y"

a = ["rock", "paper", "scissors"]
    
play = input("\nWould you like to play rock paper scissors? y/n: ")
play = play.lower()

if play == "n":
    print("Thanks for nothing!")
    exit()

while retry == "y":
        computer_action = random.choice(a) 
        if play == "y":
            guess = input("\nPlease select rock, paper, or scissors: ")
            guess = guess.lower()

            if (guess == "rock" or guess == "paper" or guess == "scissors"):
                time.sleep(0.25)
                print("3...", end= ' ', flush=True)
                time.sleep(0.5)
                print("2...", end= ' ', flush=True)
                time.sleep(0.5) 
                print("1...",  end= ' ', flush=True)
                time.sleep(0.5)

                print(f"\n{computer_action}")
            if computer_action == guess:
                print("Oh no its a tie!")
                
            retry = input("Would you like to play again? y/n: ")
               
            if input == "y":
                retry = "y"
                
            elif input == "n":
                exit()
