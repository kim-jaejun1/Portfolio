import colorgram  # colorgram 모듈을 임포트하여 이미지에서 색상 추출 기능 사용

# 'sweet_pic.jpg' 이미지에서 6개의 주요 색상을 추출
colors = colorgram.extract('sweet_pic.jpg', 6)

# colorgram.extract는 Color 객체를 반환하며, 이 객체를 통해
# RGB, HSL 값과 해당 색상이 이미지에서 차지하는 비율에 접근할 수 있음
first_color = colors[0]  # 추출된 색상 목록에서 첫 번째 색상을 선택

# 첫 번째 색상의 RGB 값에 접근 (예: (255, 151, 210))
rgb = first_color.rgb

# 첫 번째 색상의 HSL 값에 접근 (예: (230, 255, 203))
hsl = first_color.hsl

# 첫 번째 색상이 이미지에서 차지하는 비율 (예: 0.34)
proportion = first_color.proportion

# RGB와 HSL은 namedtuple로 되어 있어, 속성으로 값을 쉽게 접근할 수 있음
# 아래의 두 코드는 같은 의미
red = rgb[0]  # RGB 값의 첫 번째 요소 (빨간색 값)
red = rgb.r   # namedtuple 방식으로 빨간색 값에 접근

# HSL 값의 두 번째 요소 (채도) 값에 접근
saturation = hsl[1]  # 채도 값
saturation = hsl.s   # namedtuple 방식으로 채도 값에 접근
