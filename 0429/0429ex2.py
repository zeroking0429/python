'''
2023.04.29
kim se yeong
비교연산자(>, <, >=, <=, ==, !=), 논리연산자(and, or, not) 연습
비교, 논리 연산자는 true, false 로만 결과를 표시한다.
'''

num1 = 10
num2 = 4
num3 = 4

# 비교연산
print("비교연산")
print('num1 > num2 :', num1 > num2) # 비교연산
print('num1 <= num3 :', num1 <= num3) # 비교연산
print('num2 == num3 :', num2 == num3) # 비교연산
print('num2 != num3 :', num2 != num3) # 비교연산
print() # \n

# 논리연산
print("논리연산")
print('num1 > num2 and num2 == num3 :', num1 > num2 and num2 == num3) # 논리연산
print('num1 > num2 and num2 != num3 :', num1 > num2 and num2 != num3) # 논리연산
print('num1 > num2 or num2 != num3 :', num1 > num2 or num2 != num3) # 논리연산
print('num1 < num2 or num2 != num3 :', num1 < num2 or num2 != num3) # 논리연산