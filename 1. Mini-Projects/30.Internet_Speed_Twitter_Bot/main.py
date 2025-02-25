from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 기대하는 다운로드 및 업로드 속도 설정
PROMISED_DOWN = 150
PROMISED_UP = 10

# Chrome WebDriver 경로 설정
CHROME_DRIVER_PATH = "C:\\Users\\user\\Downloads\\chromedriver-win64\\chromedriver.exe"

# 트위터 로그인 정보 (실제 정보로 변경 필요)
TWITTER_EMAIL = "YOUR_TWITTER_EMAIL"
TWITTER_PASSWORD = "YOUR_TWITTER_PASSWORD"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        """웹 드라이버 초기화"""
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0  # 업로드 속도
        self.down = 0  # 다운로드 속도

    def get_internet_speed(self):
        """Speedtest.net에서 인터넷 속도를 측정하는 메서드"""
        self.driver.get("https://www.speedtest.net/")

        # 시작 버튼 클릭하여 테스트 실행
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()
        time.sleep(60)  # 속도 테스트가 완료될 때까지 대기

        # 업로드 및 다운로드 속도 가져오기
        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        ).text
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span'
        ).text

    def tweet_at_provider(self):
        """트위터에 인터넷 속도에 대한 불만을 트윗하는 메서드"""
        self.driver.get("https://twitter.com/login")
        time.sleep(2)

        # 이메일 및 비밀번호 입력
        email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input'
        )
        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input'
        )
        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(5)  # 로그인 대기

        # 트윗 입력 필드 찾기
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
        )

        # 불만 트윗 작성
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        # 트윗 버튼 클릭
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]'
        )
        tweet_button.click()
        time.sleep(2)

        # 드라이버 종료
        self.driver.quit()


# 봇 실행
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
