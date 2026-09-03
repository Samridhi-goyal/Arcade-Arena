import tkinter as tk
from tkinter import messagebox
from core.style import *
from core.sound import play_click, play_win


class TicTacToeGame:
    def __init__(self, username):
        self.username = username
        self.turn = "X"
        self.board = [""] * 9

    # Check winner
    def check_winner(self):
        combos = [(0,1,2),(3,4,5),(6,7,8),
                  (0,3,6),(1,4,7),(2,5,8),
                  (0,4,8),(2,4,6)]
        for a, b, c in combos:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return self.board[a]
        return None

    # Check draw
    def is_draw(self):
        return "" not in self.board

    def start(self):
        root = tk.Tk()
        root.title("Tic Tac Toe")
        root.configure(bg=BG_COLOR)

        buttons = []

        def click(i):
            if self.board[i] == "":
                play_click()
                self.board[i] = self.turn
                buttons[i].config(text=self.turn)

                winner = self.check_winner()

                if winner:
                    play_win()
                    messagebox.showinfo("Win", f"{winner} wins!")
                    root.destroy()
                    return

                elif self.is_draw():   # ✅ DRAW FIX
                    messagebox.showinfo("Draw", "It's a draw!")
                    root.destroy()
                    return

                # Switch turn
                self.turn = "O" if self.turn == "X" else "X"

        # Create grid
        for i in range(9):
            btn = tk.Button(root, text="",
                            font=("Arial", 24),
                            width=5, height=2,
                            bg="#2e2e3f", fg="white",
                            command=lambda i=i: click(i))
            btn.grid(row=i//3, column=i%3)
            buttons.append(btn)

        root.mainloop()
