PLACEHOLDER = "[name]"  # 이름을 대체할 자리 표시자 정의

# 초대할 사람들의 이름 목록을 읽어옵니다.
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()  # 각 이름을 한 줄씩 읽어서 리스트에 저장

# 시작 편지 내용을 읽어옵니다.
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()  # 전체 편지 내용을 문자열로 읽어옴
    for name in names:  # 각 이름에 대해 반복
        stripped_name = name.strip()  # 이름에서 불필요한 공백 제거
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)  # 이름을 편지 내용에 삽입
        # 새로운 편지를 해당 이름을 포함한 파일로 저장
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)  # 편지 내용을 해당 파일에 작성
