from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# Flask 애플리케이션 생성
app = Flask(__name__)


# SQLAlchemy의 기본 클래스를 정의 (Declarative Base 생성)
class Base(DeclarativeBase):
    pass


# SQLite 데이터베이스 설정 (books.db 사용)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"

# SQLAlchemy 확장 생성 및 초기화
# model_class=Base를 사용하여 선언적 클래스를 기반으로 설정
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# 데이터베이스의 테이블(Book) 모델 정의
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # 기본 키 (ID)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)  # 책 제목 (고유값, NULL 불가)
    author: Mapped[str] = mapped_column(String(250), nullable=False)  # 저자 (NULL 불가)
    rating: Mapped[float] = mapped_column(Float, nullable=False)  # 평점 (NULL 불가)


# Flask 애플리케이션 컨텍스트에서 데이터베이스 테이블 생성
with app.app_context():
    db.create_all()


# 홈페이지 라우트 설정 (모든 책 목록 표시)
@app.route('/')
def home():
    # 데이터베이스에서 모든 책을 조회하여 제목 기준으로 정렬
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()  # 데이터베이스 행에서 객체만 추출
    return render_template("index.html", books=all_books)  # index.html에 데이터 전달


# 새로운 책 추가 페이지 및 기능
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # 폼에서 데이터 가져와 새 책 객체 생성
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)  # 데이터베이스에 추가
        db.session.commit()  # 변경 사항 저장
        return redirect(url_for('home'))  # 홈 페이지로 리디렉트
    return render_template("add.html")  # GET 요청 시 추가 페이지 렌더링


# 책 평점 수정 기능
@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # 수정할 책의 ID 가져오기
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)  # 해당 책 조회
        book_to_update.rating = request.form["rating"]  # 새로운 평점 설정
        db.session.commit()  # 변경 사항 저장
        return redirect(url_for('home'))  # 홈 페이지로 리디렉트

    # GET 요청 시 수정할 책 정보 가져오기
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit_rating.html", book=book_selected)  # 수정 페이지 렌더링


# 책 삭제 기능
@app.route("/delete")
def delete():
    book_id = request.args.get('id')  # 삭제할 책의 ID 가져오기
    book_to_delete = db.get_or_404(Book, book_id)  # 해당 책 조회
    db.session.delete(book_to_delete)  # 데이터베이스에서 삭제
    db.session.commit()  # 변경 사항 저장
    return redirect(url_for('home'))  # 홈 페이지로 리디렉트


# Flask 애플리케이션 실행
if __name__ == "__main__":
    app.run(debug=True)  # 디버그 모드 활성화
