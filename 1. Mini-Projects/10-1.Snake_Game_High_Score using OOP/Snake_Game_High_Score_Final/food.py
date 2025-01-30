from turtle import Turtle
import random


class Food(Turtle):
    """Snake 게임에서 먹이 역할을 하는 클래스.

    `Turtle` 클래스를 상속받아 먹이를 생성하고,
    랜덤한 위치에 배치하는 기능을 제공한다.
    """

    def __init__(self):
        """Food 객체 초기화 메서드.

        원 모양의 파란색 먹이를 생성하고,
        크기를 작게 설정한 후,
        화면에서 빠르게 움직일 수 있도록 한다.
        """
        super().__init__()  # 부모 클래스(Turtle) 초기화
        self.shape("circle")  # 원형 모양 설정
        self.penup()  # 선 없이 이동하도록 설정
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # 기본 크기의 절반 크기로 설정
        self.color("blue")  # 색상을 파란색으로 설정
        self.speed("fastest")  # 가장 빠른 속도로 설정
        self.refresh()  # 초기 위치를 랜덤으로 설정

    def refresh(self):
        """먹이의 위치를 랜덤한 좌표로 변경하는 메서드.

        x와 y 좌표를 각각 -280에서 280 사이의 랜덤한 값으로 설정하여
        새로운 위치로 이동한다.
        """
        random_x = random.randint(-280, 280)  # x 좌표 랜덤 생성
        random_y = random.randint(-280, 280)  # y 좌표 랜덤 생성
        self.goto(random_x, random_y)  # 해당 좌표로 이동
