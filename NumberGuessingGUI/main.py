from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    if user_guess == actual_answer:
        print(f"Your guess is Correct! I was thinking of {user_guess}")
    elif user_guess < actual_answer:
        print("Too low")
        return turns-1
    else:
        print("Too high")
        return turns-1

def difficulty_level():
    level = int(input("Enter the difficulty level: "))
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
print("Welcome to Number Guessing game!!")
print("I'm thinking of a number between 1-100")
answer = randint(1,100)

turns = difficulty_level()
print(f"You have {turns} turns left")
guess = 0
while guess != answer:
    guess = int(input("Guess the number: "))
    turns = check_answer(guess, answer, turns)