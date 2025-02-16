import requests
from twilio.rest import Client

# Twilio 및 API 관련 정보 설정
VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"  # Twilio에서 제공하는 가상 번호
VERIFIED_NUMBER = "your own phone number verified with Twilio"  # Twilio에 인증된 본인 전화번호

# 조회할 주식 및 회사 정보
STOCK_NAME = "TSLA"  # 조회할 주식의 심볼(Tesla)
COMPANY_NAME = "Tesla Inc"  # 회사명

# API 엔드포인트 및 키 설정
STOCK_ENDPOINT = "https://www.alphavantage.co/query"  # 주식 정보 API 엔드포인트
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"  # 뉴스 API 엔드포인트

STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"  # Alpha Vantage API 키
NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"  # News API 키
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"  # Twilio 계정 SID
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"  # Twilio 인증 토큰

# STEP 1: 주식 가격 변동 감지
# 어제와 그제의 종가를 비교하여 5% 이상 변동이 있는지 확인

# 주식 데이터 요청 파라미터 설정
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

# API 요청 및 응답 데이터 저장
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]  # 일별 주식 데이터 추출

data_list = [value for (key, value) in data.items()]  # 데이터를 리스트로 변환

yesterday_data = data_list[0]  # 가장 최근 거래일(어제)의 데이터
yesterday_closing_price = yesterday_data["4. close"]  # 어제 종가
print(yesterday_closing_price)

# 그제의 종가 가져오기
day_before_yesterday_data = data_list[1]  # 두 번째 최근 거래일(그제)의 데이터
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]  # 그제 종가
print(day_before_yesterday_closing_price)

# 종가 차이 계산
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

# 주가 상승/하락 여부 표시
up_down = "🔺" if difference > 0 else "🔻"

# 변동률 계산 (절대값 사용)
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

# STEP 2: 뉴스 가져오기
# 변동률이 5% 이상이면 관련 뉴스 검색
if abs(diff_percent) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,  # 회사명이 제목에 포함된 뉴스 검색
    }

    # 뉴스 API 요청 및 응답 데이터 저장
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]  # 뉴스 기사 목록 추출

    # 첫 3개의 뉴스 기사 선택
    three_articles = articles[:3]
    print(three_articles)

    # STEP 3: Twilio를 이용한 문자 전송
    # 첫 3개의 뉴스 제목과 설명을 포함한 메시지 생성
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
        f"Headline: {article['title']}. \n"
        f"Brief: {article['description']}"
        for article in three_articles
    ]
    print(formatted_articles)

    # Twilio 클라이언트 생성
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # 각 뉴스 기사를 개별 문자 메시지로 전송
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
