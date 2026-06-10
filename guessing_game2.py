import Random
play_again = True:
secret_number = random.randrange(1,100);

player_guess=int(input("Guess the secret number:"));

while player_guess != secret_number:
    player_guess=int(input("Guess the secret number:"));
    if player_guess < secret_number:
        print("Too low, try again");
    elif player_guess > secret_number:
        print("Too high, try again");   

If player_guess == secret_number:
    print("You were right");

response = input("Do you want to play again? (y-yes/n-no):");
if response == "yes" or response == "y":
     play_again = True
     while play_again:
        secret_number = random.randrange(1,100);
        player_guess=int(input("Guess the secret number:"));
        while player_guess != secret_number:
            player_guess=int(input("Guess the secret number:"));
            if player_guess < secret_number:
                print("Too low, try again");
            elif player_guess > secret_number:
                print("Too high, try again");   
        if player_guess == secret_number:
            print("You were right");
        response = input("Do you want to play again? (y-yes/n-no):");
        if response == "yes" or response == "y":
             play_again = True
else:     play_again = False
