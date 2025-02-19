import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# Amadeus API 엔드포인트 정의
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:

    def __init__(self):
        """
        FlightSearch 클래스의 생성자로, Amadeus API와 통신하기 위한 초기 설정을 수행합니다.

        인스턴스 변수:
        - _api_key (str): Amadeus API 인증을 위한 API 키
        - _api_secret (str): Amadeus API 인증을 위한 비밀 키
        - _token (str): Amadeus API에서 획득한 인증 토큰
        """
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_SECRET"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        """
        Amadeus API에서 새 인증 토큰을 요청하는 함수

        Returns:
            str: API에서 획득한 새로운 액세스 토큰
        """
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        return response.json()['access_token']

    def get_destination_code(self, city_name):
        """
        주어진 도시 이름에 대한 IATA 공항 코드를 검색하는 함수

        Parameters:
        city_name (str): 검색할 도시 이름

        Returns:
        str: 해당 도시의 IATA 코드, 없을 경우 "N/A" 또는 "Not Found" 반환
        """
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {"keyword": city_name, "max": "2", "include": "AIRPORTS"}
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)
        try:
            return response.json()["data"][0]['iataCode']
        except IndexError:
            return "N/A"
        except KeyError:
            return "Not Found"

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):
        """
        두 도시 간 항공편을 검색하는 함수

        Parameters:
        - origin_city_code (str): 출발 도시의 IATA 코드
        - destination_city_code (str): 도착 도시의 IATA 코드
        - from_time (datetime): 출발 날짜
        - to_time (datetime): 귀국 날짜
        - is_direct (bool): 직항 여부 (기본값: True)

        Returns:
        dict or None: API 응답 데이터를 포함한 딕셔너리 또는 오류 발생 시 None 반환
        """
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": "10",
        }
        response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=query)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            return None
        return response.json()
