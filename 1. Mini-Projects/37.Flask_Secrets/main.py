from flask import Flask, render_template  # Flask 웹 프레임워크 및 템플릿 렌더링 기능 임포트
from flask_wtf import FlaskForm  # Flask-WTF(Flask용 WTForms 확장) 사용을 위한 모듈 임포트
from wtforms import StringField, PasswordField, SubmitField  # 폼 필드 타입 임포트
from wtforms.validators import DataRequired, Email, Length  # 폼 필드 유효성 검사기 임포트
from flask_bootstrap import Bootstrap5  # Flask에서 Bootstrap을 쉽게 사용할 수 있도록 도와주는 모듈

# 로그인 폼 클래스 정의
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])  # 이메일 입력 필드 (필수 입력)
    password = PasswordField('Password', validators=[DataRequired()])  # 비밀번호 입력 필드 (필수 입력)
    submit = SubmitField(label="Log In")  # 로그인 버튼

# Flask 애플리케이션 인스턴스 생성
app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"  # CSRF 보호를 위한 시크릿 키 설정

# Bootstrap5 초기화 (Flask 애플리케이션에 Bootstrap 기능 추가)
bootstrap = Bootstrap5(app)

# 홈 페이지 라우트 설정
@app.route("/")  # 기본 경로('/') 요청 시 실행
def home():
    return render_template('index.html')  # index.html 템플릿 렌더링

# 로그인 페이지 라우트 설정
@app.route("/login", methods=["GET", "POST"])  # GET 및 POST 요청 처리 가능
def login():
    login_form = LoginForm()  # 로그인 폼 인스턴스 생성
    if login_form.validate_on_submit():  # 폼이 제출되고 유효성이 확인되면 실행
        # 이메일과 비밀번호가 관리자 계정과 일치하는지 확인
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")  # 로그인 성공 시 success.html 렌더링
        else:
            return render_template("denied.html")  # 로그인 실패 시 denied.html 렌더링
    return render_template("login.html", form=login_form)  # 폼을 포함한 login.html 렌더링

# Flask 애플리케이션 실행 (디버그 모드 활성화, 포트 5001 사용)
if __name__ == '__main__':
    app.run(debug=True, port=5001)
