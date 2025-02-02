# 학생들의 이름과 점수를 담은 딕셔너리 생성
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# 딕셔너리를 순회하며 각 키와 값에 접근
for (key, value) in student_dict.items():
    # 각 key와 value를 사용하여 원하는 작업 수행
    pass

import pandas  # 데이터 처리를 위한 pandas 라이브러리 불러오기

# 학생 정보를 담은 딕셔너리를 DataFrame으로 변환
student_data_frame = pandas.DataFrame(student_dict)

# DataFrame의 각 행(row)을 순회하며 인덱스와 행 데이터에 접근
for (index, row) in student_data_frame.iterrows():
    # 인덱스(index)와 행(row)에 접근 가능
    # 예: row.student 또는 row.score 로 학생 이름과 점수에 접근
    pass

# iterrows()를 사용한 딕셔너리 생성의 키워드 방식 예시
# {new_key: new_value for (index, row) in df.iterrows()}

# TODO 1. 다음 형식의 딕셔너리를 생성하세요:
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. 사용자로부터 단어를 입력받아 해당하는 NATO 음성 알파벳 코드 단어들의 리스트를 생성하세요.
