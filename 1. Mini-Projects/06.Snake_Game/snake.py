from turtle import Turtle  # 터틀 그래픽 모듈의 Turtle 클래스 가져오기

# 상수 정의
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # 뱀의 초기 위치 (세 개의 사각형으로 구성)
MOVE_DISTANCE = 20  # 한 번 이동할 때의 거리
UP = 90  # 위쪽 방향 (각도)
DOWN = 270  # 아래쪽 방향 (각도)
LEFT = 180  # 왼쪽 방향 (각도)
RIGHT = 0  # 오른쪽 방향 (각도)

# Snake 클래스 정의
class Snake:
    def __init__(self):
        """Snake 객체를 초기화하는 메서드"""
        self.segments = []  # 뱀을 구성하는 각 Turtle 객체를 저장하는 리스트
        self.create_snake()  # 초기 뱀 생성
        self.head = self.segments[0]  # 뱀의 머리 부분

    def create_snake(self):
        """초기 뱀을 생성하고 위치를 설정하는 메서드"""
        for position in STARTING_POSITIONS:  # 초기 위치에 따라 세그먼트 생성
            new_segment = Turtle("square")  # 사각형 모양의 Turtle 객체 생성
            new_segment.color("white")  # 세그먼트 색상 설정
            new_segment.penup()  # 선을 그리지 않도록 설정
            new_segment.goto(position)  # 세그먼트 위치 설정
            self.segments.append(new_segment)  # 세그먼트를 리스트에 추가

    def move(self):
        """뱀이 이동하는 메서드"""
        # 뱀의 몸통을 뒤에서부터 앞 세그먼트의 위치로 이동
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # 앞 세그먼트의 x 좌표
            new_y = self.segments[seg_num - 1].ycor()  # 앞 세그먼트의 y 좌표
            self.segments[seg_num].goto(new_x, new_y)  # 현재 세그먼트를 앞 세그먼트 위치로 이동
        self.head.forward(MOVE_DISTANCE)  # 뱀의 머리를 앞으로 이동

    def up(self):
        """뱀의 방향을 위쪽으로 설정하는 메서드"""
        if self.head.heading() != DOWN:  # 현재 방향이 아래쪽이 아닐 때만 변경
            self.head.setheading(UP)  # 방향을 위쪽으로 설정

    def down(self):
        """뱀의 방향을 아래쪽으로 설정하는 메서드"""
        if self.head.heading() != UP:  # 현재 방향이 위쪽이 아닐 때만 변경
            self.head.setheading(DOWN)  # 방향을 아래쪽으로 설정

    def left(self):
        """뱀의 방향을 왼쪽으로 설정하는 메서드"""
        if self.head.heading() != RIGHT:  # 현재 방향이 오른쪽이 아닐 때만 변경
            self.head.setheading(LEFT)  # 방향을 왼쪽으로 설정

    def right(self):
        """뱀의 방향을 오른쪽으로 설정하는 메서드"""
        if self.head.heading() != LEFT:  # 현재 방향이 왼쪽이 아닐 때만 변경
            self.head.setheading(RIGHT)  # 방향을 오른쪽으로 설정
