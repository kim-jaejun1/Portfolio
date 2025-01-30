from turtle import Turtle  # 터틀 그래픽을 위한 Turtle 클래스 가져오기
import random  # 랜덤한 위치 생성을 위한 random 모듈 가져오기


class Food(Turtle):
    """Snake 게임에서 뱀이 먹을 수 있는 먹이를 생성하는 클래스."""

    def __init__(self):
        """Food 객체 초기화 메서드.

        원형 모양의 파란색 먹이를 생성하고, 크기를 작게 설정한 후,
        랜덤한 위치에 배치한다.
        """
        super().__init__()  # 부모 클래스(Turtle) 초기화
        self.shape("circle")  # 원형 모양 설정
        self.penup()  # 선 없이 이동하도록 설정
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # 기본 크기의 절반 크기로 설정 (작게 만들기)
        self.color("blue")  # 색상을 파란색으로 설정
        self.speed("fastest")  # 가장 빠른 속도로 설정하여 즉각적인 위치 변경 가능
        self.refresh()  # 처음 생성될 때 랜덤 위치 지정

    def refresh(self):
        """먹이의 위치를 랜덤한 좌표로 변경하는 메서드.

        x와 y 좌표를 각각 -280에서 280 사이의 랜덤한 값으로 설정하여
        새로운 위치로 이동시킨다.
        """
        random_x = random.randint(-280, 280)  # x 좌표 랜덤 생성
        random_y = random.randint(-280, 280)  # y 좌표 랜덤 생성
        self.goto(random_x, random_y)  # 새로운 위치로 이동
