import tkinter as tk
from core.engine import GameEngine
from core.style import *

from games.snake import SnakeGame
from games.tictactoe import TicTacToeGame
from games.dice import DiceGame
from games.memory import MemoryGame
from games.quiz import QuizGame

from analytics.stats import show_stats


def open_dashboard(username):
    engine = GameEngine()

    # -------- REGISTER GAMES --------
    engine.register_game("Snake", SnakeGame(username))
    engine.register_game("TicTacToe", TicTacToeGame(username))
    engine.register_game("Dice", DiceGame(username))
    engine.register_game("Memory", MemoryGame(username))
    engine.register_game("Quiz", QuizGame(username))

    root = tk.Tk()
    root.title("Arcade Arena Dashboard")
    root.geometry("500x600")
    root.configure(bg=BG_COLOR)

    # -------- TITLE --------
    tk.Label(root, text="🎮 Arcade Arena",
             font=FONT_TITLE,
             bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=20)

    # -------- USER --------
    tk.Label(root, text=f"Welcome, {username}",
             font=FONT_NORMAL,
             bg=BG_COLOR, fg="lightgray").pack(pady=5)

    frame = tk.Frame(root, bg=BG_COLOR)
    frame.pack(pady=20)

    def launch(game):
        root.destroy()
        engine.launch(game)

    def btn(text, game):
        return tk.Button(frame, text=text,
                         command=lambda: launch(game),
                         bg=BTN_COLOR, fg="white",
                         font=FONT_BTN,
                         width=20, height=2, bd=0)

    # -------- GAME BUTTONS --------
    btn("🐍 Snake", "Snake").pack(pady=6)
    btn("❌ Tic Tac Toe", "TicTacToe").pack(pady=6)
    btn("🎲 Dice", "Dice").pack(pady=6)
    btn("🧠 Memory", "Memory").pack(pady=6)
    btn("❓ Quiz", "Quiz").pack(pady=6)

    # -------- ANALYTICS --------
    tk.Button(root, text="📊 Analytics",
              command=lambda: show_stats(username),
              bg=ACCENT, fg="white",
              font=FONT_BTN,
              width=20, height=2).pack(pady=10)

    # -------- LOGOUT --------
    tk.Button(root, text="🚪 Logout",
              command=root.quit,
              bg="#f44336", fg="white",
              font=FONT_BTN,
              width=20, height=2).pack(pady=10)

    root.mainloop()
