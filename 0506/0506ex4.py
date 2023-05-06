from os import *
system('cls')
'''
2023-05-06
kim se yeong
loop - while
'''
sum = 0
# print 1 ~ 10
i = 1
while i <= 10:
    print(i, end=' ')
    i+=1

print() # print '\n'
# sum 1 ~ 10
i = 1
while i <= 10:
    sum += i
    i+=1
    
print(sum)
# sum 1 ~ user-num
sum = 0
num = int(input('input number : '))
i = 0
while i < num:
    i+=1
    sum += i
    
print(f'sum 1 ~ {num} : {sum}')