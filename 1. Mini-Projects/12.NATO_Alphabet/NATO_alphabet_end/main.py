import pandas  # 데이터 처리를 위한 pandas 라이브러리 불러오기

# CSV 파일(nato_phonetic_alphabet.csv)을 읽어서 데이터프레임(data)에 저장
# CSV 파일에는 'letter'와 'code'라는 열이 있어야 함.
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# 데이터프레임의 각 행을 순회하며, 각 문자(letter)를 키로, 대응하는 코드(code)를 값으로 하는 딕셔너리 생성
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# 생성된 NATO 음성 알파벳 딕셔너리를 출력
print(phonetic_dict)

# 사용자로부터 단어를 입력받고, 대문자로 변환 (딕셔너리의 키와 맞추기 위함)
word = input("단어를 입력하세요: ").upper()

# 입력받은 단어의 각 글자에 대해 해당하는 NATO 코드 단어를 찾아 리스트에 저장
output_list = [phonetic_dict[letter] for letter in word]

# 결과 리스트 출력
print(output_list)
