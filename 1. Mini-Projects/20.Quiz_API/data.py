import requests  # requests 라이브러리를 가져옴 (HTTP 요청을 보낼 때 사용)

# API 요청에 사용할 매개변수 설정
parameters = {
    "amount": 10,  # 가져올 문제 개수 (10개)
    "type": "boolean",  # 문제 유형 (True/False 형식)
}

# Open Trivia Database API에서 퀴즈 데이터를 가져오는 GET 요청을 보냄
response = requests.get("https://opentdb.com/api.php", params=parameters)

# 응답이 정상인지 확인하고, 오류 발생 시 예외를 발생시킴
response.raise_for_status()

# 응답 데이터를 JSON 형식으로 변환
data = response.json()

# 퀴즈 문제 데이터 추출 (JSON의 "results" 키에 해당하는 값)
question_data = data["results"]
