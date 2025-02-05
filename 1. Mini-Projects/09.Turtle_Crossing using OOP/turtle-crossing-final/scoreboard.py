from turtle import Turtle

# 점수판의 글꼴 설정
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """ 점수판을 관리하는 클래스 """

    def __init__(self):
        """ 점수판 객체 초기화 """
        super().__init__()
        self.level = 1  # 초기 레벨 설정
        self.hideturtle()  # 거북이 커서를 숨김
        self.penup()  # 펜을 올려서 선이 그려지지 않도록 설정
        self.goto(-280, 250)  # 화면 왼쪽 상단에 위치 설정
        self.update_scoreboard()  # 점수판 초기 출력

    def update_scoreboard(self):
        """ 현재 레벨을 화면에 표시 """
        self.clear()  # 이전 텍스트를 지우고 업데이트
        self.write(f"Level: {self.level}", align="left", font=FONT)  # 레벨 표시

    def increase_level(self):
        """ 레벨 증가 및 점수판 업데이트 """
        self.level += 1  # 레벨 1 증가
        self.update_scoreboard()  # 변경된 레벨을 화면에 업데이트

    def game_over(self):
        """ 게임 종료 메시지 출력 """
        self.goto(0, 0)  # 화면 중앙으로 이동
        self.write(f"GAME OVER", align="center", font=FONT)  # "GAME OVER" 표시
