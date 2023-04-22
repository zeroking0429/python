'''
2023-04-22
kim se yeong
# 문제
    반지름이 5인 원의 넓이 구하기
# 문제분석
    변수-반지름(radius), 원의 넓이(area)
    수식-area = (radius ** 2) * 3.141592653589793238
# 알고리즘
    1.변수 선언
        radius = 5
    2.원의 넓이 계산
        area = (radius ** 2) * 3.141592653589793238
    3.출력
'''
radius = 10
area = (radius ** 2) * 3.141592653589793238
print("반지름이 {}인 원의 넓이는 {}이다.".format(radius, area))