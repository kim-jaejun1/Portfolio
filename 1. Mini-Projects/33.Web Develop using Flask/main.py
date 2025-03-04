from flask import Flask

# Flask 애플리케이션 객체 생성
app = Flask(__name__)

# 데코레이터 함수 정의 (HTML 태그 추가 기능)
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"  # 텍스트를 굵게 표시
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"  # 텍스트를 기울임꼴로 표시
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"  # 텍스트를 밑줄 표시
    return wrapper

# 기본 루트('/')에 대한 뷰 함수 정의
@app.route('/')
def hello_world():
    # HTML 요소를 반환하여 웹 페이지 렌더링
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=200>'


# "/bye" 경로에 대해 여러 개의 데코레이터를 적용하여 스타일링
@app.route("/bye")
@make_bold  # 텍스트를 굵게
@make_emphasis  # 텍스트를 기울임꼴
@make_underlined  # 텍스트에 밑줄
def bye():
    return "Bye!"


# 변수 경로를 포함하는 라우트 (데이터 타입 변환 적용)
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    # URL에서 입력받은 name과 number를 사용하여 문자열 반환
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    # 디버그 모드로 실행하여 코드 변경 시 자동으로 서버 재시작
    app.run(debug=True)
