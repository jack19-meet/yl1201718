from turtle import *
import randomimport math

class Ball(Turtle):
	def __init__ (self, radius ,color, speed):
		Turtle.__init__(self)
		self.shape('circle')
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

ball1 = Ball(10, 'red', 3)
ball2 = Ball(30, "black", 7)

def check_collision(ball1,ball2):
	x1 = ball1.xcor()
	y1 = ball1.ycor()
	x2 = ball2.xcor()
	y2 = ball2.ycor()
	d=math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2,2))

	if d <= (ball.radius + ball.radius):
		print("it is collided")

	else:
		print("it is not collided")


check_collision(ball1,ball2)



mainloop()
