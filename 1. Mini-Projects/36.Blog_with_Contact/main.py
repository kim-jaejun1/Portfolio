from flask import Flask, render_template, request
import smtplib
import requests

app = Flask(__name__)

# 외부 JSON 데이터를 가져와 블로그 게시글 목록을 저장
# 자신의 npoint API 링크를 사용하여 게시글 데이터를 가져와야 함
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

# 이메일 전송을 위한 본인의 이메일 및 비밀번호 설정 (보안상의 이유로 환경 변수 사용 권장)
OWN_EMAIL = "YOUR OWN EMAIL ADDRESS"
OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"

# 메인 페이지 라우트
@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)  # 모든 게시글을 렌더링하여 index.html에 전달

# 'About' 페이지 라우트
@app.route("/about")
def about():
    return render_template("about.html")  # about.html 페이지 렌더링

# 'Contact' 페이지 라우트 (GET, POST 메서드 허용)
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form  # 사용자가 제출한 폼 데이터 가져오기
        send_email(data["name"], data["email"], data["phone"], data["message"])  # 이메일 전송 함수 호출
        return render_template("contact.html", msg_sent=True)  # 메일 전송 성공 메시지 포함하여 contact.html 렌더링
    return render_template("contact.html", msg_sent=False)  # 기본적으로 msg_sent=False 설정

# 이메일 전송 함수
def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # 보안 연결 설정
        connection.login(OWN_EMAIL, OWN_PASSWORD)  # 이메일 로그인
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)  # 본인 이메일로 메일 전송

# 개별 블로그 게시글 페이지 라우트 (동적 경로)
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post  # 요청된 ID와 일치하는 게시글 찾기
    return render_template("post.html", post=requested_post)  # 찾은 게시글을 post.html로 렌더링

# Flask 애플리케이션 실행
if __name__ == "__main__":
    app.run(debug=True)  # 디버그 모드로 실행
