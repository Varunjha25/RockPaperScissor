"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, paper, scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

Additional Features
Keep track of the score: Wins for the user, wins for the computer, and ties.
Ask the user if they want to play another round.
Display a final scoreboard when the user chooses to exit.
"""

import random

item_list = ["Rock", "Paper", "Scissor"]

# Initialize counters for wins
user_wins = 0
comp_wins = 0
ties = 0

while True:
    # Take user input and normalize it
    User_choice = input("Enter your move: Rock, Paper, Scissor\n").capitalize()
    
    if User_choice not in item_list:
        print("Invalid choice. Please enter Rock, Paper, or Scissor.")
        continue  # Restart the loop for valid input

    # Generate computer's choice
    comp_choice = random.choice(item_list)

    print(f"User_choice = {User_choice}, Comp_choice = {comp_choice}")

    # Game logic
    if User_choice == comp_choice:
        print("Both chose the same: Match Tie!")
        ties += 1  # Increment tie counter

    elif User_choice == "Rock":
        if comp_choice == "Paper":
            print("Paper covers Rock: Computer wins!")
            comp_wins += 1  # Increment computer win counter
        else:
            print("Rock smashes Scissor: You win!")
            user_wins += 1  # Increment user win counter

    elif User_choice == "Paper":
        if comp_choice == "Scissor":
            print("Scissor cuts Paper: Computer wins!")
            comp_wins += 1
        else:
            print("Paper covers Rock: You win!")
            user_wins += 1

    elif User_choice == "Scissor":
        if comp_choice == "Paper":
            print("Scissor cuts Paper: You win!")
            user_wins += 1
        else:
            print("Rock smashes Scissor: Computer wins!")
            comp_wins += 1
            
        

    # Display the score after each round
    print(f"\nScoreboard: You = {user_wins}, Computer = {comp_wins}, Ties = {ties}\n")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nFinal Scoreboard:")
        print(f"You: {user_wins} | Computer: {comp_wins} | Ties: {ties}")
        print("Thanks for playing! Goodbye!")
        break
