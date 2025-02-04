# *args는 여러 개의 위치 인수를 받을 수 있는 가변 인수이다.
def add(*args):
    # print(args[1])  # args는 튜플 형태로 전달되며, 인덱싱 가능하다.

    sum = 0  # 합계를 저장할 변수 초기화
    for n in args:  # 전달된 모든 인수를 순회하며 합산
        sum += n
    return sum  # 최종 합계 반환

# print(add(3, 5, 6, 2, 1, 7, 4, 3))  # 여러 개의 숫자를 전달하면 합을 반환


# **kwargs는 키워드 기반의 가변 인수를 받을 수 있는 딕셔너리 형태의 인자이다.
def calculate(n, **kwargs):
    print(kwargs)  # 전달된 키워드 인수들을 딕셔너리 형태로 출력
    # for key, value in kwargs.items():  # 키-값 쌍을 출력하는 코드 (주석 처리됨)
    #     print(key)
    #     print(value)

    n += kwargs["add"]  # kwargs 딕셔너리에서 "add" 키의 값을 가져와 n에 더함
    n *= kwargs["multiply"]  # "multiply" 키의 값을 가져와 n에 곱함
    # print(n)  # 계산된 값 출력 (주석 처리됨)

calculate(2, add=3, multiply=5)  
# n = 2, add=3, multiply=5가 전달됨
# 2 + 3 = 5, 5 * 5 = 25가 됨


# **kwargs를 안전하게 사용하는 방법
# 클래스에서 **kwargs를 사용할 때, .get()을 활용하면 키가 존재하지 않을 경우 None을 반환하여 에러를 방지할 수 있다.
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")  # 키가 없으면 None을 반환
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

# make과 model만 제공하고, colour과 seats는 제공되지 않음
my_car = Car(make="Nissan", model="Skyline")

print(my_car.model)  # Skyline 출력
