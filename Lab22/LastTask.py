from random import randint

from random import random

import turtle

turtle.shape('circle')

turtle.width(2)
turtle.color('green')
i = 0
while i < 4:
	turtle.forward(200)
	turtle.right(90)

pool = [turtle.Turtle(shape = 'circle') for i in range(number_of_turtles)]

for unit in pool:
	unit.penup()
	unit.speed(random() * 20)
	unit.shapesize(0.5)
	unit.left(random() * 360)
	unit.goto(randint(-199, 199), randint(-199, 199))

for i in range(steps_of_time):
	for unit in pool:
		unit.forward(8)
		if unit.xcor() >= 200:
			if unit.heading() <= 90:
				unit.left(180 - 2 * unit.heading())
			else:
				unit.right(2 * unit.heading() - 540)
		if unit.xcor() <= -200:
			if unit.heading() <= 180:
				unit.right(2*unit.heading() - 180)
			else:
				unit.left(540 - 2 * unit.heading())
		if unit.ycor() >= 200:
			if unit.heading() <= 90:
				unit.right(2 * unit.heading()) 
			else:
				unit.left(2 * (180 - unit.heading()))
		if unit.ycor() <= -200:
			if unit.heading() <= 270:
				unit.right(2 * (unit.heading() - 180))
			else:
				unit.left(2 * (360 - unit.heading()))














