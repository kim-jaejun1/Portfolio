import requests  # HTTP 요청을 보내기 위한 라이브러리
from datetime import datetime  # 현재 날짜를 가져오기 위한 라이브러리

# Pixela API에 필요한 사용자 정보 설정
USERNAME = "YOUR USERNAME"  # 사용자명
TOKEN = "YOUR SELF GENERATED TOKEN"  # 사용자가 직접 생성한 토큰
GRAPH_ID = "YOUR GRAPH ID"  # 그래프 ID

# Pixela 사용자 생성 API 엔드포인트
pixela_endpoint = "https://pixe.la/v1/users"

# 사용자 생성 요청에 필요한 데이터
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",  # 서비스 약관 동의
    "notMinor": "yes",  # 성인 여부 확인
}

## POST 요청: 사용자 계정 생성 (한 번만 실행하면 됨)
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)  # 응답 출력

# 그래프 생성 API 엔드포인트
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# 그래프 설정 데이터
graph_config = {
    "id": GRAPH_ID,  # 그래프 ID
    "name": "Cycling Graph",  # 그래프 이름
    "unit": "Km",  # 측정 단위 (킬로미터)
    "type": "float",  # 데이터 타입 (소수점 허용)
    "color": "ajisai"  # 그래프 색상 (보라색 계열)
}

# API 요청에 필요한 헤더 (인증을 위한 토큰 포함)
headers = {
    "X-USER-TOKEN": TOKEN
}

## POST 요청: 그래프 생성 (한 번만 실행하면 됨)
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)  # 응답 출력

# 픽셀(데이터 포인트) 생성 API 엔드포인트
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# 현재 날짜 가져오기
today = datetime.now()
# print(today.strftime("%Y%m%d"))  # 날짜 포맷 확인

# 사용자 입력을 받아 픽셀 데이터 설정
pixel_data = {
    "date": today.strftime("%Y%m%d"),  # YYYYMMDD 형식의 날짜
    "quantity": input("How many kilometers did you cycle today? ")  # 사용자 입력 값
}

# POST 요청: 픽셀(운동 데이터) 추가
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)  # 응답 출력

# 픽셀 업데이트(수정) API 엔드포인트
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# 새로운 픽셀 데이터 (예: 4.5km로 수정)
new_pixel_data = {
    "quantity": "4.5"
}

## PUT 요청: 기존 픽셀 데이터 수정
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)  # 응답 출력

# 픽셀 삭제 API 엔드포인트
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

## DELETE 요청: 픽셀 데이터 삭제
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)  # 응답 출력
