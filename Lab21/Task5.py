import turtle

turtle.shape('turtle')

i = 10

while i < 200:
	turtle.pendown()
	turtle.forward(i)
	turtle.left(90)
	turtle.forward(i)
	turtle.left(90)
	turtle.forward(i)
	turtle.left(90)
	turtle.forward(i)
	turtle.penup()
	turtle.forward(10)
	turtle.right(90)
	turtle.forward(10)
	turtle.right(180)
	i += 20