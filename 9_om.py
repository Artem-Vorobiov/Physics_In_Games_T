import turtle
import math
import random

# Set up screen
wn = turtle.Screen()
wn.bgcolor('blue')
wn.title('Simple Object Motion with Physics and NO Friction Player in the center')

class Player(turtle.Turtle):

	def __init__(self):
		turtle.Turtle.__init__(self)
		self.color('white')
		self.shape('triangle')
		self.penup()
		self.speed(0) # Animation speed
		self.speed = 0.8
		self.thrust = 0.8
		self.dx = 0
		self.dy = 0


	def move(self):
		self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

	def turnleft(self):
		self.left(30)

	def turnright(self):
		self.right(30)

########################################################################################
			################## Why is this formula ? ##########################
	def accelerate(self):											# new function
		h = self.heading()
		# print('\nHeading {}, and type of {}\n'.format(h, type(h)))
		# print('\nY {}, and type of Y {}\n'.format(self.dy, type(self.dy)))
		self.dx += math.cos(h*math.pi/180)*self.thrust
		self.dy += math.sin(h*math.pi/180)*self.thrust
		# print('\nY {}, and type of Y {}\n'.format(self.dy, type(self.dy)))
########################################################################################



class Enemy(turtle.Turtle):

	def __init__(self):
		turtle.Turtle.__init__(self)
		self.color('red')
		self.shape('circle')
		self.penup()
		self.speed(0)
		self.goto(random.randint(-500, 500), random.randint(-500, 500))

	def move(self):
		self.fd(1 )
		self.setx(self.xcor() - player.dx)
		self.sety(self.ycor() - player.dy)


player = Player()

enemies = []
for _ in range(25):
	enemies.append(Enemy())



turtle.listen() 								# Tells the Turtle module to listen for the keynoard inpput
turtle.onkey(player.turnleft, 'Left')
turtle.onkey(player.turnright, 'Right')
turtle.onkey(player.accelerate, 'Up')



wn.tracer(0)
# Main game loop
while True:
	wn.update()
	# player.move()
	for enemy in enemies:
		enemy.move()



