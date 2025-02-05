import turtle as turtle_module  # turtle 모듈을 turtle_module이라는 이름으로 임포트
import random  # 랜덤 모듈을 임포트하여 랜덤 색상 선택에 사용

turtle_module.colormode(255)  # RGB 색상 모드로 설정 (0~255 범위)
tim = turtle_module.Turtle()  # 'tim'이라는 이름의 거북이 객체 생성
tim.speed("fastest")  # 거북이의 속도를 가장 빠르게 설정
tim.penup()  # 거북이의 펜을 들어서 선을 그리지 않음
tim.hideturtle()  # 거북이를 화면에 보이지 않게 숨김

# 사용할 색상 리스트 (RGB 튜플로 정의)
color_list = [
    (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124),
    (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86),
    (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158),
    (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90),
    (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153),
    (174, 94, 97), (176, 192, 209)
]

tim.setheading(225)  # 거북이가 왼쪽 아래 방향을 향하도록 설정 (225도)
tim.forward(300)  # 300만큼 직진 (이동 후 시작 위치 조정)
tim.setheading(0)  # 거북이가 오른쪽을 향하도록 설정 (0도)

number_of_dots = 100  # 그릴 점의 개수 설정 (100개)

# 100개의 점을 그리기 위한 반복문
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))  # 랜덤 색상으로 20 크기의 점을 그림
    tim.forward(50)  # 50만큼 직진

    # 한 줄에 10개의 점을 그린 후, 새 줄로 이동하기 위한 조건
    if dot_count % 10 == 0:
        tim.setheading(90)  # 위쪽을 향하도록 설정 (90도)
        tim.forward(50)  # 50만큼 직진하여 새 줄로 이동
        tim.setheading(180)  # 왼쪽을 향하도록 설정 (180도)
        tim.forward(500)  # 500만큼 뒤로 이동하여 새 줄 시작 위치로 돌아감
        tim.setheading(0)  # 다시 오른쪽을 향하도록 설정 (0도)

# 사용자가 화면을 클릭하면 종료되도록 설정
screen = turtle_module.Screen()  # 화면 객체 생성
screen.exitonclick()  # 화면을 클릭하면 종료
