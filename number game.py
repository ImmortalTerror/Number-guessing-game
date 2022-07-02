# Python "guess the number" game by Levi Miller for IST Y9
# Note: Remade a lot of this. Made it much nicer.

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
from termcolor import colored as c, cprint


# Check function
def check(secret: int, guess: int) -> str or bool:
    """Checks how close guess is to secret

    Args:
        secret (int): Secret number
        guess (int): Users guessed number

    Raises:
        TypeError: If either guess or secret is not an int

    Returns:
        str: Coloured text based on your guess
        bool: If the guess was correct
    """
    # Makes sure both arguments are integers
    if type(secret) != int or type(guess) != int:
        raise TypeError("Guess and Secret must be an int")

    # If the guess is higher than 100 or lower than 0
    if guess > 100 or guess < 0:
        return outputs["invalid"]

    # If the guess is equal to the secret number
    if guess == secret:
        return True

    # Calculates the distance between the secret and guess
    dist = abs(secret - guess)

    # Calculates the ranges for each output
    values = {
        "boiling": range(1, 6),
        "hot": range(6, 11),
        "warm": range(11, 21),
        "cold": range(21, 41),
    }

    # Checks if the distance is in any of the ranges
    # If it is, outputs a string depending on which range
    for i in values.items():
        if dist in i[1] and guess != secret:
            return outputs[i[0]]

    # If all checks failed, guess is in freezing range
    return outputs["freezing"]


# Clears screen to make colour's work on Windows.
system("cls" if name == "nt" else "clear")
# Tells user how the game works
print(
    "Im thinking of a number between "
    + c("0", "red")
    + " and "
    + c("100", "red")
    + """
You need to guess this number
If I tell you """
    + c("boiling", "red", attrs=["bold"])
    + ", your within "
    + c("5", "red")
    + """
If I tell you """
    + c("hot", "yellow", attrs=["bold"])
    + ", your within "
    + c("10", "yellow")
    + """
If I tell you """
    + c("warm", "green", attrs=["bold"])
    + ", your within "
    + c("30", "green")
    + """
If I tell you """
    + c("cold", "cyan", attrs=["bold"])
    + ", your within "
    + c("40", "cyan")
    + """
And if I say """
    + c("freezing", "blue", attrs=["bold"])
    + ", your over "
    + c("40", "blue")
    + " away from my number\n"
)
input("Press enter to begin")

# Coloured output text dictionary
outputs = {
    "invalid": c("Invalid input", "red"),
    "boiling": c("Boiling", "red", attrs=["bold"]),
    "hot": c("Hot", "yellow", attrs=["bold"]),
    "warm": c("Warm", "green", attrs=["bold"]),
    "cold": c("Cold", "cyan", attrs=["bold"]),
    "freezing": c("Freezing", "blue", attrs=["bold"]),
}

# This clears the screen.
# With the "if os.name == 'nt'" it checks if the OS is Windows. Else it will just run clear
# This is because Windows has a different clear command to other OS's.
system("cls" if name == "nt" else "clear")

# Main loop for the game
while True:
    # Calculates secret number
    secret = randint(0, 100)
    # Number of guesses user has made
    guesses = 0

    # Loop for guessing
    guessing = True
    while guessing == True:
        guesses += 1
        print("Guess a number between 0 and 100")
        # shows your number of guesses
        print(
            "This is your " + c("first", "red", attrs=["bold"]) + " guess"
            if guesses == 1
            else "You have tried " + c(guesses, "red", attrs=["bold"]) + " times"
        )

        # The program will try run this code, but if an error is raised, output "invalid input"
        try:
            # Gets user input and runs through check func
            guess = int(input("Number: "))
            system("cls" if name == "nt" else "clear")

            checked = check(secret, guess)

            # If user guessed the secret number
            if checked == True:
                guessing = False
            else:
                print(f"{checked}\n")

        # If an invalid input was given
        except:
            system("cls" if name == "nt" else "clear")
            print(outputs["invalid"] + "\n")

    # When the player has guessed the correct number
    print(
        "You guessed the right number in "
        + c(guesses, "red", attrs=["bold"])
        + " guesses!"
    )

    # Asks if the player would like to play again
    win = True
    while win == True:
        print("Would you like to play again? " + c("(Y/N)", "green", attrs=["bold"]))
        # Makes sure the users input is in lowercase
        answer = input().lower()

        # If they answered with no
        if answer == "n":
            cprint("Thanks for playing!", "green", attrs=["bold"])
            sleep(2)
            exit()

        # If they answered with yes
        elif answer == "y":
            system("cls" if name == "nt" else "clear")
            guessing = True
            win = False

        # If they answered with something invalid
        else:
            cprint("Invalid input", "red")
            sleep(2)
            system("cls" if name == "nt" else "clear")

# I had a lot of fun making this and I hope you enjoy it!
# I have done my best to check for any errors and to avoid crashes
