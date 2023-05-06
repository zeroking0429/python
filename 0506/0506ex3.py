from os import *
system('cls')
'''
2023-05-06
kim se yeong
loop - for
'''
sum = 0
# Use sequence
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i, end=' ')

print() # print \n

# Use range()
for i in range(1, 11):
    print(i, end=' ')
    
print() # print \n

# sum 1 ~ 10
for i in range(1, 11):
    sum += i

print(f'sum 1 ~ 10 : {sum}')

# sum 1 ~ user-num

num = int(input('input number : '))
sum = 0

for i in range(1, num + 1):
    sum += i
    
print(f'sum 1 ~ {num:,} : {sum:,}')