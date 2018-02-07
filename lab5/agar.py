from turtle import *
import random
import time
colormode(255)
tracer(0)
hideturtle()

bgcolor("black")
running = True
sleep = 0.0077
number_of_BALLS = 5
minimum_ball_radius = 4
maximum_ball_radius = 24
minimum_ball_dx = -3
maximum_ball_dx = 3
minimum_ball_dy = -3
maximum_ball_dy = 3
balls = []

MY_BALL = ball(0,0,0,0,25,"red")

for i in range(number_of_BALLS):
    screen_random1_x = int(-screen_width+maximum_ball_radius)
    screen_random2_x = int(screen_width - maximum_ball_radius)
    random_x = random.randint (screen_random1_x,screen_random2_x)

    screen_random1_y = int(-screen_height + maximum_ball_radius)
    screen_random2_y = int(screen_height - maximum_ball_radius)
    random_y = random.randint (screen_random1_y,screen_random2_y)

    random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
    while random_dx == 0:
        random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)

    random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
    while random_dy == 0:
        random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
    radius = random.randint(minimum_ball_radius,maximum_ball_radius)

    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    ball = Ball(random_x,random_y,random_dx,random_dy,radius,color)
    balls.append(ball)



def move_all_balls():
    for variable in range(number_of_BALLS):
        balls[variable].move(screen_width,screen_height)



def check_collide(ball_a,ball_b):
    if ball_a == ball_b:
        return False


    balls_distance = ((ball_a.xcor() - ball_b.xcor())**2 +(ball_a.ycor() - ball_b.ycor())**2)**0.5

    if balls_distance + 10 <= ball_a.r + ball_b.r:
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
                color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))



                if radius1 > radius2:
                    ball_b.goto(random_x,random_y)
                    ball_b.x = random_x
                    ball_b.y = random_y
                    ball_b.dx = random_dx
                    ball_b.dy = random_dy
                    ball_b.r = radius 
                    ball_b.color(color, color)
                    ball_b.r += 1
                    ball_b.shapesize(ball_b.r/10)

                elif radius1 < radius2:
                    ball_a.goto(random_x,random_y)
                    ball_a.x = random_x
                    ball_a.y = random_y
                    ball_a.dx = random_dx
                    ball_a.dy = random_dy
                    ball_a.r = radius 
                    ball_a.color(color, color)
                    ball_a.r += 1
                    ball_a.shapesize(ball_b.r/10)



def check_myball_collision():
    for ball in balls:
        random_x = random.randint(screen_random1_x,screen_random2_x)
        random_y = random.randint(screen_random1_y,screen_random2_y)
        random_dx = random.randint(minimum_ball_dx,maximum_ball_dx)
        random_dy = random.randint(minimum_ball_dy,maximum_ball_dy)
        radius = random.randint(minimum_ball_radius,maximum_ball_radius)
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

        if check_collide(MY_BALL,ball):
            new_radius = MY_BALL.r 
            new_radius = ball.r 

            if MY_BALL.r < ball.r:
                return False

            else:
                MY_BALL.r = new_radius + 1
                MY_BALL .shapesize(MY_BALL.r/10)
                print(MY_BALL.r)
                ball.goto(random_x,random_y)
                ball.x = random_x
                ball.y = random_y
                ball.dx = random_dx
                ball.dy = random_dy
                ball.r = radius 
                ball.color(color, color)

    return True

def movearound (event):

    MY_BALL.goto(event.x - screen_width,screen_height - event.y)
turtle.getcanvas().bind("<Motion>", movearound)
getscreen().listen()


while running == True:




































