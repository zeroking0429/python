'''
2023.04.29
kim se yeong
조건이 여러 개인 경우의 조건문 연습
#문제 정의
    점수가 90이상이면 "A"
    전수가 80이상이 90미만 이면 "B"
    점수가 70이상이 80미만 이면 "C"
    점수가 70미만이면 "F"를 출력하는 프로그램
#문제 분석
    변수-score
#알고리즘
    1. 변수 선언 
        score = int(input('input score : '))
    2. 조건문
        if score >= 90:
            print("A")
        elif score >= 80:
            print("B")
        elif score >= 70:
            print("C")
        else:
            print("F")
'''

score = int(input('input score : '))

if score >= 90: # 조건식1
    print("A") # True
elif score >= 80: # 조건식2
    print("B") # 조건1 False 조건2 True
elif score >= 70: # 조건식3
    print("C") # 조건1 False 조건2 False 조건3 True
else: # all False
    print("F")
