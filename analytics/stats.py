import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from database.db_manager import DBManager
from analytics.report import export_pdf
from core.style import *


def show_stats(username):
    db = DBManager()
    data = db.get_user_stats(username)

    if not data:
        messagebox.showinfo("No Data", "No scores found!")
        return

    # -------- DATA PROCESSING --------
    df = pd.DataFrame(data, columns=["Game", "Score"])

    scores = np.array(df["Score"])
    avg_score = np.mean(scores)
    max_score = np.max(scores)
    min_score = np.min(scores)

    # -------- WINDOW --------
    win = tk.Toplevel()
    win.title("📊 Analytics Dashboard")
    win.geometry("450x600")
    win.configure(bg=BG_COLOR)

    # -------- TITLE --------
    tk.Label(win, text=f"{username}'s Stats",
             font=FONT_TITLE, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

    # -------- BASIC STATS --------
    tk.Label(win, text=f"Average Score: {avg_score:.2f}",
             bg=BG_COLOR, fg="white", font=FONT_NORMAL).pack()

    tk.Label(win, text=f"Max Score: {max_score}",
             bg=BG_COLOR, fg="white", font=FONT_NORMAL).pack()

    tk.Label(win, text=f"Min Score: {min_score}",
             bg=BG_COLOR, fg="white", font=FONT_NORMAL).pack()

    # -------- LISTBOX --------
    frame = tk.Frame(win, bg=BG_COLOR)
    frame.pack(pady=10)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(frame, width=40, height=10,
                         yscrollcommand=scrollbar.set)
    listbox.pack()

    scrollbar.config(command=listbox.yview)

    for g, s in data:
        listbox.insert(tk.END, f"{g} → {s}")

    # -------- FUNCTIONS --------
    def show_graph():
        plt.figure()
        plt.bar(df["Game"], df["Score"])
        plt.title("Game Scores")
        plt.xlabel("Game")
        plt.ylabel("Score")
        plt.grid()
        plt.show()

    def compare_games():
        sorted_df = df.sort_values(by="Score", ascending=False)

        plt.figure()
        plt.plot(sorted_df["Game"], sorted_df["Score"], marker='o')
        plt.title("Game Comparison")
        plt.xlabel("Game")
        plt.ylabel("Score")
        plt.grid()
        plt.show()

    def export_csv():
        path = filedialog.asksaveasfilename(defaultextension=".csv")
        if path:
            df.to_csv(path, index=False)
            messagebox.showinfo("Saved", "CSV exported successfully!")

    # -------- BUTTONS --------
    tk.Button(win, text="Show Graph",
              command=show_graph,
              bg=BTN_COLOR, fg="white",
              font=FONT_BTN, width=20).pack(pady=5)

    tk.Button(win, text="Compare Games",
              command=compare_games,
              bg="#9c27b0", fg="white",
              font=FONT_BTN, width=20).pack(pady=5)

    tk.Button(win, text="Export CSV",
              command=export_csv,
              bg="#f44336", fg="white",
              font=FONT_BTN, width=20).pack(pady=5)

    tk.Button(win, text="Export PDF",
              command=lambda: export_pdf(username),
              bg="#795548", fg="white",
              font=FONT_BTN, width=20).pack(pady=5)
