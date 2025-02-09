from tkinter import *  # Tkinter 라이브러리 임포트 (GUI 생성용)
import pandas  # pandas 라이브러리 임포트 (데이터 처리용)
import random  # random 라이브러리 임포트 (랜덤 선택용)

# 배경 색상 설정
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}  # 현재 플래시 카드 정보 저장
to_learn = {}  # 학습해야 할 단어 목록 저장

# 기존 학습 데이터 불러오기 (파일이 없으면 기본 데이터 사용)
try:
    data = pandas.read_csv("data/words_to_learn.csv")  # 학습해야 할 단어 목록 불러오기
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")  # 기본 단어 목록 불러오기
    print(original_data)
    to_learn = original_data.to_dict(orient="records")  # 데이터를 딕셔너리 형태로 변환
else:
    to_learn = data.to_dict(orient="records")  # 데이터를 딕셔너리 형태로 변환

# 새로운 플래시 카드 표시 함수
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # 이전 타이머 취소
    current_card = random.choice(to_learn)  # 무작위 단어 선택
    canvas.itemconfig(card_title, text="French", fill="black")  # 카드 제목을 "French"로 설정
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")  # 선택된 프랑스어 단어 표시
    canvas.itemconfig(card_background, image=card_front_img)  # 카드 앞면 이미지 표시
    flip_timer = window.after(3000, func=flip_card)  # 3초 후에 카드 뒷면으로 전환

# 플래시 카드 뒤집기 함수
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")  # 카드 제목을 "English"로 변경
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")  # 해당 영어 뜻 표시
    canvas.itemconfig(card_background, image=card_back_img)  # 카드 뒷면 이미지 표시

# 사용자가 단어를 학습했다고 표시하는 함수
def is_known():
    to_learn.remove(current_card)  # 학습 완료한 단어 목록에서 제거
    print(len(to_learn))  # 남은 단어 개수 출력
    data = pandas.DataFrame(to_learn)  # 학습해야 할 단어 목록을 데이터프레임으로 변환
    data.to_csv("data/words_to_learn.csv", index=False)  # 파일에 저장 (이후에도 학습 상태 유지)
    next_card()  # 다음 카드로 이동

# Tkinter 창 생성 및 설정
window = Tk()
window.title("Flashy")  # 창 제목 설정
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # 패딩 및 배경색 설정

flip_timer = window.after(3000, func=flip_card)  # 3초 후 카드 뒷면으로 자동 전환

# 캔버스(카드) 생성
canvas = Canvas(width=800, height=526)  # 캔버스 크기 설정
card_front_img = PhotoImage(file="images/card_front.png")  # 카드 앞면 이미지 로드
card_back_img = PhotoImage(file="images/card_back.png")  # 카드 뒷면 이미지 로드
card_background = canvas.create_image(400, 263, image=card_front_img)  # 초기 카드 앞면 이미지 표시
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))  # 카드 제목 표시
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))  # 카드 단어 표시
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)  # 배경 및 테두리 설정
canvas.grid(row=0, column=0, columnspan=2)  # 그리드 배치

# "틀림" 버튼 생성
cross_image = PhotoImage(file="images/wrong.png")  # 틀림 버튼 이미지 로드
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)  # 버튼 생성 및 함수 연결
unknown_button.grid(row=1, column=0)  # 그리드 배치

# "맞음" 버튼 생성
check_image = PhotoImage(file="images/right.png")  # 맞음 버튼 이미지 로드
known_button = Button(image=check_image, highlightthickness=0, command=is_known)  # 버튼 생성 및 함수 연결
known_button.grid(row=1, column=1)  # 그리드 배치

next_card()  # 첫 번째 카드 표시

window.mainloop()  # Tkinter GUI 실행
