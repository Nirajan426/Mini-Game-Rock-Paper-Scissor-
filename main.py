import random
import os
os.system('cls') #clear the terminal
'''
Here,
1 for scissor
2 for paper
3 for rock 

'''
while True:
    os.system('cls')
    computer_bot =random.choice([1,2,3]) #computer chooses among 1,2 & 3
    print("S=Scissor P=Paper R=Rock\n") #Printing the menu
    user_input=input("Enter your choice\n").lower() #user input s or p or r as input
    # clear the  terminal
    os.system('cls')

    dataDict={'s':1,'p':2,'r':3}
    user=dataDict[user_input]
    reverseDict={1:"Scissor",2:"Paper",3:"Rock"}

    # checking the conditions
    if(user_input=='p' or user_input=='s' or user_input=='r'):
        if(computer_bot==user):
            print("Opps! Draw ")
        else:
            if(computer_bot==1 and user==2):
                print("You Lose ")
            elif(computer_bot==1 and user==3):
                print("You Won ")
            elif(computer_bot==2 and user==1):
                print("You won ")
            elif(computer_bot==2 and user==3):
                print("You Lose ")
            elif(computer_bot==3 and user==1):
                print("You Lose ")
            elif(computer_bot==3 and user==2):
                print("You won ")

        # Showing who choose what
        print(f"You choose {reverseDict[user]}\nComputer choose {reverseDict[computer_bot]}")
        
        #Asking user if he/she wants to play more??

        dec=input("\nDo You want to play again (y/n)?\n")
        decision=dec.lower()
        if(decision=='n'):
           break
    else:
        print("Invalid choice!")

