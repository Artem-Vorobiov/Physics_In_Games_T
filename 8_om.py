import turtle
import math

# Set up screen
wn = turtle.Screen()
wn.bgcolor('blue')
wn.title('Simple Object Motion Move Set Distance Continuous')
GRAVITY = 0.1

class Player(turtle.Turtle):

	def __init__(self):
		turtle.Turtle.__init__(self)
		self.color('white')
		self.shape('square')
		self.penup()
		self.speed(0)       # Animation speed
		self.speed = 3     # in pixels
		self.direction = 'stop'



	def move(self):
		if self.direction == 'left':
			self.goto(self.xcor() - self.speed, self.ycor())

		elif self.direction == 'right':
			self.goto(self.xcor() + self.speed, self.ycor())

		elif self.direction == 'up':
			self.goto(self.xcor(), self.ycor() + self.speed)

		elif self.direction == 'down':
			self.goto(self.xcor(), self.ycor() - self.speed)

		else:
			self.goto(self.xcor(), self.ycor())




	def move_left(self):
		self.direction = 'left'

	def move_right(self):
		self.direction = 'right'

	def move_up(self):
		self.direction = 'up'

	def move_down(self):
		self.direction = 'down'

player = Player()



turtle.listen() 								# Tells the Turtle module to listen for the keynoard inpput
turtle.onkey(player.move_left, 'Left')
turtle.onkey(player.move_right, 'Right')
turtle.onkey(player.move_up, 'Up')
turtle.onkey(player.move_down, 'Down')



# Main game loop
while True:
	player.move()