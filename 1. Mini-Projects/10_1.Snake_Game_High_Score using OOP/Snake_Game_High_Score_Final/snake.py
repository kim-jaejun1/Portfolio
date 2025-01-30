from turtle import Turtle  # 터틀 그래픽을 위한 Turtle 클래스 가져오기

# 뱀의 초기 위치 목록 (세 개의 블록으로 시작)
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# 한 번 이동할 때의 거리
MOVE_DISTANCE = 20

# 이동 방향 상수 정의
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Snake 게임에서 뱀을 생성하고 제어하는 클래스."""

    def __init__(self):
        """Snake 객체 초기화 메서드.

        뱀의 몸을 구성하는 세그먼트 리스트를 만들고,
        초기 뱀을 생성한 후, 머리를 설정한다.
        """
        self.segments = []  # 뱀의 몸을 이루는 세그먼트 리스트
        self.create_snake()  # 초기 뱀 생성
        self.head = self.segments[0]  # 뱀의 머리 설정

    def create_snake(self):
        """초기 뱀을 생성하는 메서드.

        `STARTING_POSITIONS`의 좌표를 기반으로 세그먼트를 추가한다.
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """새로운 세그먼트를 생성하고 지정된 위치로 이동시키는 메서드."""
        new_segment = Turtle("square")  # 사각형 모양의 터틀 객체 생성
        new_segment.color("white")  # 색상을 흰색으로 설정
        new_segment.penup()  # 선 없이 이동하도록 설정
        new_segment.goto(position)  # 지정된 위치로 이동
        self.segments.append(new_segment)  # 세그먼트를 리스트에 추가

    def extend(self):
        """뱀의 길이를 늘리는 메서드.

        뱀의 마지막 세그먼트 위치에서 새로운 세그먼트를 추가한다.
        """
        self.add_segment(self.segments[-1].position())  # 마지막 세그먼트의 위치에서 추가

    def move(self):
        """뱀을 앞으로 이동시키는 메서드.

        각 세그먼트를 앞 세그먼트의 위치로 이동시키고,
        마지막으로 머리를 앞으로 이동시킨다.
        """
        # 뒤쪽 세그먼트부터 앞 세그먼트의 위치로 이동
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # 머리를 앞으로 이동

    def up(self):
        """뱀의 이동 방향을 위쪽(90도)으로 변경하는 메서드.

        단, 현재 아래쪽을 향하고 있지 않은 경우에만 방향 변경.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """뱀의 이동 방향을 아래쪽(270도)으로 변경하는 메서드.

        단, 현재 위쪽을 향하고 있지 않은 경우에만 방향 변경.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """뱀의 이동 방향을 왼쪽(180도)으로 변경하는 메서드.

        단, 현재 오른쪽을 향하고 있지 않은 경우에만 방향 변경.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """뱀의 이동 방향을 오른쪽(0도)으로 변경하는 메서드.

        단, 현재 왼쪽을 향하고 있지 않은 경우에만 방향 변경.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
