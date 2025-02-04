from tkinter import *  # Tkinter 라이브러리 가져오기

# 새로운 윈도우 생성 및 기본 설정
window = Tk()
window.title("Widget Examples")  # 윈도우 제목 설정
window.minsize(width=500, height=500)  # 최소 크기 설정

# Label (라벨 위젯 생성)
label = Label(text="This is old text")  # 기본 텍스트 설정
label.config(text="This is new text")  # 텍스트 변경
label.pack()  # 화면에 배치

# Button (버튼 위젯 생성)
def action():
    print("Do something")  # 버튼 클릭 시 출력되는 메시지

# 버튼을 클릭하면 action() 함수가 호출됨
button = Button(text="Click Me", command=action)
button.pack()  # 화면에 배치

# Entry (입력 필드 생성)
entry = Entry(width=30)  # 너비 30인 입력 필드 생성
entry.insert(END, string="Some text to begin with.")  # 기본 텍스트 삽입
print(entry.get())  # 현재 입력된 텍스트를 출력
entry.pack()  # 화면에 배치

# Text (텍스트 상자 생성)
text = Text(height=5, width=30)  # 너비 30, 높이 5인 텍스트 상자 생성
text.focus()  # 텍스트 상자에 자동으로 커서 위치
text.insert(END, "Example of multi-line text entry.")  # 기본 텍스트 삽입
print(text.get("1.0", END))  # 첫 번째 줄의 처음부터 끝까지 텍스트 가져와 출력
text.pack()  # 화면에 배치

# Spinbox (스핀박스 생성)
def spinbox_used():
    print(spinbox.get())  # 현재 선택된 값을 출력

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)  # 0부터 10까지 선택 가능한 스핀박스 생성
spinbox.pack()  # 화면에 배치

# Scale (슬라이더 생성)
def scale_used(value):
    print(value)  # 현재 슬라이더 값 출력

scale = Scale(from_=0, to=100, command=scale_used)  # 0부터 100까지 조절 가능한 슬라이더 생성
scale.pack()  # 화면에 배치

# Checkbutton (체크박스 생성)
def checkbutton_used():
    print(checked_state.get())  # 체크 상태 출력 (1: 체크됨, 0: 체크 안 됨)

checked_state = IntVar()  # 체크 상태를 저장하는 변수 (0 또는 1)
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()  # 화면에 배치

# Radiobutton (라디오 버튼 생성)
def radio_used():
    print(radio_state.get())  # 현재 선택된 라디오 버튼 값 출력

radio_state = IntVar()  # 선택된 라디오 버튼 값을 저장하는 변수
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()  # 첫 번째 라디오 버튼 배치
radiobutton2.pack()  # 두 번째 라디오 버튼 배치

# Listbox (리스트 박스 생성)
def listbox_used(event):
    print(listbox.get(listbox.curselection()))  # 현재 선택된 항목을 출력

listbox = Listbox(height=4)  # 높이가 4인 리스트 박스 생성
fruits = ["Apple", "Pear", "Orange", "Banana"]  # 리스트 항목 정의
for item in fruits:
    listbox.insert(fruits.index(item), item)  # 리스트 항목 삽입
listbox.bind("<<ListboxSelect>>", listbox_used)  # 리스트에서 항목 선택 시 이벤트 바인딩
listbox.pack()  # 화면에 배치

# Tkinter 이벤트 루프 실행 (GUI 유지)
window.mainloop()
