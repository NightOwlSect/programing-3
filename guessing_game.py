import random

#player_guess = 0

secret_number = random,randrange(1,10)

player_guess=int(input("Guess the secret number:"))

if player_guess == secret_number:
    print("You were right")

print(secret_number)
