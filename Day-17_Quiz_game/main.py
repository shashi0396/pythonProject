from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# write a for loop to iterate over question_data.
# create a Question object from each entry in question_data
# append each question object to the question bank

question_bank = []

for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_q = Question(b_text=q_text, b_answer=q_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"your final score was:{quiz.score}/{quiz.question_number}")