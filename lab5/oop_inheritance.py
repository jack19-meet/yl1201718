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

def ex2():
	class Hexagon(Turtle):
		def __init__(self,size,speed,pencolor):
			Turtle.__init__(self)
			self.ht()
			self.pu()

			begin_poly()
			
			ht()
			begin_fill()
			goto(50,0)
			goto(75,25)
			goto(50,50)
			goto(25,50)
			goto(0,25)
			goto(25,0)
			st()
			end_fill()
			end_poly()
			hexashape = get_poly()
			register_shape("hexagon",hexashape)
			self.shapesize(size)
			self.speed(speed)
			self.pencolor(pencolor)
			self.shape("hexagon")
			
			
	hexa1 = Hexagon(6,8,"maroon")		
	hexa1.ht()
	hexa1.goto(100,100)


class Rectangle(Turtle):
	def __init__(self,width,height):
		Turtle.__init__(self)
		register_shape("rect",((height,width),(height,width),(height,width),(height,width)))
		rectangle1  = Rectangle(100,50)







mainloop()