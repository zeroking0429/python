from os import *
from funcs import *
system('cls')
'''
2023-05-06
kim se yeong
turtle graphics
'''
speed(0)
colors = [red, purple, blue, green, yellow, orange]
length = 10
bgcolor('black')
width(100)

while length < 1500:
    forward(length)
    pencolor(colors[length % 6])
    right(89)
    length += 5
    
system('pause')