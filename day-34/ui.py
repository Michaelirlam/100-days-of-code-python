from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")

        self.score = self.quiz_brain.score

        self.score_text = Label(text=f"Score: {self.score}", background=THEME_COLOR, font=("Arial", 11, "normal"), fg="white")
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, background="#ffffff")
        self.question_text = self.canvas.create_text(150, 125, text="If this text appears my code isnt working", font=("Arial", 20, "italic"), width=280)
        self.true = Button(image=true_image, highlightthickness=0, command=self.check_answer_true)
        self.false = Button(image=false_image, highlightthickness=0, command=self.check_answer_false)

        self.score_text.grid(column=1, row=0, pady=10)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=10)
        self.true.grid(column=0, row=2, pady=10)
        self.false.grid(column=1, row=2, pady=10)

        self.get_next_question()
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your final score is {self.score} / 10")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def check_answer_true(self):
        self.give_feedback("true")

    def check_answer_false(self):
        self.give_feedback("false")

    def give_feedback(self, answer):
        if self.quiz_brain.check_answer(answer):
            self.canvas.itemconfig(self.question_text, text="Correct!")
            self.canvas.config(background="green")
            self.score += 1
            self.score_text.config(text=f"Score: {self.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="Wrong answer!")
            self.canvas.config(background="red")
        self.next_question = self.window.after(1000, self.get_next_question)