class Question:

    def __init__(self, q_text, q_answer):
        # Question 클래스 초기화 메서드
        # q_text: 질문 텍스트
        # q_answer: 질문의 정답 (True/False)
        self.text = q_text  # 질문 텍스트를 저장
        self.answer = q_answer  # 정답을 저장
