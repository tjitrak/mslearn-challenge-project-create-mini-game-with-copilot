# import the random module
import random

# create a list of options that has rock, paper, and scissors

options = ["rock", "paper", "scissors"]

# create a score variable and set it to 0

score = 0

# create a variable to count the number of rounds

rounds = 0

while True:
    # get the user input for rock, paper, or scissors
    user_input = input("Enter rock, paper, or scissors: ")

    # get the computer's choice
    computer_choice = random.choice(options)

    # print out the computer's choice
    print("The computer chose: " + computer_choice)

    # check to see if the user input is valid
    if user_input not in options:
        print("Invalid input. Try again.")
        continue

    # check to see if the user and computer tied
    if user_input == computer_choice:
        print("You tied!")
        rounds += 1
        continue

    # check to see if the user won
    if user_input == "rock" and computer_choice == "scissors":
        print("You won!")
        score += 1
        rounds += 1
        continue
    if user_input == "paper" and computer_choice == "rock":
        print("You won!")
        score += 1
        rounds += 1
        continue
    if user_input == "scissors" and computer_choice == "paper":
        print("You won!")
        score += 1
        rounds += 1
        continue

    # if the user didn't win or tie, then the computer won
    print("You lost!")
    rounds += 1

    # print out the score
    print("Score: " + str(score))

    # print out the number of rounds
    print("Rounds: " + str(rounds))

    # ask the user if they want to play again
    play_again = input("Do you want to play again? (y/n) ")

    # if the user doesn't want to play again, then break out of the loop
    if play_again == "n":
        break