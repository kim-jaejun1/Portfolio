from turtle import Turtle

# 플레이어(거북이)의 시작 위치
STARTING_POSITION = (0, -280)

# 이동 거리
MOVE_DISTANCE = 10

# 도착선 Y 좌표
FINISH_LINE_Y = 280


class Player(Turtle):
    """ 플레이어(거북이) 클래스 """

    def __init__(self):
        """ 플레이어 객체 초기화 """
        super().__init__()
        self.shape("turtle")  # 거북이 모양 설정
        self.penup()  # 펜을 올려서 이동 시 선이 그려지지 않도록 설정
        self.go_to_start()  # 시작 위치로 이동
        self.setheading(90)  # 위쪽(90도) 방향으로 설정

    def go_up(self):
        """ 플레이어를 위쪽으로 이동 """
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """ 플레이어를 시작 위치로 이동 """
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """ 플레이어가 도착선에 도달했는지 확인 """
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
