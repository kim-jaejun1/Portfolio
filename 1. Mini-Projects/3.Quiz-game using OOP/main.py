# 필요한 클래스와 데이터 가져오기
from question_model import Question  # Question 클래스 정의를 가져옴
from data import question_data  # 퀴즈 데이터를 포함한 question_data 가져옴
from quiz_brain import QuizBrain  # 퀴즈 진행 로직을 포함한 QuizBrain 클래스 가져옴

# 빈 리스트 생성: 퀴즈 문항(Question 객체)을 저장하기 위한 리스트
question_bank = []

# question_data를 순회하며 Question 객체 생성 및 리스트에 추가
for question in question_data:
    question_text = question["question"]  # 질문 텍스트 가져오기
    question_answer = question["correct_answer"]  # 정답 텍스트 가져오기
    new_question = Question(question_text, question_answer)  # Question 객체 생성
    question_bank.append(new_question)  # 리스트에 추가

# QuizBrain 객체 생성: 퀴즈 진행에 필요한 로직 관리
quiz = QuizBrain(question_bank)

# 퀴즈가 끝날 때까지 반복 진행
while quiz.still_has_questions():  # 남아있는 질문이 있는지 확인
    quiz.next_question()  # 다음 질문 출력 및 정답 확인

# 퀴즈 완료 메시지 출력
print("You've completed the quiz")  # 퀴즈 종료 메시지
# 최종 점수 출력
print(f"Your final score was: {quiz.score}/{quiz.question_number}")  # 점수와 질문 수 출력
