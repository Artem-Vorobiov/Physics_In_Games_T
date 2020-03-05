import turtle
import math

# Set up screen
wn = turtle.Screen()
wn.bgcolor('blue')
wn.title('Simple Object Motion with Physics and Gravity')
GRAVITY = 0.1

class Player(turtle.Turtle):

	def __init__(self):
		turtle.Turtle.__init__(self)
		self.color('white')
		self.shape('triangle')
		self.penup()
		self.speed(0)       # Animation speed
		self.setheading(90) # Sets heading to up
		self.thrust = 3
		self.dx = 0
		self.dy = 0
		self.terminal_velocity = -5


	def move(self):
		self.goto(self.xcor() + self.dx, self.ycor() + self.dy)		# new important LINE
		# print('\n\t Go to: {}; type of: {}'.format(self.goto, type(self.goto)))

		# Set ground level
		if self.ycor() < -300:
			self.dy = 0
			self.dx = 0
			self.sety(-300)
		else:
			self.dy -= GRAVITY

		# Set terminal velocity - для того, что бы сила гравитации не придала громадной скорости при возврате на земл
		if self.dy < self.terminal_velocity:
			self.dy = self.terminal_velocity

	def accelerate_left(self):
		self.dx -= self.thrust * 0.2

	def accelerate_right(self):
		self.dx += self.thrust * 0.2

	def accelerate_up(self):
		self.dy += self.thrust
		print('dx: {} dy: {}'.format(self.dx, self.dy))
		print('Thust: {}, type: {}\n'.format(self.thrust, type(self.thrust)))
		print('Xcor: {} Ycor: {}'.format(self.xcor(), self.ycor()))

player = Player()



turtle.listen() 								# Tells the Turtle module to listen for the keynoard inpput
turtle.onkey(player.accelerate_left, 'Left')
turtle.onkey(player.accelerate_right, 'Right')
turtle.onkey(player.accelerate_up, 'Up')
# turtle.onkey(player.descreasespeed, 'Down')



# Main game loop
while True:
	player.move()