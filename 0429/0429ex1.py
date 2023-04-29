'''
2023.04.29
kim se yeong
input(), change type function : int(), float()
'''
name = input('input name : ') # input name(string)
print("name is {}, name's type is {}".format(name, type(name)))

age = input('input age : ') # input age(string)
print("age is {}, age's type is {}".format(age, type(age)))

age2 = int(input('input age2 : ')) # input age(integer)
print("age is {}, age's type is {}".format(age2, type(age2)))

pi = float(input('input pi : ')) #input pi(float)
print("pi is {}, pi's type is {}".format(pi, type(pi)))