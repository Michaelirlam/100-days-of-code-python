from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(padx=50, pady=50)



# |------------------------------ UI ------------------------------|

# Images
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")


# Canvas
card_canvas = Canvas(width=800, height=526, highlightthickness=0)
card_canvas.create_image(400, 263, image=front_image)
card_canvas.grid(column=0, row=0, columnspan=3, pady=20)
title = card_canvas.create_text(400, 120, text="title", font=("Arial", 30, "bold"))
word = card_canvas.create_text(400, 263, text="word", font=("Arial", 26, "bold"))

# Buttons
right_button = Button(image=right_image, highlightthickness=0)
wrong_button = Button(image=wrong_image, highlightthickness=0)
right_button.grid(column=2, row=1)
wrong_button.grid(column=0, row=1)

window.mainloop()