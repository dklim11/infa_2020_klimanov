import turtle

turtle.shape('turtle')
l = 40

def func(n):
	i = 0
	turtle.left(180 - 90*(n - 2)/n)
	while i < n:
		turtle.forward(l)
		turtle.left(180 - 180*(n - 2)/n)
		i += 1
	turtle.right(90*(n - 2)/n + 180 - 180*(n - 2)/n)
	turtle.penup()
	turtle.forward(l * 0.5)
	turtle.pendown()
	
n = 3

while n < 10:
	func(n)
	l += 20
	n += 1
	
