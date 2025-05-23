from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FRENCH_TEXT = "#000000"
ENGLISH_TEXT = "#ffffff"

window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title("Flashy")


# |----------------------------- DATA ------------------------------|

try:
    french_data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    french_data = pandas.read_csv("./data/french_words.csv")
    french_data.to_csv("./data/words_to_learn.csv")
    french_data = pandas.read_csv("./data/words_to_learn.csv")
finally:
    french_dict = french_data.to_dict(orient="records")

# |---------------------------- CARD LOGIC -------------------------------|

flip_timer = None
new_word = {}

def next_card():
    global new_word, flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    if len(french_dict) == 0:
        card_canvas.itemconfig(word, text="All done!", fill=FRENCH_TEXT)
        card_canvas.itemconfig(title, text="", fill=FRENCH_TEXT)
        return
    new_word = random.choice(french_dict)
    card_canvas.itemconfig(word, text=new_word["French"], fill=FRENCH_TEXT)
    card_canvas.itemconfig(title, text="French", fill=FRENCH_TEXT)
    card_canvas.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global new_word
    card_canvas.itemconfig(card_background, image=back_image)
    card_canvas.itemconfig(word, text=new_word["English"], fill=ENGLISH_TEXT)
    card_canvas.itemconfig(title, text="English", fill=ENGLISH_TEXT)

def is_known():
    french_dict.remove(new_word)
    data = pandas.DataFrame(french_dict)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

# |------------------------------ UI ------------------------------|

# Images
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")


# Canvas
card_canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_background =  card_canvas.create_image(400, 263, image=front_image)
card_canvas.grid(column=0, row=0, columnspan=3, pady=20)
title = card_canvas.create_text(400, 120, text="Title", font=("Arial", 40, "italic"))
word = card_canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

# Buttons
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
right_button.grid(column=2, row=1)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()