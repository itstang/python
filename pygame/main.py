import pygame

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
		self.hitHeight = ypos + PADDLE_HEIGHT
		self.hitWidth = self.x + PADDLE_WIDTH

def drawPaddle(screen, x, y):
	pygame.draw.rect(screen, WHITE, [x,CENTER_SCREEN+y,PADDLE_WIDTH,PADDLE_HEIGHT])

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("A Game?")

done = False
clock = pygame.time.Clock()

y_coord = 0
y_speed = 0

ball_x = 50
ball_y = 50

ball_x_vel = 5
ball_y_vel = 3
# Main Game Loop
while not done:
	# Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				y_speed = -5
			if event.key == pygame.K_DOWN:
				y_speed = 5
			if event.key == pygame.K_ESCAPE:
				done = True
			if event.key == pygame.K_RETURN:
				print(player1.hitWidth)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				y_speed = 0
			if event.key == pygame.K_DOWN:
				y_speed = 0

	# Game Logic

	# Drawing Code
	screen.fill(BLACK)

	pygame.draw.ellipse(screen, WHITE, [ball_x,ball_y,25,25])

	# Border Checking -- Will need to change
	if ball_y > 475 or ball_y < 0:
		ball_y_vel *= -1
	if ball_x > 675 or ball_x < 0:
		ball_x_vel *= -1

	# Animate the ball
	ball_x += ball_x_vel
	ball_y += ball_y_vel

	# Animate the paddle
	y_coord += y_speed

	if y_coord > 200:
		y_coord = 200

	if y_coord < -225:
		y_coord = -225	

	player1 = Paddle(0, 0)
	player2 = Paddle(680, 0)

	drawPaddle(screen, player1.x, y_coord)
	drawPaddle(screen, player2.x, 0)

	player1.y = y_coord
	print(player1.hitHeight)
	#print(ball_y)

	if ball_x == player1.hitWidth and ball_y > player1.y:
		ball_x_vel *= -1

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
