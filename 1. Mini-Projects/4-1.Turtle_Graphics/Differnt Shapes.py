import turtle as t  # turtle 모듈을 t라는 이름으로 임포트
import random  # random 모듈을 임포트하여 랜덤 선택 기능 사용

tim = t.Turtle()  # 'tim'이라는 이름의 거북이 객체 생성

# 사용할 색상을 리스트로 정의
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# 다각형을 그리는 함수 정의
def draw_shape(num_sides):
    angle = 360 / num_sides  # 각 변에 대한 회전 각도 계산
    for _ in range(num_sides):  # 주어진 변의 수만큼 반복
        tim.forward(100)  # 100만큼 직진
        tim.right(angle)  # 각도를 기준으로 오른쪽으로 회전

# 3에서 9까지의 숫자를 반복하면서 각기 다른 도형을 그린다
for shape_side_n in range(3, 10):
    tim.color(random.choice(colours))  # 색상을 랜덤으로 선택하여 설정
    draw_shape(shape_side_n)  # 해당 변의 수를 가진 도형 그리기
