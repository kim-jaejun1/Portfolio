class CoffeeMaker:
    """커피를 만드는 기계를 모델링합니다."""
    def __init__(self):
        # 기계의 초기 자원 상태 설정
        self.resources = {
            "water": 300,  # 초기 물의 양 (ml)
            "milk": 200,   # 초기 우유의 양 (ml)
            "coffee": 100, # 초기 커피의 양 (g)
        }

    def report(self):
        """현재 자원의 상태를 출력합니다."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """주문을 처리할 수 있는지 확인합니다. 자원이 충분하면 True를 반환, 부족하면 False를 반환합니다."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")  # 자원이 부족한 경우 메시지 출력
                can_make = False
        return can_make

    def make_coffee(self, order):
        """필요한 재료를 자원에서 차감하고 음료 제조를 완료합니다."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]  # 각 재료 차감
        print(f"Here is your {order.name} ☕️. Enjoy!")