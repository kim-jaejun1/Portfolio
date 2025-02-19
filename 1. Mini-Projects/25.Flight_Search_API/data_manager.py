import os
from pprint import pprint
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# .env 파일에서 환경 변수를 로드
load_dotenv()


class DataManager:
    """
    Google Sheets와 연동하여 데이터를 관리하는 클래스
    """

    def __init__(self):
        # 환경 변수에서 Sheety API의 사용자명과 비밀번호를 불러옴
        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]

        # 환경 변수에서 Sheety API의 엔드포인트를 불러옴
        self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self.users_endpoint = os.environ["SHEETY_USERS_ENDPOINT"]

        # HTTP Basic 인증 설정
        self._authorization = HTTPBasicAuth(self._user, self._password)

        # 목적지 데이터 및 고객 데이터 초기화
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        """
        Google Sheets에서 목적지 데이터를 가져오는 함수
        """
        response = requests.get(url=self.prices_endpoint)
        data = response.json()  # JSON 데이터를 파싱

        # 가져온 데이터를 목적지 데이터로 저장
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        """
        목적지 데이터에서 각 도시의 IATA 코드를 업데이트하는 함수
        """
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]  # IATA 코드 업데이트
                }
            }

            # 특정 행을 업데이트하기 위해 PUT 요청 전송
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data
            )

            # 응답 결과 출력 (디버깅용)
            print(response.text)

    def get_customer_emails(self):
        """
        Google Sheets에서 고객 이메일 데이터를 가져오는 함수
        """
        response = requests.get(url=self.users_endpoint)
        data = response.json()  # JSON 데이터 파싱

        # 가져온 데이터를 고객 데이터로 저장
        self.customer_data = data["users"]
        return self.customer_data
