from turtle import Turtle, Screen  # turtle 모듈에서 Turtle과 Screen 클래스를 가져옵니다.
import random  # 랜덤 숫자를 생성하기 위한 random 모듈을 가져옵니다.

# 레이스 상태를 저장하는 변수 (초기값은 False)
is_race_on = False
screen = Screen()  # Screen 객체를 생성합니다.
screen.setup(width=500, height=400)  # 스크린의 크기를 500x400으로 설정합니다.
# 사용자에게 입력창을 띄워 어떤 색의 거북이가 승리할지 선택하도록 합니다.
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# 거북이 색상과 초기 위치를 정의합니다.
colors = ["red", "orange", "yellow", "green", "blue", "purple"]  # 거북이들의 색상 리스트
y_positions = [-70, -40, -10, 20, 50, 80]  # 거북이들의 y좌표 초기 위치 리스트
all_turtles = []  # 모든 거북이 객체를 저장할 리스트

# 6개의 거북이 객체를 생성하고 초기 위치와 색상을 설정합니다.
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")  # 거북이 객체를 생성합니다.
    new_turtle.penup()  # 선을 그리지 않도록 펜을 들어올립니다.
    new_turtle.color(colors[turtle_index])  # 각 거북이의 색상을 설정합니다.
    new_turtle.goto(x=-230, y=y_positions[turtle_index])  # 각 거북이를 초기 위치로 이동시킵니다.
    all_turtles.append(new_turtle)  # 생성한 거북이를 리스트에 추가합니다.

# 사용자가 배팅을 입력하면 레이스를 시작합니다.
if user_bet:
    is_race_on = True

# 레이스가 진행되는 동안의 동작을 정의합니다.
while is_race_on:
    for turtle in all_turtles:
        # 거북이의 위치가 x좌표 230을 넘으면 레이스 종료 조건입니다.
        # (230은 스크린 너비의 절반(250)에서 거북이 크기의 절반을 뺀 값입니다.)
        if turtle.xcor() > 230:
            is_race_on = False  # 레이스를 종료합니다.
            winning_color = turtle.pencolor()  # 승리한 거북이의 색상을 가져옵니다.
            # 사용자의 배팅과 승리한 거북이 색상을 비교하여 결과를 출력합니다.
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")  # 사용자가 이겼을 때 메시지 출력
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")  # 사용자가 졌을 때 메시지 출력

        # 각 거북이가 이동할 거리를 랜덤으로 설정합니다.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)  # 거북이를 전진시킵니다.

# 스크린을 클릭하면 프로그램이 종료됩니다.
screen.exitonclick()
