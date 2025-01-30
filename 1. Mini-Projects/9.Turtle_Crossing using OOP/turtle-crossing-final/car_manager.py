from turtle import Turtle
import random

# 자동차 색상 목록
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# 자동차의 초기 이동 거리 및 레벨 업 시 증가량
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        """ 자동차 관리를 위한 클래스 초기화 """
        self.all_cars = []  # 생성된 자동차 객체를 저장하는 리스트
        self.car_speed = STARTING_MOVE_DISTANCE  # 자동차의 초기 이동 속도 설정

    def create_car(self):
        """ 일정 확률(1/6)로 새로운 자동차를 생성하여 리스트에 추가 """
        random_chance = random.randint(1, 6)
        if random_chance == 1:  # 1이 나올 경우 자동차 생성
            new_car = Turtle("square")  # 새로운 자동차 객체 생성
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # 자동차 크기 설정 (가로로 긴 직사각형)
            new_car.penup()  # 펜을 올려서 이동 시 선이 그려지지 않도록 설정
            new_car.color(random.choice(COLORS))  # 자동차의 색상을 랜덤으로 선택
            random_y = random.randint(-250, 250)  # 화면 상 랜덤한 Y 좌표 선택
            new_car.goto(300, random_y)  # 자동차를 화면 오른쪽 끝(300, random_y)에 배치
            self.all_cars.append(new_car)  # 생성된 자동차를 리스트에 추가

    def move_cars(self):
        """ 리스트에 있는 모든 자동차를 왼쪽으로 이동 """
        for car in self.all_cars:
            car.backward(self.car_speed)  # 자동차를 현재 속도만큼 왼쪽으로 이동

    def level_up(self):
        """ 레벨 업 시 자동차 이동 속도를 증가 """
        self.car_speed += MOVE_INCREMENT  # 이동 속도를 증가시켜 난이도 상승
