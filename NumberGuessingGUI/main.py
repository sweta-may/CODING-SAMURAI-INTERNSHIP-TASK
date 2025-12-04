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

        def create_welcome_screen(self):
            for widget in self.root.winfo_children():
                widget.destroy()
            title = tk.Label(
                self.root,
                text="🎮 Number Guessing Game 🎮",
                font=("Arial", 22, "bold"),
                bg="#1e1e2e",
                fg="#cdd6f4"
            )
            title.pack(pady=30)

            desc = tk.Label(
                self.root,
                text="I'm thinking of a number between 1-100\nCan you guess it?",
                font=("Arial", 13),
                bg="#1e1e2e",
                fg="#bac2de",
                justify="center"
            )
            desc.pack(pady=20)

            difficulty_label = tk.Label(
                self.root,
                text="Choose Difficulty Level:",
                font=("Arial", 14, "bold"),
                bg="#1e1e2e",
                fg="#cdd6f4"
            )
            difficulty_label.pack(pady=20)

            easy_btn = tk.Button(
                self.root,
                text=f"🟢 EASY\n({EASY_LEVEL_TURNS} turns)",
                font=("Arial", 14, "bold"),
                bg="#a6e3a1",
                fg="#1e1e2e",
                command=lambda: self.start_game("easy"),
                cursor="hand2",
                width=15,
                height=3,
                bd=0
            )
            easy_btn.pack(pady=10)

            hard_btn = tk.Button(
                self.root,
                text=f"🔴 HARD\n({HARD_LEVEL_TURNS} turns)",
                font=("Arial", 14, "bold"),
                bg="#f38ba8",
                fg="#1e1e2e",
                command=lambda: self.start_game("hard"),
                cursor="hand2",
                width=15,
                height=3,
                bd=0
            )
            hard_btn.pack(pady=10)

            def start_game(self, level):
                self.answer = randint(1, 100)
                self.turns = EASY_LEVEL_TURNS if level == "easy" else HARD_LEVEL_TURNS
                self.guess = 0
                self.game_started = True
                self.create_game_screen()

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