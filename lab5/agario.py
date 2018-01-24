from turtle import *
import turtle
import time
import random
from ball import *
colormode(255)
screen_width=getcanvas().winfo_width()/2
screen_height=getcanvas().winfo_width()/2


number_of_BALLS = 5 
minimum_ball_radius = 10
maximum_ball_radius = 100
minimum_ball_dx = -5
maximum_ball_dx = 5
minimum_ball_dy = -5
maximum_ball_dy = 5
balls =[]

for i in range(number_of_BALLS):

	screen_random1_x = int(-screen_width+maximum_ball_radius)
	screen_random2_x = int(screen_width-maximum_ball_radius)
	random_x = random.randint(screen_random1_x,screen_random2_x)
	
	screen_random1_y = int(-screen_height+maximum_ball_radius)
	screen_random2_y = int(screen_height-maximum_ball_radius)
	random_y = random.randint(screen_random1_y,screen_random2_y)
	
	random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
	while random_dx == 0:
		random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)

	random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
	while random_dy == 0:
		random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
	radius = random.randint(minimum_ball_radius,maximum_ball_radius)

	color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
	

	ball = Ball(random_x,random_y,random_dx,random_dy,radius)
	balls.append(ball)


def move_all_balls():
	for variable in range(number_of_BALLS):
		balls[variable].move(screen_width,screen_height)



def check_collide(ball_a,ball_b):
	if ball_a == ball_b:
		return False

						#squareroot ( x2-x1 squared ) + ( y2-y1 squared)
	balls_distance = ((ball_a.x-ball_b.x)**2 +(ball_a.y-ball_b.y**2)**0.5)
	sum_radius = ball_a.r+ball_b.r
	if balls_distance+10 <= sum_radius:
		return True
	else:
		return False

def check_all_balls_collision():
	for ball_a in balls:
		for ball_b in balls:
			if check_collide(ball_a,ball_b) == True:
				radius1 = ball_a.r
				radius2 = ball_b.r
				random_x = random.randint(screen_random1_x,screen_random2_x)
				random_y = random.randint(screen_random1_y,screen_random2_y)
				random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
				random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
				radius = random.randint(minimum_ball_radius,maximum_ball_radius)
				color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

				if radius1 > radius2:
					ball_b.x = random_x
					ball_b.y = random_y
					ball_b.dx = random_dx
					ball_b.dy = random_dy
					ball_b.r = radius
					ball_b.color = color
					radius1 += 1 
					return False
				elif radius1 < radius2:
					ball_a.x = random_x
					ball_a.y = random_y
					ball_a.dx = random_dx
					ball_a.dy = random_dy
					ball_a.r = radius
					ball_a.color = color
					radius2 += 1
					return False

def check_myball_collision():			
	for ball in range(balls):
		random_x = random.randint(screen_random1_x,screen_random2_x)
		random_y = random.randint(screen_random1_y,screen_random2_y)
		random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
		random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
		radius = random.randint(minimum_ball_radius,maximum_ball_radius)
		color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

		if check_collide(MY_BALL,ball) == True:
			radius3 = MY_BALL.r
			radius4 = ball.r

		elif MY_BALL.r < ball.r:
			return 	False
		else:
			MY_BALL.r +=2
			ball.x = random_x
			ball.y = random_y
			ball.dx = random_dx
			ball.dy = random_dy
			ball.r = radius
			ball.color = color
	return True
def movearound(event):
	MY_BALL.x = event.x - screen_width
	MY_BALL.y = screen_height -event.y
turtle.listen()
turtle.getcanvas().bind("<Motion>", movearound)
for i in range(1000):
	check_all_balls_collision()
	move_all_balls()
	


#while running == True:

mainloop()