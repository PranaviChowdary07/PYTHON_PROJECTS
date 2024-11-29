import random
import logo_art

EASY_LEVEL_ATTEMPTS = 15
MEDIUM_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty(level_chosen):
    if level_chosen == 'Easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen == 'Medium':
        return MEDIUM_LEVEL_ATTEMPTS
    elif level_chosen == 'Hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return None 

def check_answer(guessed_number, answer, attempts):
    if guessed_number < answer:
        print("Your guess is too low")
        return attempts - 1
    elif guessed_number > answer:
        print("Your guess is too high")
        return attempts - 1
    else:
        print(f"Your guess is correct! The answer is {answer}")
        return attempts

def game():
    print(logo_art.logo)
    print ("")
    print("Let me think of a number between 1 and 100.")
    answer = random.randint(1, 100)

    while True:
        level = input("Choose level of difficulty: 'Easy', 'Medium', or 'Hard': ").capitalize()
        attempts = set_difficulty(level)
        
        if attempts is None:
            print("You have entered an invalid difficulty level. Please choose again.")
        else:
            break

    guessed_number = 0
    while guessed_number != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guessed_number = int(input("Guess a number: "))
        attempts = check_answer(guessed_number, answer, attempts)

        if attempts == 0:
            print("You are out of guesses. You lose!")
            return
        elif guessed_number != answer:
            print("Guess again")

game()
