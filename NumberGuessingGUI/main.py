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

    def create_game_screen(self):

        for widget in self.root.winfo_children():
            widget.destroy()


        title = tk.Label(
            self.root,
            text="Number Guessing Game",
            font=("Arial", 20, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        )
        title.pack(pady=20)


        self.turns_label = tk.Label(
            self.root,
            text=f"You have {self.turns} turns left",
            font=("Arial", 14, "bold"),
            bg="#1e1e2e",
            fg="#f9e2af"
        )
        self.turns_label.pack(pady=10)


        range_label = tk.Label(
            self.root,
            text="Number is between 1-100",
            font=("Arial", 11),
            bg="#1e1e2e",
            fg="#bac2de"
        )
        range_label.pack(pady=5)


        input_frame = tk.Frame(self.root, bg="#1e1e2e")
        input_frame.pack(pady=30)

        input_label = tk.Label(
            input_frame,
            text="Your Guess:",
            font=("Arial", 13),
            bg="#1e1e2e",
            fg="#cdd6f4"
        )
        input_label.pack(side="left", padx=10)

        self.guess_entry = tk.Entry(
            input_frame,
            font=("Arial", 16),
            width=10,
            justify="center",
            bd=2,
            relief="solid"
        )
        self.guess_entry.pack(side="left", padx=10)
        self.guess_entry.bind("<Return>", lambda e: self.make_guess())
        self.guess_entry.focus()


        self.guess_button = tk.Button(
            self.root,
            text="Guess!",
            font=("Arial", 14, "bold"),
            bg="#89b4fa",
            fg="#1e1e2e",
            command=self.make_guess,
            cursor="hand2",
            width=12,
            height=2,
            bd=0
        )
        self.guess_button.pack(pady=10)


        self.feedback_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 15, "bold"),
            bg="#1e1e2e",
            fg="#fab387",
            wraplength=400,
            justify="center",
            height=3
        )
        self.feedback_label.pack(pady=20)

        new_game_btn = tk.Button(
            self.root,
            text="🔄 New Game",
            font=("Arial", 11),
            bg="#585b70",
            fg="#cdd6f4",
            command=self.create_welcome_screen,
            cursor="hand2",
            bd=0,
            padx=20,
            pady=8
        )
        new_game_btn.pack(pady=10)

    def check_answer(self, user_guess, actual_answer, turns):
        if user_guess == actual_answer:
            self.feedback_label.config(
                text=f"🎉 Your guess is Correct!\nI was thinking of {user_guess}",
                fg="#a6e3a1"
            )
            self.guess_entry.config(state="disabled")
            self.guess_button.config(state="disabled")
            messagebox.showinfo("Winner! 🎉", f"Congratulations!\nYou guessed the correct number: {user_guess}")
            return turns
        elif user_guess < actual_answer:
            self.feedback_label.config(
                text="📈 Too low!\nTry a higher number",
                fg="#fab387"
            )
            return turns - 1
        else:
            self.feedback_label.config(
                text="📉 Too high!\nTry a lower number",
                fg="#fab387"
            )
            return turns - 1

    def make_guess(self):
        if not self.game_started:
            return

        try:
            self.guess = int(self.guess_entry.get())

            if self.guess < 1 or self.guess > 100:
                self.feedback_label.config(
                    text="❌ Please enter a number\nbetween 1 and 100!",
                    fg="#f38ba8"
                )
                return

            self.turns = self.check_answer(self.guess, self.answer, self.turns)
            self.turns_label.config(text=f"You have {self.turns} turns left")


            if self.guess != self.answer and self.turns == 0:
                self.feedback_label.config(
                    text=f"😔 Game Over!\nThe number was {self.answer}",
                    fg="#f38ba8"
                )
                self.guess_entry.config(state="disabled")
                self.guess_button.config(state="disabled")
                messagebox.showinfo("Game Over", f"You've run out of turns!\nThe correct number was {self.answer}")

            self.guess_entry.delete(0, tk.END)

        except ValueError:
            self.feedback_label.config(
                text="❌ Invalid input!\nPlease enter a valid number",
                fg="#f38ba8"
            )

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()