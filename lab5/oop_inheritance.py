from turtle import *
import random
colormode(255)
def random_color(self):
	r = random.randint(0,256)
	g = random.randint(0,256)
	b = random.randint(0,256)
	self.color((r,g,b))
def ex1():
	
	class Square(Turtle):
		def __init__(self,size):

			Turtle.__init__(self)
			self.shapesize(size)
			self.shape("square")
		def random_color(self):
			r = random.randint(0,256)
			g = random.randint(0,256)
			b = random.randint(0,256)
			self.color((r,g,b))

def extra():
	class Rectangle(Turtle):
		def __init__(self,size):

			Turtle.__init__(self)
			self.shapesize(size)
			self.shape("rectangle")
		def random_color(self):
			r = random.randint(0,256)
			g = random.randint(0,256)
			b = random.randint(0,256)
			self.color((r,g,b))
rectangle1 = Rectangle(10)
rectangle1.random_color()
extra()
mainloop()