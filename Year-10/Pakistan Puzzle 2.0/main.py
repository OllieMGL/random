from questions import question_list
import sys
import random

def answers(user_answer, current_answer):
    if user_answer.strip().lower() == current_answer.strip().lower():
        return("correct!")
    else:
        return("Incorrect")
    
def saveScoreToFile(score, num): 
    name = input("Please enter your name: ")
    f = open("scores.txt", "a")
    f.write(f"\n{name} - {score}/{num}")
    f.close()
    
    f = open("scores.txt", "r")
    print(f"{f.read()}")    
    
    
counter = 1
num_of_questions = 0   
score = 0    
#makes a list of question keys
question_keys = list(question_list.keys())

input("\nWelcome to the Pakistan Puzzle! Test your knowledge of the country!...")
while len(question_keys) != 0: 
    #takes a random item from the list of question keys
    current_question_key = random.choice(question_keys)
    #assign 'current_question' to the value of random key from the dictionary
    current_question = question_list[current_question_key][0]
    current_answer = question_list[current_question_key][1]
    
    print(f"\n{counter}){current_question}")
    user_answer = input("Please enter answer here: ")
    result = answers(user_answer, current_answer)
    print(result)    
    question_keys.remove(current_question_key)
    if result == "Incorrect":
        num_of_questions = num_of_questions + 1
        counter = counter + 1 
        input(f"Your current score is {score}/{num_of_questions}...")
    if result == "correct!":
        num_of_questions = num_of_questions + 1
        score = score + 1
        counter = counter + 1 
        input(f"Your current score is {score}/{num_of_questions}...")
        
        
    
input(f"\nYour final score was {score}/{num_of_questions}...")
user_input = input("Would you like to save your score?(y/n): ")
if user_input == "n":
    ("cool")
    sys.exit()
    
if user_input == "y":
    saveScoreToFile(score, num_of_questions)
    










