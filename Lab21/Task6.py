import turtle

turtle.shape('turtle')

i = 0
n = int(input())

while i < n:
	turtle.forward(50)
	turtle.stamp()
	turtle.right(180)
	turtle.forward(50)
	turtle.left(180 - 360/n)
	i += 1