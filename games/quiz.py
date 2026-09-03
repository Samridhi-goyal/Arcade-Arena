import tkinter as tk
from tkinter import messagebox
from core.style import *


class QuizGame:
    def __init__(self, username):
        self.username = username
        self.q_index = 0
        self.score = 0

        self.questions = [
            ("Capital of India?", ["Delhi", "Mumbai", "Chennai"], "Delhi"),
            ("2+2?", ["3", "4", "5"], "4")
        ]

    def start(self):
        root = tk.Tk()
        root.title("Quiz Game")
        root.geometry("400x400")
        root.configure(bg=BG_COLOR)

        # 🧠 Question label
        q_label = tk.Label(root,
                           font=("Arial", 14, "bold"),
                           wraplength=300,
                           bg=BG_COLOR, fg="white")
        q_label.pack(pady=30)

        # 🎯 Button frame
        btn_frame = tk.Frame(root, bg=BG_COLOR)
        btn_frame.pack()

        buttons = []

        def load():
            if self.q_index >= len(self.questions):
                show_result()
                return

            q, options, ans = self.questions[self.q_index]
            q_label.config(text=q)

            for i, opt in enumerate(options):
                buttons[i].config(text=opt,
                                  command=lambda o=opt: check(o))

        def check(choice):
            q, options, ans = self.questions[self.q_index]
            if choice == ans:
                self.score += 1
            self.q_index += 1
            load()

        # ✅ RESULT SCREEN (FIXED UI)
        def show_result():
            q_label.config(text=f"🎉 Your Score: {self.score}/{len(self.questions)}")

            # ❌ Hide buttons
            for btn in buttons:
                btn.pack_forget()

            # ✅ Play again option
            again = tk.Button(root,
                              text="Play Again",
                              bg=BTN_COLOR, fg="white",
                              font=FONT_BTN,
                              command=lambda: restart(root))
            again.pack(pady=10)

            # Exit button
            tk.Button(root,
                      text="Exit",
                      bg="#f44336", fg="white",
                      font=FONT_BTN,
                      command=root.destroy).pack(pady=5)

        def restart(win):
            win.destroy()
            QuizGame(self.username).start()

        # Create buttons
        for _ in range(3):
            btn = tk.Button(btn_frame,
                            bg=BTN_COLOR, fg="white",
                            font=FONT_BTN,
                            width=20)
            btn.pack(pady=5)
            buttons.append(btn)

        load()
        root.mainloop()
