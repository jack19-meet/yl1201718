from ball import *
import turtle 
import time
import random
import sys


window = turtle.Screen()
window.setup(width = 1.0, height = 1.0)

SCREEN_WIDTH = int(turtle.getcanvas().winfo_width() / 2)
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height() / 2)

NUMBER_OF_BALLS = 8
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 150
MAXIMUM_PLAYER_RADIUS = 500

MINIMUM_ENEMY_DX = -15
MAXIMUM_ENEMY_DX = 15
MINIMUM_ENEMY_DY = -15
MAXIMUM_ENEMY_DY = 15

ACCELARATION_OF_BALL = 9
RADIUS_TO_WIN = 500

SCORE_FONT_SIZE = 16
SCORE_FONT_TYPE = "bold"
SCORE_FONT_NAME = "Helvetica"
SCORE_COLOR = "black"

WRITE_FONT_SIZE = 100
WRITE_FONT_TYPE = "bold"
WRITE_FONT_NAME = "Helvetica"
WRITE_COLOR = (255, 9, 5)

TIME_FONT_SIZE = 16
TIME_FONT_TYPE = "bold"
TIME_FONT_NAME = "Helvetica"
TIME_COLOR = "black"

CREDITS_FONT_SIZE = 16
CREDITS_FONT_TYPE = "bold"
CREDITS_FONT_NAME = "Helvetica"
CREDITS_COLOR = "black"

writeToScreen = turtle.clone()
writeToScreen.ht()
writeToScreen.color(WRITE_COLOR)

scoreWrite = turtle.clone()
scoreWrite.color(SCORE_COLOR)
scoreWrite.ht()

timeWrite = turtle.clone()
timeWrite.color(TIME_COLOR)
timeWrite.ht()
timeScore = 0

creditWrite = turtle.clone()
creditWrite.color(CREDITS_COLOR)
creditWrite.ht()


MIN_FOOD_RADIUS = 3
MAX_FOOD_RADIUS = 7
MAX_FOOD_NUM = 50

DECAY = 0.0003

BALLS = []
FOOD = []

MY_BALL = Ball(0, 0, 4, 4, 30, (180, 0, 35))

RUNNING = True
SLEEP = 0.0077

turtle.tracer(0)
turtle.ht()

def collide(ball1, ball2):
		if (ball1 == ball2):
			return False

		distanceX = ball1.x - ball2.x
		distanceY = ball1.y - ball2.y

		distanceCircles = math.sqrt(math.pow(distanceX, 2) + math.pow(distanceY, 2))
		radiusSum = ball1.radius + ball2.radius

		if (distanceCircles + 10 <= radiusSum):
			return True
		else:
			return False

def createEnemies():
	isCrash = True
	
	for i in range(NUMBER_OF_BALLS):
		isCrash = True

		while isCrash == True:
			radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
			x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)

			while ((x < MY_BALL.x + MY_BALL.radius + radius and x > MY_BALL.x - MY_BALL.radius - radius) and (y < MY_BALL.y + MY_BALL.radius + radius and y > MY_BALL.y - MY_BALL.radius - radius) and MY_BALL.radius < MAXIMUM_PLAYER_RADIUS):
				x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)	

			color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
			dx = 0
			dy = 0

			while (dx == 0):
				dx = random.randint(MINIMUM_ENEMY_DX, MAXIMUM_ENEMY_DX)

			while (dy == 0):
				dy = random.randint(MINIMUM_ENEMY_DY, MAXIMUM_ENEMY_DX)

			ball = Ball(x, y, dx, dy, radius, color)

			if collide(MY_BALL, ball) != True:
				BALLS.append(ball)
				isCrash = False
			else:
				ball.ht()
				del ball
createEnemies()

