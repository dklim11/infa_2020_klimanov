import turtle

turtle.shape('turtle')

turtle.left(180)

def star(n):
	i = 0
	while i < n:
		turtle.forward(80)
		turtle.left(180 - 180/n)
		i += 1

star(5)

turtle.right(180)
turtle.penup()
turtle.forward(200)
turtle.right(180)
turtle.pendown()

star(11)