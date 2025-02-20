import requests
from bs4 import BeautifulSoup

# 웹 스크래핑할 대상 URL (Wayback Machine에서 저장된 과거 페이지 사용)
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# 지정한 URL에서 HTML 데이터를 가져옴
response = requests.get(URL)
website_html = response.text  # 응답 데이터를 텍스트 형태로 저장

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(website_html, "html.parser")

# 모든 영화 제목을 포함하는 <h3> 태그를 찾음 (class 속성이 "title"인 요소)
all_movies = soup.find_all(name="h3", class_="title")

# 찾은 영화 제목을 리스트로 저장 (getText()로 텍스트만 추출)
movie_titles = [movie.getText() for movie in all_movies]

# 리스트를 역순으로 정렬 (웹사이트에서 1위가 마지막에 위치하기 때문)
movies = movie_titles[::-1]

# movies.txt 파일을 생성하여 영화 제목을 저장
with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")  # 각 영화 제목을 한 줄씩 파일에 저장

'''
FAQ: Empire의 웹사이트가 변경되었습니다!

이 코드가 작성될 당시 사용된 원래 URL:
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

하지만 이후 Empire의 웹사이트가 변경되어 h3 태그의 "title" 클래스가 존재하지 않게 되었습니다.
따라서 동일한 코드를 사용하려면 Internet Archive의 Wayback Machine에서 저장된 과거 웹사이트 버전을 이용해야 합니다.
'''
