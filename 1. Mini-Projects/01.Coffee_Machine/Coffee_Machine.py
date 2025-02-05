MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# 현재까지 벌어들인 수익
profit = 0

# 현재 남아 있는 재료의 양
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """주문에 필요한 재료가 충분한지 확인하는 함수.
    재료가 부족하면 False를 반환하고 충분하면 True를 반환."""
    for item in order_ingredients:
        # 재료가 부족한 경우 알림 메시지 출력
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """사용자가 넣은 동전의 총액을 계산하여 반환하는 함수."""
    print("Please insert coins")
    total = int(input("how many quarters?: ")) * 0.25  # 쿼터 동전 계산 (0.25달러)
    total += int(input("how many dimes?: ")) * 0.1     # 다임 동전 계산 (0.1달러)
    total += int(input("how many nickles?: ")) * 0.05  # 니켈 동전 계산 (0.05달러)
    total += int(input("how many pennies?: ")) * 0.01  # 페니 동전 계산 (0.01달러)
    return total

def is_transaction_successful(money_received, drink_cost):
    """지불 금액이 음료 가격 이상인지 확인하는 함수.
    성공적으로 결제되면 True를 반환하고, 그렇지 않으면 False를 반환."""
    if money_received >= drink_cost:
        # 잔돈 계산
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost  # 수익 추가
        return True
    else:
        # 금액이 부족하면 환불 메시지 출력
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """음료를 만드는 함수. 사용된 재료를 재고에서 차감."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]  # 재고 차감
    print(f"Here is your {drink_name}. Enjoy!")

# 커피 머신이 켜져 있는지 확인하는 변수
is_on = True

while is_on:
    # 사용자 입력: 음료 선택
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        # 'off'를 입력하면 머신 종료
        is_on = False
    elif choice == "report":
        # 'report'를 입력하면 재료와 수익 상황 출력
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        # 사용자가 선택한 음료의 정보를 메뉴에서 가져오기
        drink = MENU.get(choice)
        if drink:
            # 재료가 충분한지 확인
            if is_resource_sufficient(drink["ingredients"]):
                # 동전 입력 처리
                payment = process_coins()
                # 결제가 성공적이면 음료 만들기
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            # 잘못된 입력 처리
            print("Invalid option. Please choose a valid drink.")
