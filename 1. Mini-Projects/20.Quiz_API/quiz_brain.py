import html  # HTML 엔티티(예: &quot;, &amp;)를 일반 문자로 변환하기 위해 사용


class QuizBrain:
    """
    퀴즈 게임의 핵심 로직을 담당하는 클래스
    """

    def __init__(self, q_list):
        """
        생성자 메서드 (객체가 생성될 때 실행됨)

        :param q_list: Question 객체들이 담긴 리스트 (퀴즈 문제 리스트)
        """
        self.question_number = 0  # 현재 문제 번호 (0부터 시작)
        self.score = 0  # 사용자의 점수 초기화
        self.question_list = q_list  # 퀴즈 문제 리스트 저장
        self.current_question = None  # 현재 진행 중인 문제 (초기값: None)

    def still_has_questions(self):
        """
        퀴즈가 끝났는지 확인하는 메서드

        :return: 남은 문제가 있으면 True, 없으면 False 반환
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        다음 문제를 가져오는 메서드

        :return: 현재 문제의 번호와 문제 텍스트를 문자열로 반환
        """
        self.current_question = self.question_list[self.question_number]  # 현재 문제 설정
        self.question_number += 1  # 문제 번호 증가
        q_text = html.unescape(self.current_question.text)  # HTML 엔티티를 일반 텍스트로 변환
        return f"Q.{self.question_number}: {q_text}"  # 문제 출력 형식 지정

    def check_answer(self, user_answer):
        """
        사용자의 답을 확인하는 메서드

        :param user_answer: 사용
        """
