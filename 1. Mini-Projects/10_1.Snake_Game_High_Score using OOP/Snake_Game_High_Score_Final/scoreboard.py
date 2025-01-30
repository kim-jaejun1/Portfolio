from turtle import Turtle  # 터틀 그래픽을 위한 Turtle 클래스 가져오기

# 점수판 텍스트 정렬 및 폰트 설정
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Snake 게임의 점수를 표시하고 관리하는 클래스."""

    def __init__(self):
        """Scoreboard 객체 초기화 메서드.

        점수를 0으로 설정하고, `data.txt`에서 최고 점수를 불러온 후,
        화면 상단에 점수판을 표시한다.
        """
        super().__init__()  # 부모 클래스(Turtle) 초기화
        self.score = 0  # 현재 점수 초기화

        # 최고 점수 불러오기 (파일에서 저장된 점수 읽기)
        with open("data.txt") as data:
            self.high_score = int(data.read())  # 최고 점수를 정수로 변환하여 저장

        self.color("white")  # 글자 색상을 흰색으로 설정
        self.penup()  # 선 없이 이동하도록 설정
        self.goto(0, 270)  # 점수판을 화면 상단에 배치
        self.hideturtle()  # 터틀 커서 숨기기
        self.update_scoreboard()  # 점수판 업데이트

    def update_scoreboard(self):
        """현재 점수와 최고 점수를 화면에 표시하는 메서드."""
        self.clear()  # 기존 점수 삭제 후 업데이트
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """게임이 끝났을 때 최고 점수를 갱신하고, 현재 점수를 초기화하는 메서드."""
        if self.score > self.high_score:  # 현재 점수가 최고 점수보다 크다면
            self.high_score = self.score  # 최고 점수 갱신
            with open("data.txt", mode="w") as data:  # 새 최고 점수를 파일에 저장
                data.write(f"{self.high_score}")
        self.score = 0  # 현재 점수 초기화
        self.update_scoreboard()  # 점수판 업데이트

    def increase_score(self):
        """점수를 1 증가시키고 점수판을 업데이트하는 메서드."""
        self.score += 1  # 점수 증가
        self.update_scoreboard()  # 점수판 업데이트