def createFood():
	isCreateFood = random.random()

	if isCreateFood < 0.2 and len(FOOD) < MAX_FOOD_NUM:
		x = random.randint(-SCREEN_WIDTH + MAX_FOOD_RADIUS, SCREEN_WIDTH - MAX_FOOD_RADIUS)
		y = random.randint(-SCREEN_HEIGHT + MAX_FOOD_RADIUS, SCREEN_HEIGHT - MAX_FOOD_RADIUS)
		radius = random.randint(MIN_FOOD_RADIUS, MAX_FOOD_RADIUS)
		color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

		food = Ball(x, y, 0, 0, radius, color)
		FOOD.append(food)

def moveAllBalls():
	for ball in BALLS:
		ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def checkAllBallsCollision():
	for ballA in BALLS:
		for ballB in BALLS:
			isColliding = collide(ballA, ballB)

			if isColliding == True:
				ballARadius = ballA.radius
				ballBRadius = ballB.radius

				radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)

				while ((x < MY_BALL.x + MY_BALL.radius + radius and x > MY_BALL.x - MY_BALL.radius - radius) and (y < MY_BALL.y + MY_BALL.radius + radius and y > MY_BALL.y - MY_BALL.radius - radius) and MY_BALL.radius < MAXIMUM_PLAYER_RADIUS):
					x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
					y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				
				dx = 0
				dy = 0

				while (dx == 0):
					dx = random.randint(MINIMUM_ENEMY_DX, MAXIMUM_ENEMY_DX)


				while (dy == 0):
					dy = random.randint(MINIMUM_ENEMY_DY, MAXIMUM_ENEMY_DX)

				color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

				if ballARadius > ballBRadius:
					ballA.radius += ballB.radius / 10
					ballA.setRadius(ballA.radius)

					ballB.setBall(x, y, dx, dy, radius, color)
				else:
					ballB.radius += ballA.radius / 10
					ballB.setRadius(ballB.radius)

					ballA.setBall(x, y, dx, dy, radius, color)

def checkMyBallCollision():
	for ball in BALLS:
		isColliding = collide(MY_BALL, ball)

		if isColliding == True:
			MY_BALL_RADIUS = MY_BALL.radius
			ballRadius = ball.radius

			x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)

			radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
			while ((x < MY_BALL.x + MY_BALL.radius + radius and x > MY_BALL.x - MY_BALL.radius - radius) and (y < MY_BALL.y + MY_BALL.radius + radius and y > MY_BALL.y - MY_BALL.radius - radius) and MY_BALL.radius < MAXIMUM_PLAYER_RADIUS):
					x = random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS, SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
					y = random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)

			dx = 0
			dy = 0

			while (dx == 0):
				dx = random.randint(MINIMUM_ENEMY_DX, MAXIMUM_ENEMY_DX)

			while (dy == 0):
				dy = random.randint(MINIMUM_ENEMY_DY, MAXIMUM_ENEMY_DX)

			color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

			if MY_BALL_RADIUS >= ballRadius:
				MY_BALL.radius += ball.radius / 4
				MY_BALL.setRadius(MY_BALL.radius)

				ball.setBall(x, y, dx, dy, radius, color)
				return True
			else:
				return False

	return True

def moveAround(event):
	mouseX = event.x - SCREEN_WIDTH
	mouseY = SCREEN_HEIGHT - event.y
	MY_BALL.x = mouseX
	MY_BALL.y = mouseY
	MY_BALL.goto(mouseX,mouseY)

turtle.getcanvas().bind("<Motion>", moveAround)

getscreen().listen()

def moveMyBall():
	global RUNNING 

	MY_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)
	if checkMyBallCollision() == False:
		RUNNING = False

	checkAllBallsCollision()

def eatFood():
	index = 0

	for food in FOOD:
		isColliding = collide(MY_BALL, food)

		if isColliding == True:
			MY_BALL.radius += food.radius / 2
			MY_BALL.setRadius(MY_BALL.radius)

			x = random.randint(-SCREEN_WIDTH + MAX_FOOD_RADIUS, SCREEN_WIDTH - MAX_FOOD_RADIUS)
			y = random.randint(-SCREEN_HEIGHT + MAX_FOOD_RADIUS, SCREEN_HEIGHT - MAX_FOOD_RADIUS)
			radius = random.randint(MIN_FOOD_RADIUS, MAX_FOOD_RADIUS)

			food.hideBall()

			FOOD.pop(index)

		index += 1

