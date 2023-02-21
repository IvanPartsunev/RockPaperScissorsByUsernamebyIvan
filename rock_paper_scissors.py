import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_choice = ""

print("Type 'exit' to exit game.")

while True:
    player = input("Choose Rock, Paper or Scissors by typing [r], [p] or [s]: ")

    if player == "exit":
        exit()

    win = True
    while True:

        if player == "r" or player == "[r]" or player == "Rock":
            player_choice = rock
            break
        elif player == "p" or player == "[p]" or player == "Paper":
            player_choice = paper
            break
        elif player == "s" or player == "[s]" or player == "Scissors":
            player_choice = scissors
            break
        else:
            print("Invalid input!")
            print("Try again!")
            print()

    print(f"You choose: {player_choice}")

    computer = ["Rock", "Paper", "Scissors"]

    computer_choice = random.choice(computer)

    print(f"Opponent choose: {computer_choice}")
    print()

    if player_choice == computer_choice:
        print(f"Draw!", ("\n"*2))
        continue
    elif player_choice == "Rock":
        if computer_choice == "Paper":
            win = False
    elif player_choice == "Paper":
        if computer_choice == "Scissors":
            win = False
    else:
        if computer_choice == "Rock":
            win = False

    if win:
        print("You WIN!!!", ("\n"*2))

    else:
        print("You lose.", ("\n"*2))

