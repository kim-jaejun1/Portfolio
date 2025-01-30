from turtle import Turtle  # 터틀 그래픽을 위한 Turtle 클래스 가져오기

# 점수판 텍스트 정렬 및 폰트 설정
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Snake 게임의 점수를 표시하고 관리하는 클래스."""

    def __init__(self):
        """Scoreboard 객체 초기화 메서드.

        점수를 0으로 설정하고, 화면 상단에 점수판을 표시한다.
        """
        super().__init__()  # 부모 클래스(Turtle) 초기화
        self.score = 0  # 현재 점수 초기화
        self.color("white")  # 글자 색상을 흰색으로 설정
        self.penup()  # 선 없이 이동하도록 설정
        self.goto(0, 270)  # 점수판을 화면 상단에 배치
        self.hideturtle()  # 터틀 커서 숨기기
        self.update_scoreboard()  # 점수판 업데이트

    def update_scoreboard(self):
        """현재 점수를 화면에 표시하는 메서드."""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """게임 종료 시 'GAME OVER' 메시지를 화면에 표시하는 메서드."""
        self.goto(0, 0)  # 화면 중앙으로 이동
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)  # 게임 종료 메시지 출력

    def increase_score(self):
        """점수를 1 증가시키고 점수판을 업데이트하는 메서드."""
        self.score += 1  # 점수 증가
        self.clear()  # 기존 점수 지우기
        self.update_scoreboard()  # 새로운 점수 표시
