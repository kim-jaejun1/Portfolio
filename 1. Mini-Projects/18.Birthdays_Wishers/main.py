# 코드를 실행하고 테스트하려면 다음 4곳을 업데이트해야 합니다:
# 1. MY_EMAIL/MY_PASSWORD를 본인의 이메일 계정 정보로 변경하세요.
# 2. 이메일 제공업체 설정에서 보안 수준이 낮은 앱의 액세스를 허용하세요.
# 3. SMTP ADDRESS를 이메일 제공업체에 맞게 업데이트하세요.
# 4. birthdays.csv 파일에 오늘의 월과 일을 포함하도록 수정하세요.
# 자세한 설명은 100 Days of Python Course의 솔루션 영상을 참고하세요.



from datetime import datetime
import pandas
import random
import smtplib

# 이메일 및 비밀번호 설정 (사용자의 이메일 계정 정보로 변경 필요)
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

# 현재 날짜 가져오기 (월, 일 정보 추출)
today = datetime.now()
today_tuple = (today.month, today.day)

# CSV 파일에서 생일 데이터 불러오기
data = pandas.read_csv("birthdays.csv")

# 생일 데이터를 딕셔너리 형태로 변환 (키: (월, 일), 값: 해당 데이터 행)
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# 오늘 생일인 사람이 있는지 확인
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]  # 오늘 생일인 사람의 정보 가져오기

    # 랜덤한 축하 편지 템플릿 선택 (letter_1.txt, letter_2.txt, letter_3.txt 중 하나)
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()

        # 편지 내용에서 [NAME]을 생일자의 이름으로 변경
        contents = contents.replace("[NAME]", birthday_person["name"])

    # 이메일 전송 (SMTP 서버 주소 변경 필요)
    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()  # 보안 연결 설정
        connection.login(MY_EMAIL, MY_PASSWORD)  # 이메일 로그인
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )  # 이메일 전송
