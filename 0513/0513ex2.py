from os import *
system('cls')
'''
2023-05-06
kim se yeong
#문제정의
    정수를 입력 받아서 별 출력하기
#문제분석
    변수 - n
#알고리즘
    1. 변수선언
        n = int(input('Input number : '))
    2. 반복문(중첩)
        for i in range(n):
            for j in range(i):
                print('*')

'''
n = int(input('Input number : '))

for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()

area = (n*n) / 2
print(f'area = {area}')
# 거꾸로 찍기
n = int(input('Input number : '))
cnt = n
for i in range(1, n + 1):
    cnt -= 1
    for j in range(cnt):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

area = (n*n) / 2
print(f'area = {area}')
#정삼각형
n = int(input('Input number : '))
cnt = n
for i in range(1, n + n, 2):
    cnt -= 1
    for j in range(cnt):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

area = (n*n) / 2
print(f'area = {area}')
#마름모
n = int(input('Input number : '))
cnt = n
for i in range(1, n + n, 2):
    cnt -= 1
    for j in range(cnt):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

for i in range(n + (n - 3), 0, -2):
    cnt += 1
    for j in range(cnt):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

area = (n + (n - 1)) / 2
print(f'area = {area}')
#평행사변형
n = int(input('Input number : '))
cnt = n
for i in range(1, n + 1):
    cnt -= 1
    for j in range(cnt):
        print(' ', end='')
    for j in range(n):
        print('*', end='')
    print()

area = (n*n) / 2
print(f'area = {area}')