def decay():
	MY_BALL.radius -= DECAY * MY_BALL.radius
	MY_BALL.setRadius(MY_BALL.radius)

def score():
    scoreWrite.goto(-SCREEN_WIDTH + 10, -SCREEN_HEIGHT + 10)
    scoreWrite.clear()
    scoreWrite.write("Score: " + str(int(MY_BALL.radius * 2)), False, "left", (SCORE_FONT_NAME, SCORE_FONT_SIZE, SCORE_FONT_TYPE))

def youWin():
	scoreWrite.goto((-SCREEN_WIDTH / 2) + 25, -100)
	timeWrite.goto(110,  -100)
	creditWrite.goto(-140, -160)

	writeToScreen.goto(-SCREEN_WIDTH / 2, -50)
	writeToScreen.clear()
	writeToScreen.write("YOU WON", False, "left", (WRITE_FONT_NAME, WRITE_FONT_SIZE, WRITE_FONT_TYPE))
	scoreWrite.write("Score: " + str(int(MY_BALL.radius * 2)), False, "left", (SCORE_FONT_NAME, 25, SCORE_FONT_TYPE))
	timeWrite.write("Time: " + str(timeScore), False, "left", (SCORE_FONT_NAME, 25, SCORE_FONT_TYPE))

def youLose():
	scoreWrite.goto((-SCREEN_WIDTH / 2) + 25, -100)
	timeWrite.goto(195, -100)

	writeToScreen.goto(-SCREEN_WIDTH / 2, -50)
	writeToScreen.clear()
	scoreWrite.clear()
	timeWrite.clear()
	writeToScreen.write("You LOST", False, "left", (WRITE_FONT_NAME, WRITE_FONT_SIZE, WRITE_FONT_TYPE))
	scoreWrite.write("Score: " + str(int(MY_BALL.radius * 2)), False, "left", (SCORE_FONT_NAME, 25, SCORE_FONT_TYPE))
	timeWrite.write("Time: " + str(timeScore), False, "left", (SCORE_FONT_NAME, 25, SCORE_FONT_TYPE))
	creditWrite.write( False, "left", (CREDITS_FONT_NAME, CREDITS_FONT_SIZE, CREDITS_FONT_TYPE))
 	

def timerDisplay():
	global timeScore
	timeScore = int(time.clock() * 1.5)
	timeWrite.goto(-SCREEN_WIDTH + 10, SCREEN_HEIGHT - 30)
	timeWrite.clear()
	timeWrite.write("Time: " + str(timeScore), False, "left", (TIME_FONT_NAME, TIME_FONT_SIZE, TIME_FONT_TYPE))



def scoreDisplay():
	global scoreWrite
	scorevalue = int(MY_BALL.radius * 2)
	scoreWrite.goto(SCREEN_WIDTH - 160, SCREEN_HEIGHT - 30)
	scoreWrite.clear()
	scoreWrite.write("score: " + str(scorevalue), False, "left", (TIME_FONT_NAME, TIME_FONT_SIZE, TIME_FONT_TYPE))


while (RUNNING):
	
	if (SCREEN_WIDTH != int(turtle.getcanvas().winfo_width() / 2) or SCREEN_HEIGHT != int(turtle.getcanvas().winfo_height() / 2)):
		SCREEN_WIDTH = int(turtle.getcanvas().winfo_width() / 2)
		SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height() / 2)

	moveAllBalls()
	eatFood()
	createFood()
	RUNNING = checkMyBallCollision()
	if MY_BALL.radius > MINIMUM_BALL_RADIUS:
		decay()

	score()
	timerDisplay()
	scoreDisplay()

	if MY_BALL.radius >= RADIUS_TO_WIN:
		time.sleep(3)
		youWin()
		sys.exit()

	getscreen().update()
	time.sleep(SLEEP)
	

youLose()
time.sleep(3)
print("END GAME!!!")

