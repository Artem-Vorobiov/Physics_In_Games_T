import turtle

# Set up screen
wn = turtle.Screen()
wn.bgcolor('blue')
wn.title('Simple Object Motion Template')

class Player(turtle.Turtle):

	def __init__(self):
		turtle.Turtle.__init__(self)
		self.color('white')
		self.shape('triangle')
		self.penup()
		self.speed(0) # Animation speed
		self.speed = 1

	def move(self):
		self.fd(self.speed)

	def turnleft(self):
		self.left(30)

	def turnright(self):
		self.right(30)

	def increasespeed(self):
		self.speed += 1

	def descreasespeed(self):
		self.speed -= 1

player = Player()
# print('\n\nType: {}; What is it: {}\n List of methods: {}\n'.format(type(player), player, dir(player)))


turtle.listen() 								# Tells the Turtle module to listen for the keynoard inpput
turtle.onkey(player.turnleft, 'Left')
turtle.onkey(player.turnright, 'Right')
turtle.onkey(player.increasespeed, 'Up')
turtle.onkey(player.descreasespeed, 'Down')



# Main game loop
while True:
	player.move()