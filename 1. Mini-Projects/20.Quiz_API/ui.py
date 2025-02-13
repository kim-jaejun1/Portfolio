from tkinter import *  # Tkinter 라이브러리를 가져와 GUI를 생성
from quiz_brain import QuizBrain  # 퀴즈 로직을 담당하는 QuizBrain 클래스를 가져옴

# 테마 색상 설정 (배경 색상)
THEME_COLOR = "#375362"


class QuizInterface:
    """
    퀴즈 애플리케이션의 GUI를 구성하는 클래스
    """

    def __init__(self, quiz_brain: QuizBrain):
        """
        생성자 메서드: 퀴즈 UI를 초기화하고 설정하는 역할

        :param quiz_brain: QuizBrain 객체 (퀴즈 데이터를 관리하는 클래스)
        """
        self.quiz = quiz_brain  # QuizBrain 인스턴스를 저장

        # 창(Window) 생성 및 설정
        self.window = Tk()
        self.window.title("Quizzler")  # 창 제목 설정
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)  # 여백 및 배경색 설정

        # 점수(Label) 설정
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)  # 점수 표시
        self.score_label.grid(row=0, column=1)  # 위치 지정 (행 0, 열 1)

        # 질문을 표시할 캔버스(Canvas) 생성
        self.canvas = Canvas(width=300, height=250, bg="white")  # 캔버스 크기 및 배경색 설정
        self.question_text = self.canvas.create_text(
            150, 125,  # 캔버스 중앙에 텍스트 배치
            width=280,  # 텍스트 줄 바꿈을 위한 너비 설정
            text="Some Question Text",  # 초기 텍스트 설정
            fill=THEME_COLOR,  # 글자 색상
            font=("Arial", 20, "italic")  # 글꼴 설정
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)  # 위치 및 여백 설정

        # "True" 버튼 생성 및 설정
        true_image = PhotoImage(file="images/true.png")  # True 버튼 이미지 불러오기
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)  # 위치 지정

        # "False" 버튼 생성 및 설정
        false_image = PhotoImage(file="images/false.png")  # False 버튼 이미지 불러오기
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)  # 위치 지정

        # 첫 번째 문제 불러오기
        self.get_next_question()

        # 창 실행 (이벤트 루프 시작)
        self.window.mainloop()

    def get_next_question(self):
        """
        다음 문제를 불러오는 메서드
        """
        self.canvas.config(bg="white")  # 배경색을 흰색으로 초기화
        if self.quiz.still_has_questions():  # 남은 문제가 있는 경우
            self.score_label.config(text=f"Score: {self.quiz.score}")  # 점수 업데이트
            q_text = self.quiz.next_question()  # 다음 문제 가져오기
            self.canvas.itemconfig(self.question_text, text=q_text)  # 캔버스의 질문 텍스트 업데이트
        else:  # 모든 문제가 끝난 경우
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")  # 종료 메시지 표시
            self.true_button.config(state="disabled")  # True 버튼 비활성화
            self.false_button.config(state="disabled")  # False 버튼 비활성화

    def true_pressed(self):
        """
        "True" 버튼이 눌렸을 때 실행되는 메서드
        """
        self.give_feedback(self.quiz.check_answer("True"))  # 사용자의 답을 체크하고 피드백 제공

    def false_pressed(self):
        """
        "False" 버튼이 눌렸을 때 실행되는 메서드
        """
        is_right = self.quiz.check_answer("False")  # 정답 확인
        self.give_feedback(is_right)  # 피드백 제공

    def give_feedback(self, is_right):
        """
        사용자의 정답 여부에 따라 피드백을 제공하는 메서드

        :param is_right: 정답 여부 (True 또는 False)
        """
        if is_right:
            self.canvas.config(bg="green")  # 정답일 경우 배경을 초록색으로 변경
        else:
            self.canvas.config(bg="red")  # 오답일 경우 배경을 빨간색으로 변경
        self.window.after(1000, self.get_next_question)  # 1초 후 다음 문제로 넘어감
