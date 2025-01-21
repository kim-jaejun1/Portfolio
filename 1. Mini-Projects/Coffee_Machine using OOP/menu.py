class MenuItem:
    """각 메뉴 항목을 모델링합니다."""
    def __init__(self, name, water, milk, coffee, cost):
        # 음료 이름 초기화
        self.name = name
        # 음료 가격 초기화
        self.cost = cost
        # 음료에 필요한 재료 초기화
        self.ingredients = {
            "water": water,   # 필요한 물의 양 (ml)
            "milk": milk,     # 필요한 우유의 양 (ml)
            "coffee": coffee  # 필요한 커피의 양 (g)
        }


class Menu:
    """메뉴와 음료 항목들을 모델링합니다."""
    def __init__(self):
        # 메뉴 항목 리스트 초기화
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),  # 라떼 항목 추가
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),  # 에스프레소 항목 추가
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),  # 카푸치노 항목 추가
        ]

    def get_items(self):
        """사용 가능한 모든 메뉴 항목의 이름을 반환합니다."""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"  # 항목 이름을 문자열에 추가
        return options

    def find_drink(self, order_name):
        """특정 이름의 음료를 메뉴에서 검색합니다. 존재하면 해당 항목을 반환하고, 없으면 None을 반환합니다."""
        for item in self.menu:
            if item.name == order_name:  # 주문 이름과 항목 이름이 일치하는지 확인
                return item
        print("Sorry that item is not available.")  # 해당 항목이 없을 경우 메시지 출력
