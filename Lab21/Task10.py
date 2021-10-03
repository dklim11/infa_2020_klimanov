import turtle

turtle.shape('turtle')

def funcR():
	i = 0
	while i < 180:
		turtle.forward(2)
		turtle.right(2)
		i = i + 1
	
def funcL():
	i = 0
	while i < 180:
		turtle.forward(2)
		turtle.left(2)
		i = i + 1
turtle.right(90)
i = 0

while i < 3:
	funcL()
	funcR()
	turtle.right(60)
	i = i + 1