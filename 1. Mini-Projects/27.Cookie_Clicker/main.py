from selenium import webdriver
import time

# 크롬 드라이버 경로 설정 (사용자의 크롬 드라이버 경로로 변경해야 함)
chrome_driver_path = "C:\\Users\\user\\Downloads\\chromedriver-win64\\chromedriver.exe"

# 웹드라이버 실행
driver = webdriver.Chrome(chrome_driver_path)

# 쿠키 클릭 게임 웹사이트 열기
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# 클릭할 쿠키 요소 가져오기
cookie = driver.find_element_by_id("cookie")

# 업그레이드 항목 ID 가져오기
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

# 5초 후 업그레이드 확인을 위한 타이머 설정
timeout = time.time() + 5
# 5분 후 실행 중지
total_runtime = time.time() + 60 * 5  # 5분

while True:
    # 쿠키 클릭
    cookie.click()

    # 5초마다 업그레이드 구매 시도
    if time.time() > timeout:

        # 상점의 모든 업그레이드 가격 가져오기
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        # 가격 정보를 정수형으로 변환
        for price in all_prices:
            element_text = price.text
            if element_text != "":  # 빈 문자열이 아닐 경우
                cost = int(element_text.split("-")[1].strip().replace(",", ""))  # 가격 추출 후 정수 변환
                item_prices.append(cost)

        # 업그레이드 아이템과 가격을 매칭하여 딕셔너리 생성
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # 현재 보유한 쿠키 개수 가져오기
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # 구매할 수 있는 업그레이드 찾기
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # 가장 비싼 구매 가능한 업그레이드 선택
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)  # 구매 가격 출력
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        # 해당 업그레이드 구매
        driver.find_element_by_id(to_purchase_id).click()

        # 다음 업그레이드 확인 시간 설정 (5초 후)
        timeout = time.time() + 5

    # 5분이 지나면 실행 종료 및 초당 쿠키 생산량 확인
    if time.time() > total_runtime:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)  # 초당 생산되는 쿠키 수 출력
        break
