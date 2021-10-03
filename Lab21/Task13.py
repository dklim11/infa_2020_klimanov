import turtle

turtle.shape('turtle')

turtle.penup()
turtle.left(90)
turtle.forward(40)
turtle.right(90)
turtle.pendown()

def funcR(l):
	i = 0
	while i < 90:
		turtle.forward(l)
		turtle.right(4)
		i += 1
def HalFfuncR(l):
	i = 0
	while i < 45:
		turtle.forward(l)
		turtle.right(4)
		i += 1

turtle.begin_fill()
turtle.color('yellow')
funcR(10)
turtle.end_fill()

turtle.penup()
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(40)
turtle.right(180)
turtle.pendown()

turtle.begin_fill()
turtle.color('blue')
funcR(1.5)
turtle.end_fill()

turtle.penup()
turtle.forward(80)
turtle.pendown()

turtle.begin_fill()
turtle.color('blue')
funcR(1.5)
turtle.end_fill()

turtle.penup()
turtle.left(180)
turtle.forward(40)
turtle.left(90)
turtle.forward(60)
turtle.pendown()
turtle.color('black')
turtle.width(15)
turtle.forward(30)
turtle.penup()

turtle.forward(10)
turtle.left(90)
turtle.forward(60)
turtle.right(90)
turtle.pendown()
turtle.color('red')

HalFfuncR(4)






