from turtle import *
import random
import time
colormode(255)
tracer(0)
hideturtle()


class Ball(Turtle):
    def __init__(self,x ,y ,dx ,dy ,radius):
        Turtle.__init__(self)
        self.pu()
        self.goto(x,y)
        self.dx = dx
        self.dy  = dy
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius


    def move(self,width ,height):
        current_x = self.xcor()
        new_x = current_x + dx
        current_y = self.ycor()
        new_y = current_y + dy
        right_side_ball = new_x + radius
        left_side_ball = new_x - radius
        top_side_ball = new_y + radius
        bottom_side_ball = new_y - radius
        self.goto(new_x, new_y)

        if top_side_ball > height/2:
            self.dy = -self.dy

        elif bottom_side_ball < -height/2:
            self.dy = -self.dy

        elif right_side_ball > width/2:
            self.dx = -self.dx

        elif left_side_ball < -width/2:
            self.dx = -self.dx

        self.goto(new_x, new_y)