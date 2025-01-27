class Animal:
    def __init__(self):
        # 모든 Animal 객체는 기본적으로 두 개의 눈(num_eyes)을 가진다.
        self.num_eyes = 2

    def breathe(self):
        # 모든 Animal 객체는 기본적으로 "Inhale, exhale." (숨을 들이마시고 내쉼)을 출력하는 breathe 메서드를 가진다.
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        # 부모 클래스(Animal)의 __init__ 메서드를 호출하여 num_eyes 속성을 상속받는다.
        super().__init__()

    def breathe(self):
        # 부모 클래스의 breathe 메서드를 호출한다.
        super().breathe()
        # 추가로, "doing this underwater."(물속에서 이 작업을 수행 중)을 출력한다.
        print("doing this underwater.")

    def swim(self):
        # Fish 클래스는 "moving in water."(물속에서 움직임)을 출력하는 swim 메서드를 가진다.
        print("moving in water.")

# Fish 클래스의 객체를 생성하여 nemo라는 변수에 할당한다.
nemo = Fish()
# nemo 객체의 breathe 메서드를 호출하여 동작을 확인한다.
nemo.breathe()
