import turtle as t  # turtle 모듈을 t라는 이름으로 임포트
import random  # random 모듈을 임포트하여 랜덤 선택 기능 사용

tim = t.Turtle()  # 'tim'이라는 이름의 거북이 객체 생성

# 사용할 색상 리스트 정의
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# 거북이가 갈 수 있는 방향 (0: 오른쪽, 90: 위쪽, 180: 왼쪽, 270: 아래쪽)
directions = [0, 90, 180, 270]

tim.pensize(15)  # 펜 크기를 15로 설정
tim.speed("fastest")  # 거북이의 속도를 가장 빠르게 설정

# 200번 반복하면서 랜덤한 색상과 방향으로 움직인다
for _ in range(200):
    tim.color(random.choice(colours))  # 색상을 랜덤으로 선택하여 설정
    tim.forward(30)  # 30 단위만큼 직진
    tim.setheading(random.choice(directions))  # 방향을 랜덤으로 설정 (0, 90, 180, 270 중 하나)
