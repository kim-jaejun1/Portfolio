from flask import Flask

# Flask 애플리케이션 객체 생성
app = Flask(__name__)

# 데코레이터: HTML 태그 추가 기능 구현

def make_bold(function):
    """ 함수의 반환값을 <b> 태그로 감싸서 굵게 표시 """
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    """ 함수의 반환값을 <em> 태그로 감싸서 이탤릭체로 표시 """
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    """ 함수의 반환값을 <u> 태그로 감싸서 밑줄을 추가 """
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

# 루트 경로('/')에서 실행될 함수 정의
@app.route('/')
def hello_world():

    """ 웹 페이지의 기본 화면을 렌더링 """
            # 제목 태그
    return '<h1 style="text-align: center">Hello, World!</h1>' \
            # 단락 태그
           '<p>This is a paragraph.</p>' \
            # 이미지 삽입
           '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=200>'

# '/bye' 경로에서 실행될 함수 정의
@app.route("/bye")
@make_bold  # 굵은 글씨 적용
@make_emphasis  # 이탤릭체 적용
@make_underlined  # 밑줄 적용
def bye():
    """ 'Bye!' 문자열을 HTML 태그로 감싸 변형된 상태로 반환 """
    return "Bye!"

# 동적 URL 경로 설정 (변수를 포함하는 경로)
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    """ 'username' 경로에서 사용자 이름과 숫자를 입력받아 출력 """
    return f"Hello there {name}, you are {number} years old!"

# Flask 애플리케이션 실행
if __name__ == "__main__":
    # 디버그 모드 활성화 (코드 변경 시 자동으로 서버 재시작)
    app.run(debug=True)
