import random

play_again = True

while play_again:
    secret_number = random.randint(1, 100)
    player_guess = int(input("Guess the secret number: "))

    while player_guess != secret_number:
        if player_guess < secret_number:
            print("Too low, try again")
        else:
            print("Too high, try again")
        player_guess = int(input("Guess the secret number: "))

    print("You were right!")

    response = input("Do you want to play again? (y-yes/n-no): ").strip().lower()
    play_again = response in ("y", "yes")

