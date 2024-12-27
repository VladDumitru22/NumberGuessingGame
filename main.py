from random import randint

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def check_answer(number_to_guess, user_guess, attempts):
    """Checks answer against guess, returns the number of attempts remaining."""
    if user_guess > number_to_guess:
        print("Too high.")
        return attempts-1
    elif user_guess < number_to_guess:
        print("Too low.")
        return attempts-1
    else:
        print(f"Correct! The answer was {number_to_guess}")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS


def game():

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = randint(1, 100)
    #print(f"HINT: {number_to_guess}")

    attempts = set_difficulty()

    user_guess = 0
    while user_guess != number_to_guess:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        attempts = check_answer(number_to_guess, user_guess, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return
        elif user_guess != number_to_guess:
            print("Guess again.")

game()