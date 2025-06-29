import random

print("Welcome to Rock Paper Scissor")
options = ["Rock", "Paper", "Scissor"]

while True:
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    print("0. Exit")

    user = int(input("Choose an option: "))
    machine = random.randint(1, 3)

    if user == 0:
        break
    elif user == 1 or user == 2 or user == 3:
        if user == machine:
            print("Tie!")
        elif (user == 1 and machine == 3) or (user == 2 and machine == 1) or (user == 3 and machine == 2):
            print("Win!")
        else:
            print("Lose!")
        print(f"You chose {options[user-1]} and Machine chose {options[machine-1]}\n")
    else:
        print("Invalid option.\n")

        