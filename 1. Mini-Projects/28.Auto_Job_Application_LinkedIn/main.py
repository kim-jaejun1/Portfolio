from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

# 로그인 정보 및 드라이버 경로 설정
ACCOUNT_EMAIL = YOUR LOGIN EMAIL  # 본인의 이메일 입력
ACCOUNT_PASSWORD = YOUR LOGIN PASSWORD  # 본인의 비밀번호 입력
PHONE = YOUR PHONE NUMBER  # 본인의 전화번호 입력

chrome_driver_path = "C:\\Users\\user\\Downloads\\chromedriver-win64\\chromedriver.exe"  # 크롬 드라이버 경로 설정

# 웹드라이버 실행 및 링크드인 구직 페이지 접속
driver = webdriver.Chrome(chrome_driver_path)
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(2)  # 페이지 로딩 대기

# 로그인 페이지로 이동
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)  # 로그인 페이지가 로드될 시간을 확보

# 이메일 및 비밀번호 입력 후 로그인 시도
email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)  # 로그인 후 페이지 로딩 대기

# 모든 구직 공고 리스트 가져오기
all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

# 각 구직 공고에 대해 지원 진행
for listing in all_listings:
    print("called")  # 지원 프로세스가 시작됨을 알림
    listing.click()  # 공고 클릭
    time.sleep(2)  # 페이지 로딩 대기
    try:
        # '간편 지원' 버튼이 있는지 확인 후 클릭
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)  # 지원 양식이 로딩될 시간을 확보

        # 전화번호 입력 필드가 비어 있으면 입력
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        # 제출 버튼 가져오기
        submit_button = driver.find_element_by_css_selector("footer button")

        # 만약 추가 단계(복잡한 지원 절차)가 필요한 경우, 지원 취소
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()

            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")  # 복잡한 지원 절차이므로 스킵
            continue
        else:
            # 지원 제출 버튼 클릭
            submit_button.click()

        time.sleep(2)

        # 지원 완료 후 닫기 버튼 클릭
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")  # 지원 버튼이 없으면 스킵
        continue

# 일정 시간 대기 후 브라우저 종료
time.sleep(5)
driver.quit()
