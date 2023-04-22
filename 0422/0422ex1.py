'''
2023.04.22
kim se yeong
순서가 있는 자료-string, list
-index, indexing, slicing
'''
str1 = 'Ready'
animal = ['rabbit', 'dog', 'deer'] # list

# index
print('str1변수의 인덱스 1번 요소는', str1[1])
print('animal변수의 인덱스 2번 요소는', animal[2])
# indexing
print(animal)
animal[0] = '사자'
print(animal)
# slicing( [start index:end index]-end index - 1([2:5] 2 <= index < 5) )
print("string :", str1)
print("list :", animal)
print("string slicing :", str1[0:3]) # slicing index 0 ~ 2
print("list slicing :", animal[:2]) # slicing index start ~ 1
print("string slicing :", str1[2:]) # slicing index 2 ~ end