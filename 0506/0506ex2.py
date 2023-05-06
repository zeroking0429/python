'''
2023-05-06
kim se yeong
sequence data-type
'''
str1 = "once" # string
str_list = ['t', 'w', 'i', 'c', 'e'] # list
num_tuple = (5, 3, 2, 1, 4) # tuple
num1 = [1, 2, 3]
num2 = [4, 5, 6]

print(str1[3]) # indexing - variable str1's index 3
print(str_list[2:]) # slicing - index 2 ~ index end
print(num_tuple[:3]) # slicing - index start ~ index 2

print(f'length of variable str1 is {len(str1)}')
print(f"str_list include 's'? {'s' in str_list}")
print('once ' * 3)
print(num1 + num2)