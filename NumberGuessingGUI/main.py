from random import randint
from tkinter import messagebox
import tkinter as tk

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("450x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.answer = None
        self.turns = None
        self.guess = 0
        self.game_started = False

        self.create_welcome_screen()

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