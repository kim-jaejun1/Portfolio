import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# 게임 화면 설정
screen = Screen()
screen.setup(width=600, height=600)  # 화면 크기를 600x600으로 설정
screen.tracer(0)  # 애니메이션을 비활성화하여 수동으로 화면을 업데이트하도록 설정

# 게임 루프 실행 변수
game_is_on = True

# 게임 루프 시작
while game_is_on:
    time.sleep(0.1)  # 루프가 0.1초마다 실행되도록 설정 (게임 속도 조절)
    screen.update()  # 화면을 갱신하여 변경 사항을 반영
