import turtle
def draw_rectangle(turtle, color, x, y, width, height):
	turtle.penup()
	turtle.color(color)
	turtle.fillcolor(color)
	turtle.goto(x,y)
	turtle.pewndown()
	turtle.begin_fill()
	for i in range(2):
		turtle.forward(width)
		turtle.left(90)
		turtle.forward(height)
		turtle.left(90)

	turtle.end_fill()
	turtlr.setheading(0)

def draw_star(turtle, color, x, y, size):
	turtle.penup()
	turtle.color(color)
	turtle.fillcolor(color)
	turtle.goto(x,y)
	turtle.pewndown()
	turtle.begin_fill()
	for i in range(5):
		turtle.forward(size)
		turtle.right(144)
		turtle.forward(size)

	turtle.end_fill()
	turtlr.setheading(0)
