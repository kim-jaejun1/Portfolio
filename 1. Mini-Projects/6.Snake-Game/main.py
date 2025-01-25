from turtle import Screen  # 터틀 그래픽 모듈의 Screen 클래스 가져오기
from snake import Snake  # 사용자 정의 Snake 클래스 가져오기
import time  # 시간 관련 모듈 가져오기

# 화면 설정
screen = Screen()
screen.setup(width=600, height=600)  # 화면 크기를 600x600 픽셀로 설정
screen.bgcolor("black")  # 배경색을 검은색으로 설정
screen.title("My Snake Game")  # 창 제목 설정
screen.tracer(0)  # 화면 갱신을 비활성화하여 움직임을 부드럽게 함

# Snake 객체 생성
snake = Snake()
food = Food()  # Food 클래스가 정의되었다고 가정 (하지만 코드에는 정의되지 않았음)

# 키보드 입력 감지 설정
screen.listen()  # 키보드 입력을 수신 대기
screen.onkey(snake.up, "Up")  # "위쪽 화살표" 키로 snake.up 메서드 호출
screen.onkey(snake.down, "Down")  # "아래쪽 화살표" 키로 snake.down 메서드 호출
screen.onkey(snake.left, "Left")  # "왼쪽 화살표" 키로 snake.left 메서드 호출
screen.onkey(snake.right, "Right")  # "오른쪽 화살표" 키로 snake.right 메서드 호출

# 게임 루프
game_is_on = True
while game_is_on:
    screen.update()  # 화면 갱신
    time.sleep(0.1)  # 0.1초 동안 대기하여 게임 속도를 조절

    snake.move()  # Snake 객체를 이동시킴

# 사용자가 화면을 클릭하면 종료
screen.exitonclick()
