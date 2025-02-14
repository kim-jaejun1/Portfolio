import requests  # HTTP 요청을 보내기 위한 라이브러리
import os  # 환경 변수를 사용하기 위한 라이브러리
from twilio.rest import Client  # Twilio API를 사용하여 문자 메시지를 보내기 위한 라이브러리
from twilio.http.http_client import TwilioHttpClient  # 프록시 설정을 위한 Twilio HTTP 클라이언트

# OpenWeatherMap API의 엔드포인트 URL
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# 환경 변수에서 API 키 가져오기
api_key = os.environ.get("OWM_API_KEY")

# Twilio 계정 정보 (환경 변수에서 가져와야 보안 유지 가능)
account_sid = "YOUR ACCOUNT SID"
auth_token = os.environ.get("AUTH_TOKEN")

# 날씨 API 요청을 위한 파라미터 설정
weather_params = {
    "lat": "YOUR LATITUDE",  # 위도 입력
    "lon": "YOUR LONGITUDE",  # 경도 입력
    "appid": api_key,  # API 키
    "exclude": "current,minutely,daily"  # 필요 없는 데이터 제외 (현재, 분 단위, 일 단위 데이터 제외)
}

# OpenWeatherMap API에 GET 요청을 보내 날씨 데이터 가져오기
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()  # 응답 오류가 있으면 예외 발생
weather_data = response.json()  # 응답 데이터를 JSON 형식으로 변환

# 앞으로 12시간의 시간별 날씨 데이터 추출
weather_slice = weather_data["hourly"][:12]

# 비가 올지 여부를 판별하는 변수
will_rain = False

# 12시간 동안의 날씨 데이터에서 강수 여부 확인
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]  # 날씨 상태 코드 가져오기
    if int(condition_code) < 700:  # 기상 상태 코드가 700보다 작으면 비 또는 눈이 오는 것임
        will_rain = True

# 비가 올 경우 Twilio API를 사용하여 문자 메시지 전송
if will_rain:
    # Twilio 프록시 클라이언트 설정 (환경 변수에 프록시가 설정된 경우)
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    # Twilio 클라이언트 초기화
    client = Client(account_sid, auth_token, http_client=proxy_client)

    # 문자 메시지 생성 및 전송
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",  # 메시지 본문
        from_="YOUR TWILIO VIRTUAL NUMBER",  # Twilio 가상 번호
        to="YOUR TWILIO VERIFIED REAL NUMBER"  # 사용자의 실제 전화번호
    )

    # 메시지 전송 상태 출력
    print(message.status)
