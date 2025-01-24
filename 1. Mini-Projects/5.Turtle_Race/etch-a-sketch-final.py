from turtle import Turtle, Screen  # turtle 모듈에서 Turtle과 Screen 클래스를 가져옵니다.

tim = Turtle()  # Turtle 객체를 생성하고 tim 변수에 저장합니다.
screen = Screen()  # Screen 객체를 생성하고 screen 변수에 저장합니다.

# 앞으로 이동하는 함수
def move_forwards():
    tim.forward(10)  # 거북이를 앞으로 10만큼 이동시킵니다.

# 뒤로 이동하는 함수
def move_backwards():
    tim.backward(10)  # 거북이를 뒤로 10만큼 이동시킵니다.

# 왼쪽으로 회전하는 함수
def turn_left():
    new_heading = tim.heading() + 10  # 현재 방향에서 10도 왼쪽으로 회전한 각도를 계산합니다.
    tim.setheading(new_heading)  # 거북이의 새로운 방향을 설정합니다.

# 오른쪽으로 회전하는 함수
def turn_right():
    new_heading = tim.heading() - 10  # 현재 방향에서 10도 오른쪽으로 회전한 각도를 계산합니다.
    tim.setheading(new_heading)  # 거북이의 새로운 방향을 설정합니다.

# 화면을 초기화하는 함수
def clear():
    tim.clear()  # 거북이가 그린 모든 선과 도형을 지웁니다.
    tim.penup()  # 거북이가 선을 그리지 않도록 펜을 들어올립니다.
    tim.home()  # 거북이를 화면 중앙(0, 0)으로 이동시키고 방향을 초기화합니다.
    tim.pendown()  # 펜을 다시 내려서 선을 그릴 수 있도록 설정합니다.

screen.listen()  # 키보드 입력을 감지할 수 있도록 스크린을 설정합니다.

# 키보드 이벤트를 연결합니다.
screen.onkey(move_forwards, "Up")  # 위쪽 화살표 키를 누르면 move_forwards 함수 실행
screen.onkey(move_backwards, "Down")  # 아래쪽 화살표 키를 누르면 move_backwards 함수 실행
screen.onkey(turn_left, "Left")  # 왼쪽 화살표 키를 누르면 turn_left 함수 실행
screen.onkey(turn_right, "Right")  # 오른쪽 화살표 키를 누르면 turn_right 함수 실행
screen.onkey(clear, "c")  # 'c' 키를 누르면 clear 함수 실행

# 화면을 클릭하면 프로그램을 종료합니다.
screen.exitonclick()
