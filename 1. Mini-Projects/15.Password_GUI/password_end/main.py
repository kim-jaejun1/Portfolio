from tkinter import *  # Tkinter GUI 라이브러리
from tkinter import messagebox  # 알림 창을 위한 messagebox
from random import choice, randint, shuffle  # 랜덤한 비밀번호 생성을 위한 라이브러리
import pyperclip  # 클립보드에 비밀번호를 자동 복사하기 위한 라이브러리


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """무작위로 생성된 보안 비밀번호를 입력 필드에 추가하고 클립보드에 복사하는 함수"""
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # 랜덤한 문자, 숫자, 특수문자 선택
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # 비밀번호 리스트 생성 및 섞기
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # 리스트를 문자열로 변환 후 입력 필드에 삽입
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)  # 비밀번호를 클립보드에 복사


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """입력된 웹사이트, 이메일, 비밀번호 정보를 파일에 저장하는 함수"""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # 필드가 비어 있는지 확인
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        # 사용자 확인 메시지 출력
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:  # data.txt 파일에 정보 추가
                data_file.write(f"{website} | {email} | {password}\n")

                # 입력 필드 초기화
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")  # 창 제목 설정
window.config(padx=50, pady=50)  # 여백 설정

# 캔버스를 이용해 로고 삽입
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels (레이블 생성 및 배치)
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries (입력 필드 생성 및 배치)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # 프로그램 실행 시 웹사이트 입력창에 자동 포커스

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")  # 기본 이메일 주소 입력

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons (버튼 생성 및 배치)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# GUI 실행
window.mainloop()
