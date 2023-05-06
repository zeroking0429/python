'''
2023-05-06
kim se yeong
sequence data-type practice
'''
line_up = []
line_up.append('turtle')
print(line_up)

line_up.append('rabit')
print(line_up)

line_up.insert(1, '다람쥐')
print(line_up)

line_up.remove('turtle')
print(line_up)

num_list = [5, 3, 8, 2, 10]
# add number 4 (index 2)
num_list.insert(2, 4)

# remove number 10
num_list.remove(10)
print(num_list)

num_list.sort()
print(num_list)
