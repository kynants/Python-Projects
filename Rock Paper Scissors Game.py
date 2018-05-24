# MY INITIAL ATTEMPT
'''
def weapon(rock, paper, scissors)
rock
paper
scissors

    if user == "rock" and computer == "scissors":
        print("User wins!")

    elif user == "rock" and computer == "paper":
        print("Computer wins!")

    elif user == "paper" and computer == "rock":
        print("User wins!")

    elif user == "paper" and computer == "scissors":
        print("Computer wins!")

    elif user == "scissors" and computer == "paper":
        print("User wins!")

    elif user == "scissors" and computer == "rock":
        print("Computer wins!")

    else user == computer:
        print("Draw!")

yourAnswer = input("Which weapon will you choose?")
print()
'''

# ONLINE SOLUTION (WITH SOME MINOR BUGS I FIXED)
# https://youtu.be/TGUi8TRwI3A
import random

# Define the Computer Choice Function
def rps():
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        computer_choice_rock()
    elif computer_choice == 2:
        computer_choice_paper()
    else:
        computer_choice_scissors()

# Define Function when computer chooses Rock
def computer_choice_rock():
    #I had to change "raw_input" to "input" for Python 3
    user_choice = input("1 for Rock, 2 for Paper, 3 for Scissors: ")
    if user_choice == "1":
        print("You Tie. You chose Rock and the computer chose Rock.")
        try_again()
    if user_choice == "2":
        print("You Win! You chose Paper and the computer chose Rock.")
        try_again()
    if user_choice == "3":
        print("You Lose! You chose Scissors and the computer chose Rock.")
        try_again()
    else:
        print("Try again")
        computer_choice_rock()

# Define Function when computer chooses Paper
def computer_choice_paper():
    user_choice = input("1 for Rock, 2 for Paper, 3 for Scissors: ")
    if user_choice == "1":
        print("You Lose! You chose Rock and the computer chose Paper.")
        try_again()
    if user_choice == "2":
        print("You Tie. You chose Paper and the computer chose Paper.")
        try_again()
    if user_choice == "3":
        print("You Win! You chose Scissors and the computer chose Paper.")
        try_again()
    else:
        print("Try again")
        computer_choice_paper()

# Define Function when computer chooses Scissors
def computer_choice_scissors():
    user_choice = input("1 for Rock, 2 for Paper, 3 for Scissors: ")
    if user_choice == "1":
        print("You Win! You chose Rock and the computer chose Scissors.")
        try_again()
    if user_choice == "2":
        print("You Lose! You chose Paper and the computer chose Scissors.")
        try_again()
    if user_choice == "3":
        print("You Tie. You chose Scissors and the computer chose Scissors.")
        try_again()
    else:
        print("Try again")
        computer_choice_scissors()

# Define Try Again Function
def try_again():
    choice = input("Would you like to play again? y/n ")
    if choice == "y" or choice == "yes" or choice == "Y":
        rps()
    #I had added 2 more choices for entering "No"
    elif choice == "n" or choice == "no" or choice == "N":
        print("Thanks for playing")
        quit()
    else:
        print("Try again")
        try_again()
rps()