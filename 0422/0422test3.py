'''
2023-04-22
kim se yeong
# 문제
    num1, num2 변수를 이용한 사칙연산 프로그램
# 문제분석
    변수-10(num1), 20(num2)
    수식
    {
        num1 + num2
        num1 - num2
        num1 * num2
        num1 / num2
    }
# 알고리즘
    1.변수 선언
        num1 = 10
        num2 = 20
    2.사칙연산
        {
            num1 + num2
            num1 - num2
            num1 * num2
            num1 / num2
        }
    3. 2를출력
'''
num1 = 10 # interger 10
num2 = 20 # interger 20
print("{} + {} = {}".format(num1, num2, num1 + num2))
print("{} - {} = {}".format(num1, num2, num1 - num2))
print("{} * {} = {}".format(num1, num2, num1 * num2))
print("{} / {} = {}".format(num1, num2, num1 / num2))