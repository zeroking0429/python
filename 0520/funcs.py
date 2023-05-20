from turtle import *

def leftgo(leg, n):
    forward(leg)
    left(n)
    
def rightgo(leg, n):
    forward(leg)
    right(n)

def polygon(n, leg):
    for i in range(n):
        leftgo(leg, 360 / n)

def intinput(tit :str, text :str):
    return int(textinput(tit, text))
    
    
red = 'red'
purple = 'purple'
blue = 'blue'
green = 'green'
yellow = 'yellow'
orange = 'orange'
pause = 'pause'
