import turtle
from random import random

turtle.shape('circle')
turtle.color('red')

i = 0

while i < 300:
	m = random() * 50
	r = random() * 360
	turtle.forward(m)
	turtle.right(r)
	i += 1
