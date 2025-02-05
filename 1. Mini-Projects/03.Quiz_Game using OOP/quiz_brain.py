class QuizBrain:

    def __init__(self, q_list):
        # 클래스 초기화 메서드
        self.question_number = 0  # 현재 질문 번호 초기화
        self.score = 0  # 점수 초기화
        self.question_list = q_list  # 질문 리스트 저장

    def still_has_questions(self):
        # 남아 있는 질문이 있는지 확인하는 메서드
        return self.question_number < len(self.question_list)  # 질문 번호가 리스트 길이보다 작으면 True 반환

    def next_question(self):
        # 다음 질문을 가져오고 사용자에게 질문하는 메서드
        current_question = self.question_list[self.question_number]  # 현재 질문 가져오기
        self.question_number += 1  # 질문 번호 증가
        # 사용자 입력 요청 (True/False)
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # 사용자 답과 정답 비교
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        # 사용자의 답변이 정답과 일치하는지 확인하는 메서드
        if user_answer.lower() == correct_answer.lower():  # 대소문자 구분 없이 비교
            self.score += 1  # 정답이면 점수 증가
            print("You got it right!")  # 정답 메시지 출력
        else:
            print("That's wrong.")  # 오답 메시지 출력
        # 정답과 현재 점수 출력
        print(f"The correct answer was: {correct_answer}.")  # 정답 출력
        print(f"Your current score is: {self.score}/{self.question_number}")  # 현재 점수 출력
        print("\n")  # 줄바꿈으로 출력 정리
