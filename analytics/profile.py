import tkinter as tk
from database.db_manager import DBManager
from core.style import *


def show_profile(username):
    db = DBManager()
    data = db.get_user_stats(username)

    win = tk.Toplevel()
    win.title("👤 Profile")
    win.geometry("350x400")
    win.configure(bg=BG_COLOR)

    # -------- TITLE --------
    tk.Label(win, text=f"{username}'s Profile",
             font=FONT_TITLE,
             bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

    # -------- DATA --------
    if not data:
        tk.Label(win, text="No data available",
                 bg=BG_COLOR, fg="white",
                 font=FONT_NORMAL).pack(pady=10)
        return

    # -------- LISTBOX --------
    frame = tk.Frame(win, bg=BG_COLOR)
    frame.pack(pady=10)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(frame,
                         width=35,
                         height=12,
                         font=FONT_NORMAL,
                         yscrollcommand=scrollbar.set)
    listbox.pack()

    scrollbar.config(command=listbox.yview)

    for game, score in data:
        listbox.insert(tk.END, f"{game} → Score: {score}")

    # -------- CLOSE BUTTON --------
    tk.Button(win, text="Close",
              command=win.destroy,
              bg="#f44336", fg="white",
              font=FONT_BTN, width=15).pack(pady=10)
