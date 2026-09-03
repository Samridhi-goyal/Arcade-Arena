import pygame
import os

# Initialize mixer safely
try:
    pygame.mixer.init()
except Exception as e:
    print("Sound system not available")

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def load_sound(filename):
    path = os.path.join(BASE_DIR, "assets", filename)

    if not os.path.exists(path):
        print(f"Sound file missing: {path}")
        return None

    try:
        return pygame.mixer.Sound(path)
    except Exception:
        print(f"Error loading sound: {path}")
        return None


# Load sounds
click = load_sound("click.wav")
win = load_sound("win.wav")
lose = load_sound("lose.wav")


# Play functions
def play_click():
    if click:
        click.play()


def play_win():
    if win:
        win.play()


def play_lose():
    if lose:
        lose.play()
