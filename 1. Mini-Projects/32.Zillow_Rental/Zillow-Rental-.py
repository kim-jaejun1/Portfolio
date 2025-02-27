from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

# 웹 스크래핑을 위한 헤더 설정 (사이트가 봇을 차단하는 것을 방지하기 위함)
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Zillow 웹사이트에서 특정 조건의 매물 정보를 가져오기 위한 요청
response = requests.get(
    "https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
    headers=header)

# HTML 데이터 파싱
data = response.text
soup = BeautifulSoup(data, "html.parser")

# 매물의 링크 가져오기
all_link_elements = soup.select(".list-card-top a")
all_links = []
for link in all_link_elements:
    href = link["href"]
    print(href)
    # 절대 경로가 아닌 경우 기본 URL 추가
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

# 매물 주소 가져오기
all_address_elements = soup.select(".list-card-info address")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

# 매물 가격 가져오기
all_price_elements = soup.select(".list-card-heading")
all_prices = []
for element in all_price_elements:
    try:
        # 단일 매물 가격 가져오기
        price = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        print('Multiple listings for the card')
        # 여러 매물이 포함된 경우 가격 가져오기
        price = element.select(".list-card-details li")[0].contents[0]
    finally:
        all_prices.append(price)

# Chrome WebDriver 경로 설정
chrome_driver_path = "C:\\Users\\user\\Downloads\\chromedriver-win64\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# 구글 폼에 자동 입력하는 과정
for n in range(len(all_links)):
    driver.get(URL_TO_YOUR_GOOGLE_FORM)  # 구글 폼 링크로 이동

    time.sleep(2)  # 페이지 로딩을 위해 대기

    # 폼 필드 요소 찾기
    address = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    # 데이터 입력
    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])

    # 폼 제출 버튼 클릭
    submit_button.click()
