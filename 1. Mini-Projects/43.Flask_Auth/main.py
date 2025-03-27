# 필요한 라이브러리 import
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# Flask 앱 생성
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'  # 세션 보호용 시크릿 키 설정

# SQLAlchemy의 베이스 클래스 정의
class Base(DeclarativeBase):
    pass

# 데이터베이스 URI 설정 (SQLite 사용)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)  # 커스텀 베이스 사용
db.init_app(app)  # Flask 앱에 SQLAlchemy 연동

# Flask-Login 초기화
login_manager = LoginManager()
login_manager.init_app(app)

# 유저 정보 로드 함수 (Flask-Login이 로그인 상태 유지에 사용)
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# 유저 모델 정의 (UserMixin을 통해 Flask-Login과 연동)
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)  # 이메일은 고유해야 함
    password: Mapped[str] = mapped_column(String(100))  # 해시된 비밀번호 저장
    name: Mapped[str] = mapped_column(String(1000))  # 유저 이름

# 앱 실행 컨텍스트 내에서 테이블 생성
with app.app_context():
    db.create_all()

# 홈페이지 라우트
@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)

# 회원가입 라우트
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get('email')

        # 이메일 중복 확인
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        if user:
            flash("이미 가입된 이메일입니다. 로그인 해주세요!")
            return redirect(url_for('login'))

        # 비밀번호 해싱
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        # 새 유저 생성
        new_user = User(
            email=email,
            password=hash_and_salted_password,
            name=request.form.get('name'),
        )
        # DB에 저장
        db.session.add(new_user)
        db.session.commit()
        # 회원가입 후 자동 로그인
        login_user(new_user)
        return redirect(url_for("secrets"))

    return render_template("register.html", logged_in=current_user.is_authenticated)

# 로그인 라우트
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        if not user:
            flash("존재하지 않는 이메일입니다.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('비밀번호가 틀렸습니다.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html", logged_in=current_user.is_authenticated)

# 비밀 페이지 (로그인한 유저만 접근 가능)
@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)  # 콘솔에 유저 이름 출력
    return render_template("secrets.html", name=current_user.name, logged_in=True)

# 로그아웃
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# 파일 다운로드 라우트
@app.route('/download')
@login_required
def download():
    # static/files/cheat_sheet.pdf 파일을 유저에게 전송
    return send_from_directory('static', path="files/cheat_sheet.pdf")

# 앱 실행
if __name__ == "__main__":
    app.run(debug=True)  # 디버그 모드로 실행 (개발 시에만 사용)
