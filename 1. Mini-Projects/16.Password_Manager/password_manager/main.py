# 필요한 라이브러리 가져오기
from tkinter import *  # GUI 생성을 위한 tkinter 라이브러리
from tkinter import messagebox  # 메시지 박스를 위한 라이브러리
from random import choice, randint, shuffle  # 랜덤한 비밀번호 생성을 위한 라이브러리
import pyperclip  # 클립보드에 비밀번호를 복사하기 위한 라이브러리

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """강력한 랜덤 비밀번호를 생성하고, 입력창에 추가 및 클립보드에 복사하는 함수"""
    # 사용할 문자, 숫자, 특수문자 리스트 정의
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("0123456789")
    symbols = list("!#$%&()*+")

    # 랜덤한 개수의 문자, 숫자, 특수문자를 선택하여 리스트 생성
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # 세 개의 리스트를 합쳐서 비밀번호 리스트를 만들고, 순서를 랜덤으로 섞음
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # 리스트를 문자열로 변환하여 최종 비밀번호 생성
    password = "".join(password_list)

    # 생성된 비밀번호를 입력창에 추가하고 클립보드에 복사
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """입력된 웹사이트, 이메일, 비밀번호 정보를 파일에 저장하는 함수"""
    website = website_entry.get()  # 웹사이트 입력값 가져오기
    email = email_entry.get()  # 이메일 입력값 가져오기
    password = password_entry.get()  # 비밀번호 입력값 가져오기

    # 필수 입력값이 비어있는지 확인
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")  # 알림창 표시
    else:
        # 입력된 정보 확인 후 저장 여부 묻기
        is_ok = messagebox.askokcancel(
            title=website, 
            message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?"
        )

        if is_ok:
            # "data.txt" 파일을 열어 입력된 정보를 저장 (추가 모드 'a' 사용)
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

            # 웹사이트와 비밀번호 입력 필드 초기화
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# 메인 윈도우 생성
window = Tk()
window.title("Password Manager")  # 창 제목 설정
window.config(padx=50, pady=50)  # 여백 설정

# 캔버스(이미지 로고 표시)
canvas = Canvas(height=200, width=200)  # 캔버스 크기 설정
logo_img = PhotoImage(file="logo.png")  # 로고 이미지 불러오기
canvas.create_image(100, 100, image=logo_img)  # 캔버스에 이미지 추가
canvas.grid(row=0, column=1)  # 위치 설정

# Labels (레이블 설정)
website_label = Label(text="Website:")  # 웹사이트 입력 필드 레이블
website_label.grid(row=1, column=0)  # 위치 설정

email_label = Label(text="Email/Username:")  # 이메일 입력 필드 레이블
email_label.grid(row=2, column=0)  # 위치 설정

password_label = Label(text="Password:")  # 비밀번호 입력 필드 레이블
password_label.grid(row=3, column=0)  # 위치 설정

# Entries (입력 필드 설정)
website_entry = Entry(width=35)  # 웹사이트 입력 필드 생성
website_entry.grid(row=1, column=1, columnspan=2)  # 위치 설정
website_entry.focus()  # 프로그램 실행 시 자동으로 커서 포커스

email_entry = Entry(width=35)  # 이메일 입력 필드 생성
email_entry.grid(row=2, column=1, columnspan=2)  # 위치 설정
email_entry.insert(0, "wowns5720@gmail.com")  # 기본 이메일 입력값 설정

password_entry = Entry(width=21)  # 비밀번호 입력 필드 생성
password_entry.grid(row=3, column=1)  # 위치 설정

# Buttons (버튼 설정)
generate_password_button = Button(text="Generate Password", command=generate_password)  # 비밀번호 생성 버튼
generate_password_button.grid(row=3, column=2)  # 위치 설정

add_button = Button(text="Add", width=36, command=save)  # 저장 버튼
add_button.grid(row=4, column=1, columnspan=2)  # 위치 설정

# Tkinter 메인 루프 실행 (GUI 창 실행)
window.mainloop()
