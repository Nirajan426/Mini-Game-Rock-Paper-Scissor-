import random
import os
import time

os.system('cls')  # clear the terminal

# Initialize scores
user_score = 0
computer_score = 0
draws = 0

# Game instructions and welcome message
print("Welcome to Rock, Paper, Scissors!")
print("Instructions: ")
print("1. Scissors = s")
print("2. Paper = p")
print("3. Rock = r")
print("4. Press 'q' to quit the game.\n")

while True:
    os.system('cls')
    print("Get ready!")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    
    computer_bot = random.choice([1, 2, 3])  # computer chooses among 1, 2 & 3
    print("S = Scissor, P = Paper, R = Rock\n")  # Printing the menu
    user_input = input("Enter your choice: ").lower()  # user input s or p or r
    
    # Check for exit condition
    if user_input == 'q':
        print("Thanks for playing!")
        break
    
    # clear the terminal
    os.system('cls')

    dataDict = {'s': 1, 'p': 2, 'r': 3}
    
    # Validate user input
    while user_input not in ['s', 'p', 'r']:
        print("Invalid input! Please choose from s (Scissor), p (Paper), or r (Rock).")
        user_input = input("Enter your choice: ").lower()

    user = dataDict[user_input]
    reverseDict = {1: "Scissor", 2: "Paper", 3: "Rock"}

    # Checking the conditions
    if computer_bot == user:
        draws += 1
        result = "Opps! Draw"
    elif (computer_bot == 1 and user == 2) or (computer_bot == 2 and user == 3) or (computer_bot == 3 and user == 1):
        user_score += 1
        result = "You Won"
    else:
        computer_score += 1
        result = "You Lose"

    # Showing the result
    print(result)
    print(f"You choose {reverseDict[user]}\nComputer choose {reverseDict[computer_bot]}")
   
    
    # Display the score after each round
    print(f"Scores: You {user_score} - Computer {computer_score} - Draws {draws}")
    
    # Ask if the user wants to play again
    dec = input("\nDo you want to play again (y/n)?\n").lower()
    if dec == 'n':
        print("Thanks for playing!")
        break
