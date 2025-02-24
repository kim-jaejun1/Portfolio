from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

# Facebook 로그인 정보 설정
FB_EMAIL = YOUR_FACEBOOK_LOGIN_EMAIL  # 사용자의 Facebook 이메일
FB_PASSWORD = YOUR_FACEBOOK_PASSWORD  # 사용자의 Facebook 비밀번호

# Chrome WebDriver 경로 설정
chrome_driver_path = "C:\\Users\\user\\Downloads\\chromedriver-win64\\chromedriver.exe"  # ChromeDriver의 경로

# Selenium을 사용하여 Chrome 브라우저 실행
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Tinder 웹사이트 열기
driver.get("http://www.tinder.com")
sleep(2)  # 페이지 로딩을 위해 대기

# 로그인 버튼 클릭
login_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login_button.click()
sleep(2)  # 로그인 페이지가 로딩될 시간을 기다림

# Facebook 로그인 버튼 클릭
fb_login = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()
sleep(2)  # Facebook 로그인 창이 뜨기를 기다림

# 현재 윈도우 핸들 저장
base_window = driver.window_handles[0]  # Tinder 메인 창
fb_login_window = driver.window_handles[1]  # Facebook 로그인 창

# Facebook 로그인 창으로 전환
driver.switch_to.window(fb_login_window)
print(driver.title)  # Facebook 로그인 창의 제목 출력

# Facebook 로그인 정보 입력
email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')

email.send_keys(FB_EMAIL)  # 이메일 입력
password.send_keys(FB_PASSWORD)  # 비밀번호 입력
password.send_keys(Keys.ENTER)  # 로그인 버튼 클릭 (Enter 키 입력)

# 다시 Tinder 창으로 전환
driver.switch_to.window(base_window)
print(driver.title)  # Tinder 메인 창의 제목 출력

sleep(5)  # 페이지가 로드될 시간을 기다림

# 위치 허용 버튼 클릭
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

# 알림 거부 버튼 클릭
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

# 쿠키 허용 버튼 클릭
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

# 100번 자동으로 "좋아요" 클릭 반복
for n in range(100):
    sleep(1)  # 각 클릭 사이의 간격을 두기 위해 대기
    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()  # "좋아요" 버튼 클릭
    except ElementClickInterceptedException:
        try:
            # 매칭이 되었을 경우, 팝업 창이 뜨므로 닫기
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)  # 팝업이 없으면 2초 대기 후 다시 시도

# 모든 작업이 끝난 후 브라우저 종료
driver.quit()
