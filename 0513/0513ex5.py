from os import *
from mine import *
system('cls')
'''
2023-05-06
kim se yeong
#문제정의
    숫자를 반복적으로 입력 받아서 합계가 1000이상이면 반복을 종료하고, 합계와 평균을 출력하시오.
#문제분석
    변수 - n(정수), cnt(입력 개수), sum(합), average(평균)
#알고리즘
    1. 변수선언
        average = 0
        cnt = 0
        sum = 0
    2. 반복문(+break)
        while True:
            n = int(input('Input number : '))
            cnt += 1
            sum += n
            if (sum >= 1000):
                break
                
        average = sum / cnt
        print(f'sum : {sum}\naverage : {average}')
'''
average = 0
cnt = 0
sum = 0

while True:
    n = int(input('Input number : '))
    cnt += 1
    sum += n
    if (sum >= 1000):
        break
        
average = sum / cnt
print(f'sum : {sum}\naverage : {average}')
