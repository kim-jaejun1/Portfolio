from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 필요한 객체 생성
money_machine = MoneyMachine()  # 금전 처리기 객체
coffee_maker = CoffeeMaker()  # 커피 제조기 객체
menu = Menu()  # 메뉴 객체

is_on = True  # 커피 머신이 작동 중인지 여부를 나타내는 플래그

while is_on:
    # 사용자에게 메뉴 옵션을 표시하고 선택을 입력받음
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        # "off" 입력 시 프로그램 종료
        is_on = False
    elif choice == "report":
        # "report" 입력 시 현재 기계 상태와 수익 출력
        coffee_maker.report()
        money_machine.report()
    else:
        # 사용자가 선택한 음료 검색
        drink = menu.find_drink(choice)

        if drink:
            # 자원이 충분하고 지불이 완료되면 음료를 제조
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)