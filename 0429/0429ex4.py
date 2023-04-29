'''
2023.04.29
kim se yeong
#문제정의
    입력받은 정수가 짝수이면 "짝수"출력, 아니면 "홀수"출력 하는 프로그램
#문제분석
    변수-n
#알고리즘
    1. 변수 선언
        n = int(input('input number : '))
    2. 조건식
        if n % 2 == 0:
            print("짝수")
        else:
            print("홀수")
'''

n = int(input('input number : '))

if n % 2 == 0: # 조건식
    print("짝수") # True
else:
    print("홀수") #False
