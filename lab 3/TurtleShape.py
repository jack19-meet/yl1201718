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
ex1()

def ex2():
	turtle.forward(50)
	turtle.right(270)
	turtle.forward(50)







turtle.mainloop()