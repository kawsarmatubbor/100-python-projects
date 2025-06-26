import random

secret = random.randint(1, 1000)

max_attempts = 10
attempts = 0

while attempts < max_attempts :
    user_input = int(input(f"Guess a number between 1 to 1000 ({max_attempts - attempts} attempts left): "))
    attempts +=1
    if secret == user_input:
        print(f"Congratulations! You guessed it in {attempts} attempts. The number is {secret}.\n")
        break
    elif secret < user_input:
        print("Too high! Try again.\n")
    elif secret > user_input:
        print("Too low! Try again.\n")
else:
    print(f"Game over. The number is {secret}.\n")