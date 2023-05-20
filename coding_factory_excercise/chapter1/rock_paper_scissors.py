import random

while True:
    
    options = ["rock", "paper", "scissors"]
    
    player_input = input("Enter your choice (rock, paper, scissors): ").lower()
    computer_str = random.choice(options)
    print("You chose: ",  player_input)
    print("Computer chose: ", computer_str)


    if player_input == computer_str:
        print("It's a draw!")
    elif player_input == "rock":
        if computer_str == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player_input == "paper":
        if computer_str == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player_input == "scissors":
        if computer_str == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
        print("not valid choice")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again.lower() != "yes":
        break