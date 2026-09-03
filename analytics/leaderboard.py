import tkinter as tk
from database.db_manager import DBManager
from core.style import *


def show_leaderboard():
    db = DBManager()
    data = db.get_leaderboard()

    win = tk.Toplevel()
    win.title("🏆 Leaderboard")
    win.geometry("400x500")
    win.configure(bg=BG_COLOR)

    # -------- TITLE --------
    tk.Label(win, text="🏆 Leaderboard",
             font=FONT_TITLE,
             bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

    # -------- LISTBOX --------
    frame = tk.Frame(win, bg=BG_COLOR)
    frame.pack(pady=10)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(frame,
                         width=40,
                         height=15,
                         font=FONT_NORMAL,
                         yscrollcommand=scrollbar.set)
    listbox.pack()

    scrollbar.config(command=listbox.yview)

    # -------- DATA --------
    if not data:
        listbox.insert(tk.END, "No data available")
        return

    # Sort by score (highest first)
    data = sorted(data, key=lambda x: x[2], reverse=True)

    for i, (user, game, score) in enumerate(data, start=1):
        listbox.insert(tk.END, f"{i}. {user} | {game} | Score: {score}")

    # -------- CLOSE BUTTON --------
    tk.Button(win, text="Close",
              command=win.destroy,
              bg="#f44336", fg="white",
              font=FONT_BTN, width=15).pack(pady=10)
