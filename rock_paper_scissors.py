import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
options[0]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("computer picked", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue
    if user_input == computer_pick:
        print("Nobody wins!")
        user_wins =+ 0
        computer_wins += 0
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue
    else:
        print("you lost!")
        computer_wins += 1
        continue

print ("you won",user_wins,"times.")
print("the computer",computer_wins,"times.")

print("Goodbye!")

