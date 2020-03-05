import turtle
import math

# Set up screen
wn = turtle.Screen()
wn.bgcolor('blue')
wn.title('Simple Object Motion Move Set Distance')
GRAVITY = 0.1

class Player(turtle.Turtle):

	def __init__(self):
		turtle.Turtle.__init__(self)
		self.color('white')
		self.shape('square')
		self.penup()
		self.speed(0)       # Animation speed
		self.speed = 20     # in pixels



	def move(self):
		self.goto(self.xcor(), self.ycor())

	def move_left(self):
		self.setx(self.xcor() - self.speed)

	def move_right(self):
		self.setx(self.xcor() + self.speed)

	def move_up(self):
		self.sety(self.ycor() + self.speed)

	def move_down(self):
		self.sety(self.ycor() - self.speed)

player = Player()



turtle.listen() 								# Tells the Turtle module to listen for the keynoard inpput
turtle.onkey(player.move_left, 'Left')
turtle.onkey(player.move_right, 'Right')
turtle.onkey(player.move_up, 'Up')
turtle.onkey(player.move_down, 'Down')



# Main game loop
while True:
	player.move()