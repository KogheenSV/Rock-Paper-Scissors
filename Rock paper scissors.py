import random

def play_game():
    # Get player choice
    player_choice = input("Rock, paper, or scissors? ").lower()
    while player_choice not in ["rock", "paper", "scissors"]:
        player_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()

    # Get computer choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Print choices
    print("You chose:", player_choice)
    print("Computer chose:", computer_choice)

    # Determine winner
    if player_choice == computer_choice:
        print("Tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")

# Play game
while True:
    play_game()
    play_again = input("Play again? (y/n)").lower()
    if play_again != "y":
        break
