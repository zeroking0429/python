'''
2023.04.29
kim se yeong
#문제정의
    숫자를 입력 받아서, +x, -x, 0을 구분하는 프로그램 만들기
#문제분석
    변수-com, user
#알고리즘
    1. 변수 선언
        com = 17
        user = int(input('up-down game - input number : '))
    2. 조건문
        if user > com:
            print("-")
        elif user < com:
            print("+")
        else:
            print("정답!")
'''

com = 17
user = int(input('up-down game - input number : '))

if user > com:
    print("-")
elif user < com:
    print("+")
else:
    print("정답!")
