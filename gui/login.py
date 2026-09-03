import tkinter as tk
from tkinter import messagebox
from gui.dashboard import open_dashboard
from auth.auth import login_user, register_user
from core.style import *


def login_screen():
    root = tk.Tk()
    root.title("🎮 Arcade Arena Login")
    root.geometry("500x450")
    root.configure(bg=BG_COLOR)

    # -------- CARD FRAME --------
    frame = tk.Frame(root, bg=CARD_COLOR, padx=30, pady=30)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # -------- TITLE --------
    tk.Label(frame, text="🎮 Arcade Arena",
             font=FONT_TITLE,
             bg=CARD_COLOR, fg=TEXT_COLOR).pack(pady=10)

    # -------- USERNAME --------
    tk.Label(frame, text="Username",
             font=FONT_NORMAL,
             bg=CARD_COLOR, fg="lightgray").pack(pady=5)

    username = tk.Entry(frame,
                        font=("Arial", 14),
                        width=22,
                        justify="center")
    username.pack(pady=8)

    # -------- PASSWORD --------
    tk.Label(frame, text="Password",
             font=FONT_NORMAL,
             bg=CARD_COLOR, fg="lightgray").pack(pady=5)

    password = tk.Entry(frame,
                        font=("Arial", 14),
                        width=22,
                        justify="center",
                        show="*")
    password.pack(pady=8)

    # -------- FUNCTIONS --------
    def login():
        user = username.get()
        pwd = password.get()

        success, message = login_user(user, pwd)

        if success:
            messagebox.showinfo("Success", message)
            root.destroy()
            open_dashboard(user)
        else:
            messagebox.showerror("Error", message)

    def register():
        user = username.get()
        pwd = password.get()

        success, message = register_user(user, pwd)

        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

    # -------- BUTTONS --------
    tk.Button(frame, text="Login",
              command=login,
              bg=BTN_COLOR, fg="white",
              font=FONT_BTN,
              width=18, height=2).pack(pady=10)

    tk.Button(frame, text="Register",
              command=register,
              bg="#3f51b5", fg="white",
              font=FONT_BTN,
              width=18, height=2).pack(pady=5)

    # -------- FOOTER --------
    tk.Label(frame,
             text="Enter credentials to continue",
             font=("Arial", 9),
             bg=CARD_COLOR,
             fg="gray").pack(pady=10)

    root.mainloop()
