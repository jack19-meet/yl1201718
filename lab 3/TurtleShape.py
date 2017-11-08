import turtle

def ex1():
	amount = 5
	forw = 100
	turn = 144
	color = ['red','blue','green','black','yellow']
	for i in range (amount):
		turtle.pencolor(color[i])
		turtle.forward(forw)
		turtle.right(turn)


def ex2():
	turtle.register_shape("pentagon", ((10,0),(10,10),(5,15),(0,10),(0,0)))
	turtle.shape("pentagon")

	turtle.goto(50,0)
	turtle.goto(50,50)
	turtle.goto(25,75)
	turtle.goto(0,50)
	turtle.goto(0,0)


def ex4():
	for i in range(360):
		turtle.home()
		turtle.right(i)
		turtle.speed(1000)
		turtle.forward(200)
		turtle.right(45)
		turtle.forward(100)
		turtle.right(90)
		turtle.forward(50)
		
ex4()

turtle.mainloop()