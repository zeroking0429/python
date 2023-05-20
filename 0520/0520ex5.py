from os import *
from funcs import *
system('cls')
'''
2023-05-06
kim se yeong
turtle graphics - polygon
'''
speed(0)
begin_fill()
color(textinput('Color', 'Input color'))
polygon(intinput('Polygon', 'Input n'), 100) 
end_fill()
'''
# polygon(n, leg) = for i in range(n):; forward(leg); left(360 / n);
# intinput(title, text) = int(text(or num)input(title, text))
-note-
numinput()'s data type = float
'''

system('pause')
