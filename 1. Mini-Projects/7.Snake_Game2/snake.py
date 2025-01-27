from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # 뱀의 초기 위치 리스트
MOVE_DISTANCE = 20  # 뱀의 이동 거리
UP = 90  # 위쪽 방향(각도)
DOWN = 270  # 아래쪽 방향(각도)
LEFT = 180  # 왼쪽 방향(각도)
RIGHT = 0  # 오른쪽 방향(각도)

class Snake:

    def __init__(self):
        self.segments = []  # 뱀의 몸통을 구성하는 세그먼트 리스트
        self.create_snake()  # 초기 뱀 생성
        self.head = self.segments[0]  # 뱀의 머리를 첫 번째 세그먼트로 설정

    def create_snake(self):
        # STARTING_POSITIONS에 따라 뱀의 초기 세그먼트를 생성한다.
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # 새로운 세그먼트를 생성하고 지정된 위치로 이동시킨다.
        new_segment = Turtle("square")
        new_segment.color("white")  # 세그먼트 색상 설정
        new_segment.penup()  # 선을 그리지 않도록 설정
        new_segment.goto(position)  # 지정된 위치로 이동
        self.segments.append(new_segment)  # 세그먼트를 리스트에 추가

    def extend(self):
        # 뱀의 길이를 연장한다. 마지막 세그먼트 위치를 기준으로 추가
        self.add_segment(self.segments[-1].position())

    def move(self):
        # 뱀의 몸통을 앞 세그먼트의 위치로 이동시키고 머리를 전진시킨다.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # 뱀의 현재 방향이 아래쪽이 아닐 때 위쪽으로 방향 전환
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # 뱀의 현재 방향이 위쪽이 아닐 때 아래쪽으로 방향 전환
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # 뱀의 현재 방향이 오른쪽이 아닐 때 왼쪽으로 방향 전환
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # 뱀의 현재 방향이 왼쪽이 아닐 때 오른쪽으로 방향 전환
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
