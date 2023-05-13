from os import *
from mine import *
system('cls')
'''
2023-05-06
kim se yeong
#문제정의
    정수 2개와 연산자(+, -, *, /)1개를 입력 받아서 사칙연산을 수행하는 계산기 만들기
#문제분석
    변수 - first(첫번째 수), second(두번째 수), symbol(연산 기호)
#알고리즘
    1. 변수선언
        first = int(input('Input first number : '))
        symbol = int(input('Input symbol(+, -, *, /) : '))
        second = int(input('Input second number : '))
    2. 조건문
        if symbol == '+':
            print(f'{first} + {second} = {first + second}')
        elif symbol == '-':
            print(f'{first} - {second} = {first - second}')
        elif symbol == '*':
            print(f'{first} * {second} = {first * second}')
        elif symbol == '/':
            print(f'{first} / {second} = {first / second}')
        else:
            print('None symbol')
'''
first = int(input('Input first number : '))
symbol = input('Input symbol(+, -, *, /) : ')
second = int(input('Input second number : '))

if symbol == '+':
    print(f'{first} + {second} = {first + second}')
elif symbol == '-':
    print(f'{first} - {second} = {first - second}')
elif symbol == '*':
    print(f'{first} * {second} = {first * second}')
elif symbol == '/':
    print(f'{first} / {second} = {first / second}')
else:
    print('None symbol')