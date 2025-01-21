class MoneyMachine:

    # 통화 기호를 정의
    CURRENCY = "$"

    # 동전의 가치(미국 동전 기준)를 정의
    COIN_VALUES = {
        "quarters": 0.25,  # 쿼터 동전 (25센트)
        "dimes": 0.10,     # 다임 동전 (10센트)
        "nickles": 0.05,   # 니켈 동전 (5센트)
        "pennies": 0.01    # 페니 동전 (1센트)
    }

    def __init__(self):
        # 기계의 총 수익 초기화
        self.profit = 0
        # 받은 돈 초기화
        self.money_received = 0

    def report(self):
        """현재 수익을 출력합니다."""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """투입된 동전으로부터 계산된 총 금액을 반환합니다."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            # 각 동전의 개수를 입력받아 총액에 추가
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """지불이 성공하면 True를 반환하고, 부족하면 False를 반환합니다."""
        self.process_coins()  # 동전 입력 처리
        if self.money_received >= cost:
            # 지불 금액이 충분할 경우 잔돈을 계산
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            # 수익에 비용 추가
            self.profit += cost
            # 받은 돈 초기화
            self.money_received = 0
            return True
        else:
            # 지불 금액이 부족한 경우 메시지 출력 및 환불
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
