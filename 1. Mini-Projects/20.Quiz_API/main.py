from question_model import Question  # Question 클래스를 가져옴 (퀴즈 문제 객체 생성에 사용)
from data import question_data  # 퀴즈 문제 데이터를 가져옴
from quiz_brain import QuizBrain  # 퀴즈 로직을 담당하는 QuizBrain 클래스 가져옴
from ui import QuizInterface  # 퀴즈 UI를 담당하는 QuizInterface 클래스 가져옴

# 퀴즈 문제를 저장할 리스트 생성
question_bank = []

# question_data 리스트에 있는 각 문제를 Question 객체로 변환하여 question_bank에 추가
for question in question_data:
    question_text = question["question"]  # 문제 텍스트 가져오기
    question_answer = question["correct_answer"]  # 정답 가져오기
    new_question = Question(question_text, question_answer)  # Question 객체 생성
    question_bank.append(new_question)  # 리스트에 추가

# QuizBrain 객체 생성 (퀴즈 진행을 담당)
quiz = QuizBrain(question_bank)

# QuizInterface 객체 생성 (퀴즈 UI를 담당)
quiz_ui = QuizInterface(quiz)
