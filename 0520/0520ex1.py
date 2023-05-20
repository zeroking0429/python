from os import *
from funcs import *
system('cls')
'''
2023-05-06
kim se yeong
turtle graphics
'''
speed(0)
shape() # = shape('classic') # None = classic

# leftgo(leg, n) leftgo = forward(leg); left(n);

# draw ㅁ with loop
for i in range(2):
    leftgo(100, 90)
    leftgo(50, 90)

# draw □ with loop
for i in range(4):
    leftgo(50, 90);

# triangle
# polygon(n, leg) = for i in range(n):; forward(leg); left(360 / n)
polygon(3, 100)

# draw r = 100 circle
circle(100)

# 5
polygon(5, 100)

system('pause')
