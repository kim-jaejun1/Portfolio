import turtle as t  # turtle 모듈을 t라는 이름으로 임포트
import random  # random 모듈을 임포트하여 랜덤 선택 기능 사용

tim = t.Turtle()  # 'tim'이라는 이름의 거북이 객체 생성
t.colormode(255)  # 색상을 RGB 모드로 설정 (0~255 범위로 색상 지정)

# 랜덤 색상을 생성하는 함수 정의
def random_color():
    r = random.randint(0, 255)  # 빨간색 값 (0~255 범위)
    g = random.randint(0, 255)  # 초록색 값 (0~255 범위)
    b = random.randint(0, 255)  # 파란색 값 (0~255 범위)
    color = (r, g, b)  # (r, g, b) 형태로 색상 튜플을 생성
    return color  # 생성된 랜덤 색상 반환

########### Challenge 5 - Spirograph ########

# 스파이로그래프를 그리는 함수 정의
def draw_spirograph(size_of_gap):
    # size_of_gap에 맞게 원을 그리며 회전하는 루프
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())  # 랜덤 색상으로 설정
        tim.circle(100)  # 반지름이 100인 원을 그림
        tim.setheading(tim.heading() + size_of_gap)  # 각도를 size_of_gap만큼 더하여 회전

draw_spirograph(5)  # 5도씩 회전하며 스파이로그래프 그리기
