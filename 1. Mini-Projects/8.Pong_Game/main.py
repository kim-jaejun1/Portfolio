from turtle import Screen, Turtle
from paddle import Paddle  # Paddle 클래스 임포트
from ball import Ball  # Ball 클래스 임포트
from scoreboard import Scoreboard  # Scoreboard 클래스 임포트
import time

# 화면 설정
screen = Screen()
screen.bgcolor("black")  # 배경색을 검정색으로 설정
screen.setup(width=800, height=600)  # 화면 크기 설정 (800x600)
screen.title("Pong")  # 게임 제목 설정
screen.tracer(0)  # 화면 업데이트를 수동으로 설정 (애니메이션 효과를 위해)

# 게임 객체 생성
r_paddle = Paddle((350, 0))  # 오른쪽 패들 생성 (초기 위치 (350, 0))
l_paddle = Paddle((-350, 0))  # 왼쪽 패들 생성 (초기 위치 (-350, 0))
ball = Ball()  # 공 객체 생성
scoreboard = Scoreboard()  # 점수판 객체 생성

# 키 입력 설정
screen.listen()  # 키보드 입력을 대기
screen.onkey(r_paddle.go_up, "Up")  # 위쪽 화살표 키로 오른쪽 패들을 위로 이동
screen.onkey(r_paddle.go_down, "Down")  # 아래쪽 화살표 키로 오른쪽 패들을 아래로 이동
screen.onkey(l_paddle.go_up, "w")  # 'w' 키로 왼쪽 패들을 위로 이동
screen.onkey(l_paddle.go_down, "s")  # 's' 키로 왼쪽 패들을 아래로 이동

# 게임 루프
game_is_on = True
while game_is_on:
    screen.update()  # 화면 업데이트
    ball.move()  # 공 이동

    # 공이 벽에 충돌했는지 확인 (위쪽/아래쪽 경계)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # y축 방향 반전

    # 공이 패들과 충돌했는지 확인
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()  # x축 방향 반전

    # 오른쪽 패들이 공을 놓쳤는지 확인
    if ball.xcor() > 380:
        ball.reset_position()  # 공을 초기 위치로 리셋
        scoreboard.l_point()  # 왼쪽 플레이어 점수 증가

    # 왼쪽 패들이 공을 놓쳤는지 확인
    if ball.xcor() < -380:
        ball.reset_position()  # 공을 초기 위치로 리셋
        scoreboard.r_point()  # 오른쪽 플레이어 점수 증가

# 화면을 클릭하면 게임 종료
screen.exitonclick()
