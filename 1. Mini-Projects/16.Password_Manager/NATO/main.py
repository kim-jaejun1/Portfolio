# pandas 라이브러리를 가져옴
import pandas

# CSV 파일을 읽어서 DataFrame으로 저장
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# DataFrame을 딕셔너리로 변환
# 각 행(row)에서 'letter' 열을 키로, 'code' 열을 값으로 저장
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)  # 변환된 딕셔너리 출력


def generate_phonetic():
    """사용자가 입력한 단어를 NATO 음성 알파벳 코드로 변환하는 함수"""
    word = input("Enter a word: ").upper()  # 사용자 입력을 대문자로 변환

    try:
        # 입력된 단어의 각 글자를 phonetic_dict에서 변환하여 리스트로 저장
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        # 알파벳이 아닌 문자가 입력되었을 경우 예외 처리
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()  # 재귀 호출하여 다시 입력받기
    else:
        # 변환된 NATO 음성 알파벳 리스트 출력
        print(output_list)


# 함수 실행
generate_phonetic()
