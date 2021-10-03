import turtle

turtle.shape('turtle')

def funcR(l):
	i = 0
	while i < 90:
		turtle.forward(l)
		turtle.right(4)
		i += 1
def funcL(l):
	i = 0
	while i < 90:
		turtle.forward(l)
		turtle.left(4)
		i = i + 1
i = 2
while i < 12:
	funcR(i)
	funcL(i)
	i += 1