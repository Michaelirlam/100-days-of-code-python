from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
game_over = False

for question in question_data:
    question_object = Question(question["text"], question["answer"])
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score was {quiz.score}/{len(quiz.question_list)}")

