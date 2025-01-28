from turtle import Turtle

class Scoreboard(Turtle):
    # Scoreboard 클래스는 Turtle 클래스를 상속받아 점수판을 생성합니다.

    def __init__(self):
        super().__init__()  # 부모 클래스(Turtle)의 초기화 메서드를 호출
        self.color("white")  # 점수판의 색상을 흰색으로 설정
        self.penup()  # 선을 그리지 않도록 설정
        self.hideturtle()  # 점수판의 거북이 모양을 숨김
        self.l_score = 0  # 왼쪽 플레이어의 점수를 초기화
        self.r_score = 0  # 오른쪽 플레이어의 점수를 초기화
        self.update_scoreboard()  # 점수판을 초기화

    def update_scoreboard(self):
        # 화면에 점수를 업데이트하는 메서드
        self.clear()  # 이전 점수를 지움
        self.goto(-100, 200)  # 왼쪽 점수의 위치로 이동
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        # 왼쪽 플레이어의 점수를 출력
        self.goto(100, 200)  # 오른쪽 점수의 위치로 이동
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        # 오른쪽 플레이어의 점수를 출력

    def l_point(self):
        # 왼쪽 플레이어의 점수를 1 증가시키고 점수판을 업데이트
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        # 오른쪽 플레이어의 점수를 1 증가시키고 점수판을 업데이트
        self.r_score += 1
        self.update_scoreboard()
