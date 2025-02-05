from turtle import Turtle


class Ball(Turtle):
    # Ball 클래스는 Turtle 클래스를 상속받아 공 객체를 생성합니다.

    def __init__(self):
        super().__init__()  # 부모 클래스(Turtle)의 초기화 메서드를 호출
        self.color("white")  # 공의 색상을 흰색으로 설정
        self.shape("circle")  # 공의 모양을 원형으로 설정
        self.penup()  # 공이 이동할 때 선을 그리지 않도록 설정
        self.x_move = 3  # x축 이동 방향과 속도
        self.y_move = 3  # y축 이동 방향과 속도
        self.move_speed = 0.1  # 공의 이동 속도 (게임 난이도 조정에 사용)

    def move(self):
        # 공을 현재 위치에서 이동시킵니다.
        new_x = self.xcor() + self.x_move  # 새로운 x좌표 계산
        new_y = self.ycor() + self.y_move  # 새로운 y좌표 계산
        self.goto(new_x, new_y)  # 공을 새로운 좌표로 이동

    def bounce_y(self):
        # 공이 y축에서 충돌할 때 방향을 반대로 전환
        self.y_move *= -1

    def bounce_x(self):
        # 공이 x축에서 충돌할 때 방향을 반대로 전환하고 속도를 증가
        self.x_move *= -1
        self.move_speed *= 0.9  # 공의 이동 속도를 조금 더 빠르게 설정

    def reset_position(self):
        # 공을 화면 중앙으로 초기화하고 x축 방향을 반전
        self.goto(0, 0)  # 공을 원점으로 이동
        self.move_speed = 0.1  # 이동 속도를 초기화
        self.bounce_x()  # x축 방향 반전
