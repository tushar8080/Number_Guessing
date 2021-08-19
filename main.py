from Number_Guessing_Art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, number, turns):
    """checks answers against guess. Returns number of turns remaining"""
    if guess > number:
        print("Too High")
        return turns -1
    elif guess < number:
        print("Too Low")
        return turns -1
    else:
        print(f"You got it. The answer was {number}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'Easy' or 'Hard':\t").title()
    if level == "Hard":
        global turns
        return HARD_LEVEL_TURNS

    elif level == "Easy":
        turns = EASY_LEVEL_TURNS
    else:
        print("Invalid choice")


def game():
    print(logo)

    print("Welcome to the number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    number = random.choice(range(1, 100))
    # print(f"psst! the number is {number}")

    turns = set_difficulty()

    guess = 0
    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a Guess: "))
        turns = check_answer(guess, number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif turns != 0:
            print("Guess again.")


game()
ā