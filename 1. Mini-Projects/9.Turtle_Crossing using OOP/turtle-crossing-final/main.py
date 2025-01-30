import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# 스크린 설정
screen = Screen()
screen.setup(width=600, height=600)  # 창 크기를 600x600으로 설정
screen.tracer(0)  # 애니메이션을 끄고, 수동으로 업데이트하도록 설정

# 게임의 주요 객체 생성
player = Player()  # 플레이어(거북이) 객체 생성
car_manager = CarManager()  # 자동차 관리자 객체 생성
scoreboard = Scoreboard()  # 점수판 객체 생성

# 키 입력 설정
screen.listen()  # 키보드 입력을 감지하도록 설정
screen.onkey(player.go_up, "Up")  # "Up" 키를 누르면 플레이어가 위로 이동

# 게임 실행 상태 변수
game_is_on = True

# 게임 루프
while game_is_on:
    time.sleep(0.1)  # 게임 속도 조절 (0.1초마다 루프 실행)
    screen.update()  # 화면 업데이트

    car_manager.create_car()  # 새로운 자동차를 일정 확률로 생성
    car_manager.move_cars()  # 모든 자동차를 왼쪽으로 이동

    # 자동차와의 충돌 감지
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # 플레이어와 자동차의 거리가 20 미만이면 충돌
            game_is_on = False  # 게임 루프 종료
            scoreboard.game_over()  # "Game Over" 메시지 표시

    # 플레이어가 도착선에 도달했는지 확인
    if player.is_at_finish_line():
        player.go_to_start()  # 플레이어를 시작 위치로 이동
        car_manager.level_up()  # 자동차 이동 속도 증가 (난이도 상승)
        scoreboard.increase_level()  # 점수(레벨) 증가

# 사용자가 클릭하면 창 닫기
screen.exitonclick()
