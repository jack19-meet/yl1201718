from turtle import *
import random

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

mainloop()