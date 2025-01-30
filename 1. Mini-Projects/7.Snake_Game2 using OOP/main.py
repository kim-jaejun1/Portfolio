from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen 객체를 생성하고 화면의 초기 설정을 정의한다.
screen = Screen()
screen.setup(width=600, height=600)  # 화면의 크기를 600x600으로 설정한다.
screen.bgcolor("black")  # 배경색을 검은색으로 설정한다.
screen.title("My Snake Game")  # 화면 제목을 "My Snake Game"으로 설정한다.
screen.tracer(0)  # 애니메이션 효과를 끄고 수동으로 업데이트한다.

# Snake, Food, Scoreboard 객체를 생성한다.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# 키보드 입력을 설정한다.
screen.listen()
screen.onkey(snake.up, "Up")  # 위쪽 화살표 키로 snake의 up 메서드를 호출한다.
screen.onkey(snake.down, "Down")  # 아래쪽 화살표 키로 snake의 down 메서드를 호출한다.
screen.onkey(snake.left, "Left")  # 왼쪽 화살표 키로 snake의 left 메서드를 호출한다.
screen.onkey(snake.right, "Right")  # 오른쪽 화살표 키로 snake의 right 메서드를 호출한다.

# 게임 루프를 시작한다.
game_is_on = True
while game_is_on:
    screen.update()  # 화면을 업데이트한다.
    time.sleep(0.1)  # 0.1초 동안 대기한다.
    snake.move()  # 뱀이 이동한다.

    # 음식과의 충돌을 감지한다.
    if snake.head.distance(food) < 15:  # 뱀의 머리와 음식 사이의 거리가 15 미만이면 충돌로 간주한다.
        food.refresh()  # 음식을 새로운 위치로 이동시킨다.
        snake.extend()  # 뱀의 몸을 연장한다.
        scoreboard.increase_score()  # 점수를 증가시킨다.

    # 벽과의 충돌을 감지한다.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False  # 게임을 종료한다.
        scoreboard.game_over()  # 게임 종료 메시지를 표시한다.

    # 꼬리와의 충돌을 감지한다.
    for segment in snake.segments:
        if segment == snake.head:
            pass  # 뱀의 머리인 경우 충돌로 간주하지 않는다.
        elif snake.head.distance(segment) < 10:  # 머리와 몸체 사이의 거리가 10 미만이면 충돌로 간주한다.
            game_is_on = False  # 게임을 종료한다.
            scoreboard.game_over()  # 게임 종료 메시지를 표시한다.

# 화면을 클릭하면 프로그램을 종료한다.
screen.exitonclick()
