'''
2023.04.29
kim se yeong
#문제정의
    숫자를 입력 받아서, +x, -x, 0을 구분하는 프로그램 만들기
#문제분석
    변수-n
#알고리즘
    1. 변수 선언
        n = int(input('input number : '))
    2. 조건문
        if n > 0:
            print("+")
        elif n == 0:
            print("0")
        else:
            print("-")
'''

n = int(input("input number : "))

if n > 0:
    print("+")
elif n == 0:
    print("0")
else:
    print("-")
