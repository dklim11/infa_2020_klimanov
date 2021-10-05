import turtle
turtle.shape('turtle')

l = 40
n = 3

def func(n, l):
	i = 0
	turtle.left(180 - 90*(n - 2)/n)
	while i < n:
		turtle.forward(l)
		turtle.left(180 - 180*(n - 2)/n)
		i += 1
	turtle.right(90*(n - 2)/n + 180 - 180*(n - 2)/n)
	turtle.penup()
	turtle.forward(l * 0.5 - (n - 3) * 5)
	turtle.pendown()

while n < 10:
	func(n, l)
	l += 20
	n += 1 