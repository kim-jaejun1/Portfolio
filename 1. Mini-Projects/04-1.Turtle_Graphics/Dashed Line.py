import turtle as t  # turtle 모듈을 t라는 이름으로 임포트

tim = t.Turtle()  # 'tim'이라는 이름의 거북이 객체 생성

# 15번 반복하면서 대시선 (점선)을 그린다
for _ in range(15):
    tim.forward(10)  # 거북이가 10 단위만큼 직진
    tim.penup()  # 펜을 들어서 선을 그리지 않음
    tim.forward(10)  # 다시 10 단위만큼 직진 (이 부분은 빈 공간이 생김)
    tim.pendown()  # 펜을 내려서 다시 선을 그리기 시작
