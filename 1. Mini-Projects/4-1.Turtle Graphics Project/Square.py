import turtle as t  # turtle 모듈을 t라는 이름으로 임포트

timmy_the_turtle = t.Turtle()  # 'timmy_the_turtle'이라는 이름의 거북이 객체 생성

# 4번 반복하면서 사각형을 그린다
for _ in range(4):
    timmy_the_turtle.forward(100)  # 거북이가 100 단위만큼 직진
    timmy_the_turtle.left(90)  # 거북이가 90도 왼쪽으로 회전
