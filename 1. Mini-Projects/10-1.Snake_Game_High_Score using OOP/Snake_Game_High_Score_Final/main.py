from turtle import Screen  # 화면을 제어하는 Screen 클래스 가져오기
from snake import Snake  # Snake 클래스 가져오기
from food import Food  # Food 클래스 가져오기
from scoreboard import Scoreboard  # Scoreboard 클래스 가져오기
import time  # 시간 지연을 위한 time 모듈 가져오기

# 게임 화면 설정
screen = Screen()
screen.setup(width=600, height=600)  # 화면 크기 설정
screen.bgcolor("black")  # 배경색을 검은색으로 설정
screen.title("My Snake Game")  # 게임 제목 설정
screen.tracer(0)  # 화면 업데이트를 수동으로 제어 (애니메이션 부드럽게 하기 위함)

# 게임 객체 생성
snake = Snake()  # 뱀 생성
food = Food()  # 먹이 생성
scoreboard = Scoreboard()  # 점수판 생성

# 키보드 입력 감지 설정
screen.listen()  # 키 입력을 받을 준비
screen.onkey(snake.up, "Up")  # 위쪽 방향키 입력 시 뱀이 위로 이동
screen.onkey(snake.down, "Down")  # 아래쪽 방향키 입력 시 뱀이 아래로 이동
screen.onkey(snake.left, "Left")  # 왼쪽 방향키 입력 시 뱀이 왼쪽으로 이동
screen.onkey(snake.right, "Right")  # 오른쪽 방향키 입력 시 뱀이 오른쪽으로 이동

# 게임 실행
game_is_on = True  # 게임 루프 실행 여부 설정
while game_is_on:
    screen.update()  # 화면 업데이트 (tracer(0) 설정으로 인해 수동 업데이트)
    time.sleep(0.1)  # 게임 속도 조절 (0.1초 대기)
    snake.move()  # 뱀 이동

    # 먹이와의 충돌 감지
    if snake.head.distance(food) < 15:  # 뱀의 머리가 먹이와 가까워지면
        food.refresh()  # 먹이를 새로운 위치로 이동
        snake.extend()  # 뱀 길이 증가
        scoreboard.increase_score()  # 점수 증가

    # 벽과의 충돌 감지
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False  # 게임 종료
        scoreboard.game_over()  # 게임 오버 메시지 표시

    # 자신의 몸과의 충돌 감지
    for segment in snake.segments:
        if segment == snake.head:  # 머리는 충돌 검사에서 제외
            pass
        elif snake.head.distance(segment) < 10:  # 머리가 몸통에 닿으면
            game_is_on = False  # 게임 종료
            scoreboard.game_over()  # 게임 오버 메시지 표시

# 화면 클릭 시 종료
screen.exitonclick()
