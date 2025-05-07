from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#ffffff"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
ticks = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global reps
    global ticks
    global timer
    window.after_cancel(timer)
    reps = 0
    ticks = 1
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_time():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global ticks
    global timer
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    elif count == 0 and reps < 8:
        start_time()
        if reps % 2 == 0:
            check_label.config(text="✓"*ticks)
            ticks += 1

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

timer_label = Label(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

tomato_image = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_label.grid(column=1, row=3)

start_button = Button(text="Start", background=WHITE, command=start_time)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", background=WHITE, command=reset)
reset_button.grid(column=2, row=2)


window.mainloop()