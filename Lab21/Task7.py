import turtle

turtle.shape('turtle')

i = 0

while i < 1000:
	turtle.forward(0.5 + i*0.05)
	turtle.left(20)
	i += 1