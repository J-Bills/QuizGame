class QuizBrain:
    def __init__(self,question_list:list):
        self.question_number = 0
        self.question_list = question_list
        self.answers_correct = 0

    def check_answer(self, question, user_answer):
        if question.answer.lower() == user_answer.lower():
            self.answers_correct += 1
            print("You got it right")
        else:
            print("That's wrong")
        print(f"The correct answer is {question.answer.lower()}")
        print(f"Your current score is {self.answers_correct} / {len(self.question_list)}")
        print("\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = str(input(f"Q.{self.question_number} {current_question.text} '(TRUE or FALSE)?'"))
        self.check_answer(current_question, user_answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)


