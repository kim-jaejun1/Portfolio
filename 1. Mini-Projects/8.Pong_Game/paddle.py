from turtle import Turtle

class Paddle(Turtle):
    # Paddle 클래스는 Turtle 클래스를 상속받아 패들 객체를 생성합니다.

    def __init__(self, position):
        super().__init__()  # 부모 클래스(Turtle)의 초기화 메서드를 호출
        self.shape("square")  # 패들의 모양을 사각형으로 설정
        self.color("white")  # 패들의 색상을 흰색으로 설정
        self.shapesize(stretch_wid=5, stretch_len=1)
        # 패들의 크기를 길게 설정 (높이 5배, 너비 1배)
        self.penup()  # 패들이 이동할 때 선을 그리지 않도록 설정
        self.goto(position)  # 패들의 초기 위치를 설정

    def go_up(self):
        # 패들을 위로 이동시키는 메서드
        new_y = self.ycor() + 20  # 현재 y좌표에 20을 더하여 새로운 y좌표 계산
        self.goto(self.xcor(), new_y)  # x좌표는 유지하고 새로운 y좌표로 이동

    def go_down(self):
        # 패들을 아래로 이동시키는 메서드
        new_y = self.ycor() - 20  # 현재 y좌표에서 20을 빼서 새로운 y좌표 계산
        self.goto(self.xcor(), new_y)  # x좌표는 유지하고 새로운 y좌표로 이동
