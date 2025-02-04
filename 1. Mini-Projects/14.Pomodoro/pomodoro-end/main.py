from tkinter import *
import math

# ---------------------------- 상수 설정 ------------------------------- #
PINK = "#e2979c"  # 짧은 휴식 시간에 사용될 색상
RED = "#e7305b"  # 긴 휴식 시간에 사용될 색상
GREEN = "#9bdeac"  # 작업 시간에 사용될 색상
YELLOW = "#f7f5dd"  # 배경 색상
FONT_NAME = "Courier"  # 폰트 스타일
WORK_MIN = 1  # 작업 시간 (분)
SHORT_BREAK_MIN = 5  # 짧은 휴식 시간 (분)
LONG_BREAK_MIN = 20  # 긴 휴식 시간 (분)
reps = 0  # 작업 및 휴식 반복 횟수
timer = None  # 타이머 변수

# ---------------------------- 타이머 초기화 ------------------------------- #

def reset_timer():
    """ 타이머를 초기화하는 함수 """
    window.after_cancel(timer)  # 현재 실행 중인 타이머 취소
    canvas.itemconfig(timer_text, text="00:00")  # 타이머 표시 초기화
    title_label.config(text="Timer")  # 타이틀 초기화
    check_marks.config(text="")  # 체크 마크 초기화
    global reps
    reps = 0  # 반복 횟수 초기화

# ---------------------------- 타이머 시작 ------------------------------- #

def start_timer():
    """ 타이머를 시작하는 함수 """
    global reps
    reps += 1  # 반복 횟수 증가

    work_sec = WORK_MIN * 60  # 작업 시간(초)
    short_break_sec = SHORT_BREAK_MIN * 60  # 짧은 휴식 시간(초)
    long_break_sec = LONG_BREAK_MIN * 60  # 긴 휴식 시간(초)

    if reps % 8 == 0:  # 8번째 반복마다 긴 휴식
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:  # 2의 배수일 때 짧은 휴식
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:  # 그 외에는 작업 시간
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- 카운트다운 기능 ------------------------------- #
def count_down(count):
    """ 카운트다운을 실행하는 함수 """
    count_min = math.floor(count / 60)  # 분 단위 계산
    count_sec = count % 60  # 초 단위 계산
    if count_sec < 10:  # 초가 한 자리 수일 경우 앞에 0을 붙여 표시
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")  # 타이머 UI 업데이트
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # 1초 후 카운트다운 계속 진행
    else:
        start_timer()  # 시간이 0이 되면 다음 타이머 시작
        marks = ""
        work_sessions = math.floor(reps / 2)  # 완료한 작업 세션 수 계산
        for _ in range(work_sessions):
            marks += "✔"  # 작업 세션이 끝날 때마다 체크 마크 추가
        check_marks.config(text=marks)  # UI 업데이트

# ---------------------------- UI 설정 ------------------------------- #
window = Tk()
window.title("Pomodoro")  # 창 제목 설정
window.config(padx=100, pady=50, bg=YELLOW)  # 여백 및 배경 색상 설정

# 타이틀 레이블 설정
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# 캔버스(이미지 및 타이머 표시) 설정
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # 타이머 이미지
canvas.create_image(100, 112, image=tomato_img)  # 이미지 배치
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# 시작 버튼 설정
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# 초기화 버튼 설정
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# 체크 마크 레이블 설정 (완료한 작업 표시)
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# 창 실행
window.mainloop()
