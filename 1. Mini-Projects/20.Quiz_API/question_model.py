class Question:
    """
    퀴즈 문제를 저장하는 클래스
    """

    def __init__(self, q_text, q_answer):
        """
        생성자 메서드 (객체가 생성될 때 실행됨)

        :param q_text: 문제의 텍스트 (문제 내용)
        :param q_answer: 정답 (True/False 또는 문자열)
        """
        self.text = q_text  # 문제의 텍스트 저장
        self.answer = q_answer  # 정답 저장
