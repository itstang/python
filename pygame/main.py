import pygame
from random import randrange

# Definitions
pi = 3.1415926535

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

PADDLE_HEIGHT = 75
PADDLE_WIDTH = 20

CENTER_SCREEN = 225

pygame.init()

class Paddle(object):
	def __init__(self, xpos, ypos):
		self.x = xpos
		self.y = ypos + 200
		self.y_vel = 0
		self.hitHeight = 0
		self.hitWidth = xpos + PADDLE_WIDTH
	def setHeight(self, ypos):
		self.height = ypos + PADDLE_HEIGHT + 225
		return self.height
	def checkBounds(self):
		if self.y > 200:
			self.y = 200

		if self.y < -225:
			self.y = -225

class Ball(object):
	def __init__(self, screen, xpos, ypos):
		self.x = xpos
		self.y = ypos
		self.x_vel = 0
		self.y_vel = 0
	def drawBall(self, xpos, ypos):
		pygame.draw.ellipse(screen, WHITE, [xpos,ypos,25,25])
	def ballSpeed(self):
		self.x_vel = 5
		self.y_vel = 3

def drawPaddle(screen, x, y):
	pygame.draw.rect(screen, WHITE, [x,CENTER_SCREEN+y,PADDLE_WIDTH,PADDLE_HEIGHT])

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("A Game?")

done = False
clock = pygame.time.Clock()


ball = Ball(screen, 350, 250)
player1 = Paddle(0, 250)
player2 = Paddle(680, 250)

# Main Game Loop
while not done:
	# Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				# Start Game
				if ball.x_vel == 0 and ball.y_vel == 0:
					ball.x_vel = randrange(-10, -5)
					ball.y_vel = randrange(-3, -1)
				player2.y_vel = -5
			if event.key == pygame.K_DOWN:
				# Start Game
				if ball.x_vel == 0 and ball.y_vel == 0:
					ball.x_vel = randrange(-10, -5)
					ball.y_vel = randrange(1, 3)
				player2.y_vel = 5

			if event.key == pygame.K_w:
				# Start Game
				if ball.x_vel == 0 and ball.y_vel == 0:
					ball.x_vel = 5
					ball.y_vel = 3
				player1.y_vel = -5
			if event.key == pygame.K_s:
				# Start Game
				if ball.x_vel == 0 and ball.y_vel == 0:
					ball.x_vel = 5
					ball.y_vel = 3
				player1.y_vel = 5

			if event.key == pygame.K_ESCAPE:
				done = True
			

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player2.y_vel = 0
			if event.key == pygame.K_DOWN:
				player2.y_vel = 0

			if event.key == pygame.K_w:
				player1.y_vel = 0
			if event.key == pygame.K_s:
				player1.y_vel = 0

	# Game Logic

	# Drawing Code
	screen.fill(BLACK)

	ball.drawBall(ball.x, ball.y)

	# Border Checking -- Will need to change
	if ball.y > 475 or ball.y < 0:
		ball.y_vel *= -1
	elif ball.x < 0:
		ball.x = player2.x-20
		ball.y = player2.hitHeight-(PADDLE_HEIGHT/2)
		ball.x_vel = 0
		ball.y_vel = 0
	elif ball.x > 675:
		ball.x = 350
		ball.y = 250
		ball.x_vel = 0
		ball.y_vel = 0

	# Animate the ball
	ball.x += ball.x_vel
	ball.y += ball.y_vel

	# Animate the paddle
	player1.y += player1.y_vel
	player2.y += player2.y_vel

	# Top/Bottom Boundries
	player1.checkBounds()	
	player2.checkBounds()

	drawPaddle(screen, player1.x, player1.y)
	drawPaddle(screen, player2.x, player2.y)

	player1.y = player1.y
	player2.y = player2.y

	# Update the hitbox height
	player1.hitHeight = player1.setHeight(player1.y)
	player2.hitHeight = player2.setHeight(player2.y)

	# Paddle hit detection
	if ball.x <= player1.hitWidth:
		if ball.y < player1.hitHeight and ball.y > (player1.y+225):
			ball.x_vel *= -1

	if (ball.x+25) > player2.x:
		if ball.y < player2.hitHeight and ball.y > (player2.y+225):
			ball.x_vel *= -1

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
