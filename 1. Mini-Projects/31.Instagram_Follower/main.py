from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

# Chrome WebDriver의 경로 지정
CHROME_DRIVER_PATH = "C:\\Users\\user\\Downloads\\chromedriver-win64\\chromedriver.exe"
# 팔로우할 계정
SIMILAR_ACCOUNT = "buzzfeedtasty"
# 인스타그램 로그인 정보 (사용자의 계정 정보 입력 필요)
USERNAME = YOUR
INSTAGRAM
USERNAME
PASSWORD = YOUR
INSTAGRAM
PASSWORD


class InstaFollower:
    def __init__(self, path):
        """클래스 초기화 및 Chrome WebDriver 실행"""
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        """인스타그램에 로그인하는 메서드"""
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)  # 페이지 로딩 대기

        # 사용자 이름과 비밀번호 입력란 찾기
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        # 로그인 정보 입력
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)  # 로그인 버튼 클릭

    def find_followers(self):
        """지정한 계정의 팔로워 목록을 찾고 스크롤하여 더 많은 팔로워를 로드하는 메서드"""
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")  # 대상 계정 페이지로 이동

        time.sleep(2)
        # 팔로워 목록 버튼 클릭
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        # 팔로워 목록이 표시되는 모달 창 찾기
        modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')

        # 일정 횟수만큼 스크롤 다운하여 더 많은 팔로워를 로드
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        """팔로워 목록에서 '팔로우' 버튼을 클릭하는 메서드"""
        all_buttons = self.driver.find_elements_by_css_selector("li button")  # 모든 버튼 찾기

        for button in all_buttons:
            try:
                button.click()  # 팔로우 버튼 클릭
                time.sleep(1)  # 클릭 간격 조정
            except ElementClickInterceptedException:
                # 이미 팔로우된 경우 취소 버튼을 찾아 클릭
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


# 인스타그램 봇 실행
bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
