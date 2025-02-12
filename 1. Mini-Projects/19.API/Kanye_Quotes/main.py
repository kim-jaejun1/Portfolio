from tkinter import *  # Tkinter 라이브러리 임포트
import requests  # HTTP 요청을 위한 requests 라이브러리 임포트


def get_quote():
    """
    Kanye API에서 명언을 가져와서 캔버스의 텍스트를 업데이트하는 함수
    """
    response = requests.get("https://api.kanye.rest")  # API 요청
    response.raise_for_status()  # 오류 발생 시 예외 발생
    data = response.json()  # JSON 응답을 파싱
    quote = data["quote"]  # 명언 추출
    canvas.itemconfig(quote_text, text=quote)  # 캔버스의 텍스트 업데이트


# Tkinter 윈도우 생성
window = Tk()
window.title("Kanye Says...")  # 윈도우 제목 설정
window.config(padx=50, pady=50)  # 여백 설정

# 캔버스 생성 (배경 이미지 및 명언 표시)
canvas = Canvas(width=300, height=414)  # 캔버스 크기 설정
background_img = PhotoImage(file="background.png")  # 배경 이미지 로드
canvas.create_image(150, 207, image=background_img)  # 캔버스에 이미지 배치
quote_text = canvas.create_text(
    150, 207, text="Kanye Quote Goes HERE", width=250,
    font=("Arial", 30, "bold"), fill="white"
)  # 명언이 표시될 텍스트 객체 생성
canvas.grid(row=0, column=0)  # 캔버스를 윈도우 그리드에 배치

# Kanye 버튼 생성
kanye_img = PhotoImage(file="kanye.png")  # 버튼에 사용할 이미지 로드
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)  # 버튼 생성 (클릭 시 get_quote 실행)
kanye_button.grid(row=1, column=0)  # 버튼을 윈도우 그리드에 배치

# Tkinter 메인 루프 실행 (GUI 실행)
window.mainloop()
