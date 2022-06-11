# Python "guess the number" game by Levi Miller for IST Y9

# INSTRUCTIONS:
# The computer program must generate a random number called “secret” between 1 and 100.
# The user is asked to input a “guess” (research how to create a random number in python)
# Record the number of guesses made and store in “count”
#  If guess is equal to secret then the program will output ‘Well done you have guessed the number” and also “You have used <count> guesses”
# Include the following outputs for the guesses with these rules:
#  “boiling”: within 5 numbers of the secret number
#  “hot”: within 10 numbers of the secret number
#  “warm”: within 20 of the secret number
#  “cold”: within 40 of the secret number
#  “freezing”: greater than 40 of the secret number


# Imports random, os, time and termcolor modules.

# Os is used to clear the screen.
# Random is used to generate random numbers.
# Time is used to wait a specific amount of seconds at times.
# Termcolor is used to change the color of text.
from os import name, system
from random import randint
from time import sleep
from termcolor import colored, cprint

# Clears screen to make colour's work on Windows.
system("cls" if name == "nt" else "clear")
# Tells you how the game works
print(
    "Im thinking of a number between "
    + colored("0", "red")
    + " and "
    + colored("100", "red")
    + """
You need to guess this number
If I tell you """
    + colored("boiling", "red", attrs=["bold"])
    + ", your within "
    + colored("5", "red")
    + """
If I tell you """
    + colored("hot", "yellow", attrs=["bold"])
    + ", your within "
    + colored("10", "yellow")
    + """
If I tell you """
    + colored("warm", "green", attrs=["bold"])
    + ", your within "
    + colored("30", "green")
    + """
If I tell you """
    + colored("cold", "cyan", attrs=["bold"])
    + ", your within "
    + colored("40", "cyan")
    + """
And if I say """
    + colored("freezing", "blue", attrs=["bold"])
    + ", your over "
    + colored("40", "blue")
    + " away from my number\n"
)
input("Press enter to begin")

# This clears the screen.
# With the "if os.name == 'nt'" it checks if the OS is Windows. Else it will just run clear
# This is because Windows has a different clear command.
system("cls" if name == "nt" else "clear")

# Main loop for the game
playing = True
while playing == True:
    # Generates a random number between 0 and 100
    secret = randint(0, 100)
    # This is the number of guesses the player has made
    guesses = 0

    # Loop for guessing
    guessing = True
    while guessing == True:
        guesses += 1
        print("Guess a number between 0 and 100")
        # This shows your number of guesses
        print(
            "This is your " + colored("first", "red", attrs=["bold"]) + " guess"
            if guesses == 1
            else "You have tried " + colored(guesses, "red", attrs=["bold"]) + " times"
        )

        # The program will try run this code, but if a "ValueError" is raised, it will skip this
        try:
            guess = int(input("Number: "))
            system("cls" if name == "nt" else "clear")

            # Checks if the input was a number and isn't too high or low
            if str(guess).isnumeric() == False or guess > 100 or guess < 0:
                cprint("Invalid input\n", "red")

            # Checks if the number is within 5 of the secret number
            elif guess in range(secret - 5, secret + 5) and guess != secret:
                cprint("Boiling\n", "red", attrs=["bold"])

            # Checks if the number is within 10 of the secret number
            elif guess in range(secret - 10, secret - 5) or guess in range(
                secret + 5, secret + 10
            ):
                cprint("Hot\n", "yellow", attrs=["bold"])

            # Checks if the number is within 30 of the secret number
            elif guess in range(secret - 20, secret - 10) or guess in range(
                secret + 10, secret + 20
            ):
                cprint("Warm\n", "green", attrs=["bold"])

            # Checks if the number is within 40 of the secret number
            elif guess in range(secret - 40, secret - 20) or guess in range(
                secret + 20, secret + 40
            ):
                cprint("Cold\n", "cyan", attrs=["bold"])

            # Checks if the number is over 40 away from the secret number
            elif (
                guess <= secret + 40
                and guess != secret
                or guess >= secret - 40
                and guess != secret
            ):
                cprint("Freezing\n", "blue", attrs=["bold"])

            # Checks if the number is the secret number
            elif guess == secret:
                guessing = False

            # I think its impossible to get here but you never know ;)
            else:
                print("idk how you got here...\n")
                input()
                exit()

        # This is if the guess caused a value error
        # This is because the user didn't enter anything
        except ValueError:
            system("cls" if name == "nt" else "clear")
            cprint("Invalid input\n", "red")
            continue

    # This is if the player guessed the number
    print(
        "You guessed the right number in "
        + colored(guesses, "red", attrs=["bold"])
        + " guesses!"
    )

    # This is if the player wants to play again
    win = True
    while win == True:
        print(
            "Would you like to play again? " + colored("(Y/N)", "green", attrs=["bold"])
        )
        # Makes sure the users input is in lowercase
        answer = input().lower()

        # If they answer with no
        if answer == "n":
            cprint("Thanks for playing!", "green", attrs=["bold"])
            sleep(2)
            exit()

        # If they answer with yes
        elif answer == "y":
            system("cls" if name == "nt" else "clear")
            guessing = True
            win = False

        # If they answer with something else
        else:
            cprint("Invalid input", "red")
            sleep(2)
            system("cls" if name == "nt" else "clear")

# I had a lot of fun making this and I hope you enjoy it!
# I have done my best to check for any errors and to avoid crashes
