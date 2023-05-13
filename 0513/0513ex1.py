from os import *
system('cls')
'''
2023-05-06
kim se yeong
#문제정의
    loop - multiplication tables(input)
#문제분석
    변수 - n
#알고리즘
    1. 변수선언
        n = int(input('Input number : '))
    2. 반복문
        for i in range(1, 10):
            print(f'{n} * {i} = {n * i}')

'''
n = int(input('Input number : '))
i = 1
print(f'----{n}단----')
while i < 10:
    print(f'{n} * {i} = {n * i}')
    i += 1
    
print()
n = int(input('Input number : '))
print(f'----{n}단----')
for i in range(1, 10):
    print(f'{n} * {i} = {n * i}')
