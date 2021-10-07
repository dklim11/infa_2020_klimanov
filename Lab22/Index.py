import turtle

turtle.shape('turtle')
turtle.color('blue')
turtle.width(2)

x_distance = 1.3 * 60

#We begin to draw from the right top bottom
def draw(A):
	x_begin = turtle.xcor()
	y_begin = turtle.ycor()
	
	for i in range(len(A)):
		turtle.goto(turtle.xcor() + A[i][0], turtle.ycor() + A[i][1])
	
	turtle.penup()
	turtle.goto(x_begin + x_distance, y_begin)
	turtle.pendown()

n = int(input())
for i in range(n):
	A = [(0, 0)] * int(input())
	j = 0
	while j < len(A):		
		a = int(input()) * 50
		b = int(input()) * 50
		A[j] = (a, b)
		j += 1
	draw(A)

	