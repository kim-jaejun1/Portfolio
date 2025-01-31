import turtle  # 터틀 그래픽 모듈 가져오기
import pandas  # 판다스 모듈 가져오기 (CSV 파일을 읽기 위해 사용)

# 터틀 스크린 설정
screen = turtle.Screen()
screen.title("U.S. States Game")  # 게임 제목 설정

# 배경 이미지 추가 (미국 지도)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# CSV 파일을 읽어서 데이터프레임으로 변환
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()  # 모든 주 이름을 리스트로 저장

guessed_states = []  # 사용자가 맞힌 주 목록 저장

# 사용자가 50개 주를 모두 맞힐 때까지 반복
while len(guessed_states) < 50:
    # 사용자 입력 받기 (맞힌 주 개수 표시)
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # 사용자가 'Exit'을 입력하면 게임 종료 및 학습할 주 저장
    if answer_state == "Exit":
        missing_states = []  # 사용자가 맞히지 못한 주 목록 저장
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        # 맞히지 못한 주 목록을 CSV 파일로 저장
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # 사용자가 입력한 주가 리스트에 있으면 맞힌 것으로 처리
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        # 입력한 주의 좌표 가져오기
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))  # 주의 좌표로 이동
        t.write(answer_state)  # 주 이름을 지도에 표시
