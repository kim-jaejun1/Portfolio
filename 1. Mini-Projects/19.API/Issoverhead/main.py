import requests
from datetime import datetime
import smtplib
import time

# 이메일 및 위치 정보 설정
MY_EMAIL = "___YOUR_EMAIL_HERE____"  # 본인의 이메일 입력
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"  # 본인의 이메일 비밀번호 입력
MY_LAT = 51.507351  # 본인의 위도 입력
MY_LONG = -0.127758  # 본인의 경도 입력


def is_iss_overhead():
    """
    국제우주정거장(ISS)의 현재 위치를 가져와서 사용자의 위치 근처에 있는지 확인하는 함수
    """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")  # ISS 현재 위치 API 요청
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])  # ISS 위도 가져오기
    iss_longitude = float(data["iss_position"]["longitude"])  # ISS 경도 가져오기

    # 사용자의 위치가 ISS의 위치로부터 ±5도 이내에 있는지 확인
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    """
    현재 시간이 밤인지 확인하는 함수
    """
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)  # 일출 및 일몰 시간 API 요청
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])  # 일출 시간 가져오기
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])  # 일몰 시간 가져오기

    time_now = datetime.now().hour  # 현재 시간 가져오기

    # 현재 시간이 일몰 이후이거나 일출 이전이면 밤으로 간주
    if time_now >= sunset or time_now <= sunrise:
        return True

# 1분마다 ISS 위치와 밤 여부를 확인
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():  # ISS가 머리 위에 있고 밤이라면
        connection = smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___")  # SMTP 서버에 연결
        connection.starttls()  # 보안 연결 활성화
        connection.login(MY_EMAIL, MY_PASSWORD)  # 이메일 로그인
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."  # 이메일 전송
        )
