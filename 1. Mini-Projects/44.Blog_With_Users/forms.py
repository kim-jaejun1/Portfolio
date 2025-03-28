from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

# 블로그 게시글 작성을 위한 폼 클래스
class CreatePostForm(FlaskForm):
    # 블로그 제목 필드 (필수 입력)
    title = StringField("Blog Post Title", validators=[DataRequired()])
    # 부제목 필드 (필수 입력)
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    # 이미지 URL 필드 (필수 입력 + URL 형식 검증)
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    # 블로그 본문 내용 필드 (CKEditor 사용, 필수 입력)
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    # 제출 버튼
    submit = SubmitField("Submit Post")


# 신규 사용자 등록을 위한 폼 클래스
class RegisterForm(FlaskForm):
    # 이메일 필드 (필수 입력)
    email = StringField("Email", validators=[DataRequired()])
    # 비밀번호 필드 (필수 입력)
    password = PasswordField("Password", validators=[DataRequired()])
    # 사용자 이름 필드 (필수 입력)
    name = StringField("Name", validators=[DataRequired()])
    # 제출 버튼
    submit = SubmitField("Sign Me Up!")


# 기존 사용자 로그인을 위한 폼 클래스
class LoginForm(FlaskForm):
    # 이메일 필드 (필수 입력)
    email = StringField("Email", validators=[DataRequired()])
    # 비밀번호 필드 (필수 입력)
    password = PasswordField("Password", validators=[DataRequired()])
    # 제출 버튼
    submit = SubmitField("Let Me In!")


# 댓글 작성을 위한 폼 클래스
class CommentForm(FlaskForm):
    # 댓글 입력 필드 (CKEditor 사용, 필수 입력)
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    # 제출 버튼
    submit = SubmitField("Submit Comment")
