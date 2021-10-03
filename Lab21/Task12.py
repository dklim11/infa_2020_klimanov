import turtle

def funcR(l):
	i = 0
	while i < 45:
		turtle.forward(l)
		turtle.right(4)
		i += 1
i = 0
while i < 20:
	funcR(2)
	funcR(0.25)
	i += 1