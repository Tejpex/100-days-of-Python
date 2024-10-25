class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        text = self.question_list[self.question_number].text
        correct = self.question_list[self.question_number].answer
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {text} (True/False): ").lower()
        self.check_answer(correct, answer)

    def check_answer(self, correct, answer):
        if answer == correct.lower():
            self.score += 1
            print("You are right.")
        else:
            print(f"Sorry. The correct answer was {correct.lower()}.")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")
