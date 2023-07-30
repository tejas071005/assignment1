import tkinter as tk
from random import randint
import time

class DiceRollSimulator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Dice Rolling Simulator")
        self.geometry("300x150")

        self.result_label = tk.Label(self, text="", font=("Helvetica", 48))
        self.result_label.pack(pady=20)

        self.roll_button = tk.Button(self, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack()

    def roll_dice(self):
        # Disable the button while rolling
        self.roll_button.config(state=tk.DISABLED)

        # Simulate rolling a dice for a few times
        rolls = 15
        for _ in range(rolls):
            result = randint(1, 6)
            self.result_label.config(text=str(result))
            self.update()
            time.sleep(0.1)  # Add a small delay for the animation effect

        # Enable the button after the rolling animation is finished
        self.roll_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    app = DiceRollSimulator()
    app.mainloop()
