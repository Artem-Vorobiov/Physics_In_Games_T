import turtle
import math

# Set up screen
wn = turtle.Screen()
wn.bgcolor('blue')
wn.title('Simple Object Motion with Physics and no Friction')

class Player(turtle.Turtle):

	def __init__(self):
		turtle.Turtle.__init__(self)
		self.color('white')
		self.shape('triangle')
		self.penup()
		self.speed(0) # Animation speed
		self.speed = 0.2
		self.thrust = 0.5
		self.dx = 0
		self.dy = 0


	def move(self):
		self.goto(self.xcor() + self.dx, self.ycor() + self.dy)		# new important LINE
		# print('\n\t Go to: {}; type of: {}'.format(self.goto, type(self.goto)))

	def turnleft(self):
		self.left(30)

	def turnright(self):
		self.right(30)

########################################################################################
			################## Why is this formula ? ##########################
	def accelerate(self):											# new function
		h = self.heading()
		print('\nHeading {}, and type of {}\n'.format(h, type(h)))
		print('\nY {}, and type of Y {}\n'.format(self.dy, type(self.dy)))
		self.dx += math.cos(h*math.pi/180)*self.thrust
		self.dy += math.sin(h*math.pi/180)*self.thrust
		print('\nY {}, and type of Y {}\n'.format(self.dy, type(self.dy)))
########################################################################################

	def descreasespeed(self):
		self.speed -= 1

player = Player()
# print('\n\nType: {}; What is it: {}\n List of methods: {}\n'.format(type(player), player, dir(player)))


turtle.listen() 								# Tells the Turtle module to listen for the keynoard inpput
turtle.onkey(player.turnleft, 'Left')
turtle.onkey(player.turnright, 'Right')
turtle.onkey(player.accelerate, 'Up')
turtle.onkey(player.descreasespeed, 'Down')



# Main game loop
while True:
	player.move()