# Password Generator Project (비밀번호 생성기 프로젝트)
import random  # 랜덤한 요소를 선택하고 섞기 위한 random 모듈 임포트

# 비밀번호를 구성할 문자, 숫자, 특수문자 리스트
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# 랜덤한 개수의 문자, 숫자, 특수문자 선택
nr_letters = random.randint(8, 10)  # 8~10개의 문자 선택
nr_symbols = random.randint(2, 4)   # 2~4개의 특수문자 선택
nr_numbers = random.randint(2, 4)   # 2~4개의 숫자 선택

# 비밀번호를 저장할 리스트 초기화
password_list = []

# 랜덤한 문자 추가
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# 랜덤한 특수문자 추가
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# 랜덤한 숫자 추가
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# 비밀번호 리스트를 무작위로 섞음
random.shuffle(password_list)

# 리스트를 문자열로 변환하여 최종 비밀번호 생성
password = "".join(password_list)

# 생성된 비밀번호 출력
print(f"Your password is: {password}")
