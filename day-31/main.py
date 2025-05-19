from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.title("Flashy")


# |----------------------------- DATA ------------------------------|

french_data = pandas.read_csv("./data/french_words.csv")
french_dict = french_data.to_dict(orient="records")

french_word = french_dict[random.randint(1, 101)]["French"]

def next_card():
    new_word = french_dict[random.randint(1, 101)]["French"]
    return card_canvas.itemconfig(word, text=new_word)


# |------------------------------ UI ------------------------------|

# Images
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")


# Canvas
card_canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_canvas.create_image(400, 263, image=front_image)
card_canvas.grid(column=0, row=0, columnspan=3, pady=20)
title = card_canvas.create_text(400, 120, text="French", font=("Arial", 40, "italic"))
word = card_canvas.create_text(400, 263, text=french_word, font=("Arial", 60, "bold"))

# Buttons
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
right_button.grid(column=2, row=1)
wrong_button.grid(column=0, row=1)

window.mainloop()