from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

# Flask 애플리케이션 생성
app = Flask(__name__)
# 보안용 SECRET_KEY 설정 (CSRF 방지를 위해 필요)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# Flask-Bootstrap5 초기화 (템플릿에서 Bootstrap을 쉽게 사용 가능)
Bootstrap5(app)

# FlaskForm을 사용하여 카페 정보를 입력받을 폼 생성
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])  # 카페 이름 입력 필드
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])  # 지도 URL 입력 필드
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])  # 개점 시간 입력 필드
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])  # 폐점 시간 입력 필드
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])  # 커피 평점 선택 필드
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])  # 와이파이 강도 선택 필드
    power_rating = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])  # 콘센트 개수 선택 필드
    submit = SubmitField('Submit')  # 폼 제출 버튼

# 홈페이지 라우트 (index.html을 렌더링)
@app.route("/")
def home():
    return render_template("index.html")

# 카페 추가 페이지 라우트 (폼을 통해 데이터 입력 후 저장)
@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():  # 사용자가 폼을 올바르게 제출하면 실행
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            # 입력받은 데이터를 CSV 파일에 추가
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))  # 입력 후 'cafes' 페이지로 이동
    return render_template('add.html', form=form)  # add.html 템플릿을 렌더링

# 카페 목록 페이지 라우트 (저장된 CSV 데이터를 읽어와 표시)
@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []  # CSV 데이터를 저장할 리스트
        for row in csv_data:
            list_of_rows.append(row)  # 각 행을 리스트에 추가
    return render_template('cafes.html', cafes=list_of_rows)  # cafes.html에 데이터 전달 후 렌더링

# 애플리케이션 실행 (디버그 모드 활성화 및 포트 5002 사용)
if __name__ == '__main__':
    app.run(debug=True, port=5002)
