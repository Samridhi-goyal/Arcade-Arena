import tkinter as tk
import random
from core.style import *
from core.sound import play_click


class DiceGame:
    def __init__(self, username):
        self.username = username

    def start(self):
        root = tk.Tk()
        root.title("Dice Game")
        root.geometry("300x300")
        root.configure(bg=BG_COLOR)

        label = tk.Label(root, text="🎲",
                         font=("Arial", 50),
                         bg=BG_COLOR, fg="white")
        label.pack(pady=20)

        # ✅ RULE TEXT ADDED
        rule = tk.Label(root,
                        text="Roll > 4 to Win",
                        font=FONT_NORMAL,
                        bg=BG_COLOR, fg="lightgray")
        rule.pack()

        result = tk.Label(root, text="Roll the dice!",
                          font=FONT_NORMAL,
                          bg=BG_COLOR, fg="white")
        result.pack()

        def roll():
            play_click()
            num = random.randint(1, 6)
            label.config(text=str(num))

            if num > 4:
                result.config(text="You Win!")
            else:
                result.config(text="Try Again!")

        tk.Button(root, text="Roll",
                  command=roll,
                  bg=BTN_COLOR, fg="white",
                  font=FONT_BTN).pack(pady=20)

        root.mainloop()
