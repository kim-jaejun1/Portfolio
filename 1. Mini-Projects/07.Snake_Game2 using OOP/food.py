from turtle import Turtle  # Turtle 모듈을 임포트한다.
import random  # 랜덤 좌표 생성을 위해 random 모듈을 임포트한다.

class Food(Turtle):  # Food 클래스는 Turtle 클래스를 상속받는다.
    def __init__(self):
        # 부모 클래스(Turtle)의 초기화 메서드를 호출한다.
        super().__init__()
        # Food 객체의 모양을 원(circle)으로 설정한다.
        self.shape("circle")
        # 객체를 그릴 때 선이 생기지 않도록 한다.
        self.penup()
        # 객체 크기를 기본 크기의 절반으로 줄인다.
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # Food 객체의 색상을 파란색으로 설정한다.
        self.color("blue")
        # 객체의 이동 속도를 가장 빠르게 설정한다.
        self.speed("fastest")
        # 객체를 무작위 좌표로 이동시킨다.
        self.refresh()

    def refresh(self):
        # 화면 내에서 무작위 x, y 좌표를 생성한다.
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        # 객체를 무작위 좌표로 이동시킨다.
        self.goto(random_x, random_y)