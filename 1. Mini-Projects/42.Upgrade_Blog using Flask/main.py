# 필요한 라이브러리 불러오기
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5  # Bootstrap5 적용을 위한 플러그인
from flask_sqlalchemy import SQLAlchemy  # 데이터베이스 ORM
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm  # Flask-WTF: 폼 처리를 위한 라이브러리
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL  # 필수 입력 및 URL 검증
from flask_ckeditor import CKEditor, CKEditorField  # 에디터 적용
from datetime import date  # 오늘 날짜 가져오기

# Flask 애플리케이션 초기화
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'  # Flask-WTF를 위한 비밀키

# CKEditor, Bootstrap5 플러그인 초기화
ckeditor = CKEditor(app)
Bootstrap5(app)

# SQLAlchemy 데이터베이스 초기화 설정
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'  # SQLite 데이터베이스 파일 위치
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# 블로그 게시글 모델 정의
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # 기본 키
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)  # 제목
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)  # 부제목
    date: Mapped[str] = mapped_column(String(250), nullable=False)  # 게시 날짜
    body: Mapped[str] = mapped_column(Text, nullable=False)  # 게시글 본문
    author: Mapped[str] = mapped_column(String(250), nullable=False)  # 작성자
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)  # 이미지 URL

# 애플리케이션 시작 시 테이블 생성
with app.app_context():
    db.create_all()

# 블로그 작성용 폼 클래스 정의
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

# 메인 페이지: 모든 게시글 조회
@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))  # 모든 게시글 가져오기
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)

# 게시글 상세 페이지
@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)  # 게시글 ID로 검색, 없으면 404
    return render_template("post.html", post=requested_post)

# 새 게시글 작성 페이지
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():  # POST 요청 시 폼 유효성 검사
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=form.author.data,
            date=date.today().strftime("%B %d, %Y")  # 오늘 날짜 저장
        )
        db.session.add(new_post)  # DB에 저장
        db.session.commit()
        return redirect(url_for("get_all_posts"))  # 메인 페이지로 리디렉션
    return render_template("make-post.html", form=form)

# 게시글 수정 페이지
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    # 기존 내용을 폼에 채워서 보여줌
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        # 수정된 데이터 저장
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.author.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)  # 수정용 템플릿 렌더링

# 게시글 삭제
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# 기타 페이지: 소개 / 연락처
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# 애플리케이션 실행
if __name__ == "__main__":
    app.run(debug=True, port=5002)  # 디버그 모드로 실행, 포트 5002번 사용
