import tkinter as tk
import random
from tkinter import messagebox
from core.style import *
from core.sound import play_win


class MemoryGame:
    def __init__(self, username):
        self.username = username

    def start(self):
        root = tk.Tk()
        root.title("Memory Game")
        root.configure(bg=BG_COLOR)

        cards = list("AABBCCDD")
        random.shuffle(cards)

        buttons = []
        first = [None]
        matched = [False] * 8   # ✅ track matched cards

        def click(i):
            if buttons[i]["text"] != "" or matched[i]:
                return

            buttons[i].config(text=cards[i])

            if first[0] is None:
                first[0] = i
            else:
                first_index = first[0]   # ✅ store safely

                if cards[i] != cards[first_index]:
                    root.after(500, lambda:
                        (buttons[i].config(text=""),
                         buttons[first_index].config(text="")))
                else:
                    matched[i] = True
                    matched[first_index] = True

                first[0] = None

                # ✅ CHECK WIN
                if all(matched):
                    play_win()
                    messagebox.showinfo("Victory", "You won!")
                    root.destroy()

        for i in range(8):
            btn = tk.Button(root, text="",
                            width=5, height=2,
                            bg="#2e2e3f", fg="white",
                            font=("Arial", 12),
                            command=lambda i=i: click(i))
            btn.grid(row=i//4, column=i%4, padx=5, pady=5)
            buttons.append(btn)

        root.mainloop()
