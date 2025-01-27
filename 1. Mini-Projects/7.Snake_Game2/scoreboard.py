from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0  # 초기 점수를 0으로 설정한다.
        self.color("white")  # 점수판의 글자 색상을 흰색으로 설정한다.
        self.penup()  # 선을 그리지 않도록 설정한다.
        self.goto(0, 270)  # 점수판의 위치를 화면 위쪽 중앙에 설정한다.
        self.hideturtle()  # 거북이를 숨겨 점수판만 보이도록 한다.
        self.update_scoreboard()  # 점수판을 초기화한다.

    def update_scoreboard(self):
        # 점수를 화면에 표시한다.
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        # 게임 종료 메시지를 화면 중앙에 표시한다.
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        # 점수를 1 증가시키고 점수판을 업데이트한다.
        self.score += 1
        self.clear()  # 기존 점수를 지운다.
        self.update_scoreboard()