# Question
class Question:
    def __init__(self, text, choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        return self.answer == answer

# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionsIndex = 0

    def getQuestion(self):
        return self.questions[self.questionsIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionsIndex + 1}: {question.text}')

        for q in question.choices:
            print("-"+q)

        answer = input("cevap: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionsIndex += 1

        self.displayQuestion()

    def loadQuestion(self):
        if len(self.questions) == self.questionsIndex:
            self.showScore()
        else:
            self.displayQuestion()

    def showScore(self):
        print("score: ", self.score)

q1 = Question("En iyi programlama dili hangisidir?",["C#","Python","Javascript","Java"],"Python")
q2 = Question("En popüler programlama dili hangisidir?",["Python","Javascript","C#","Java"],"Python")
q3 = Question("En çok kazandıran programlama dili hangisidir?",["C#","Javascript","Java","Python"],"Python")
questions = [q1,q2,q3]

quiz = Quiz(questions)
quiz.displayQuestion()
