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

player = Player()
# print('\n\nType: {}; What is it: {}\n List of methods: {}\n'.format(type(player), player, dir(player)))


# Main game loop
while True:
	player.move()