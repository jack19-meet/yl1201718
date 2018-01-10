from turtle import *
import random
import math
tracer()

class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

ball1 = Ball(69,"black",9)
ball2 = Ball(30,"red",4)
ball1.forward(100)
balls = []
balls.append(ball1)
balls.append(ball2)
print(balls)

def check_collision(ball1,ball2):
	x1 = ball1.xcor()
	y1 = ball1.ycor()
	x2 = ball2.xcor()
	y2 = ball2.ycor()
	b = math.pow(x2-x1)
	x_squared = math.sqrt(b)
	math.abs()
	d = math.pow(y2-y1)
	y_squared = math.sqrt(d)
	z = b+d
	f = math.sqrt(z)
	


def move(self):
	current_x = self.xcor()
	current_y = self.ycor()
	self.goto(current_x = self.dx, current_y = self.dy)

mainloop()
