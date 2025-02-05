from tkinter import *  # Tkinter GUI 라이브러리 가져오기

# 메인 윈도우 생성
window = Tk()
window.title("Grid Layout Example")  # 윈도우 제목 설정

# 빨간색 레이블 생성 및 배치
r = Label(bg="red", width=20, height=5)  # 배경색: 빨강, 너비: 20, 높이: 5
r.grid(row=0, column=0)  # 0행 0열에 배치

# 초록색 레이블 생성 및 배치
g = Label(bg="green", width=20, height=5)  # 배경색: 초록, 너비: 20, 높이: 5
g.grid(row=1, column=1)  # 1행 1열에 배치

# 파란색 레이블 생성 및 배치
b = Label(bg="blue", width=40, height=5)  # 배경색: 파랑, 너비: 40, 높이: 5
b.grid(row=2, column=0, columnspan=2)  # 2행 0열부터 1열까지 확장하여 배치

# GUI 실행
window.mainloop()
