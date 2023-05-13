from os import *
system('cls')
'''
2023-05-06
kim se yeong
#문제정의
    loop - multiplication tables
#문제분석
    변수 - i, j
#알고리즘
    1. 변수선언
        for i ..., for j ...
    2. 반복문
        for i in range(2, 10):
            for j in range(1, 10):
                print(f'{i} * {j} = {i * j}')

'''
for i in range(2, 10):
    print(f'----{i}단----')
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}')
