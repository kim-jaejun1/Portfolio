from tkinter import *  # Tkinter 라이브러리 가져오기


# 버튼 클릭 시 실행될 함수 정의
def button_clicked():
    print("I got clicked")  # 콘솔에 클릭되었다는 메시지 출력
    new_text = input.get()  # 입력 필드에서 값을 가져옴
    my_label.config(text=new_text)  # 가져온 값을 라벨의 텍스트로 변경


# Tkinter 윈도우 객체 생성
window = Tk()
window.title("My First GUI Program")  # 윈도우 제목 설정
window.minsize(width=500, height=300)  # 최소 크기 설정
window.config(padx=100, pady=200)  # 전체 패딩 추가 (여백 설정)

# Label (라벨 위젯 생성)
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))  # 라벨 생성 (기본 텍스트, 폰트 설정)
my_label.config(text="New Text")  # 라벨의 텍스트를 변경
my_label.grid(column=0, row=0)  # 라벨을 (0,0) 위치에 배치
my_label.config(padx=50, pady=50)  # 라벨 내부 패딩 추가

# Button (버튼 생성)
button = Button(text="Click Me", command=button_clicked)  # 버튼 생성 및 클릭 이벤트 연결
button.grid(column=1, row=1)  # 버튼을 (1,1) 위치에 배치

# 새로운 버튼 추가
new_button = Button(text="New Button")  # 새 버튼 생성 (기능 없음)
new_button.grid(column=2, row=0)  # 버튼을 (2,0) 위치에 배치

# Entry (입력 필드 생성)
input = Entry(width=10)  # 너비가 10인 입력 필드 생성
print(input.get())  # 현재 입력된 값을 콘솔에 출력 (초기에는 빈 문자열 출력)
input.grid(column=3, row=2)  # 입력 필드를 (3,2) 위치에 배치

# Tkinter 이벤트 루프 실행 (GUI 유지)
window.mainloop()
