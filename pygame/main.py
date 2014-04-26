import pygame

# Definitions
pi = 3.1415926535

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

def drawPaddle(screen, x, y):
	pygame.draw.rect(screen, WHITE, [x,225+y,20,75])

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("A Game?")

done = False
clock = pygame.time.Clock()

y_coord = 0
y_speed = 0

rect_x = 50
rect_y = 50

rect_x_vel = 5
rect_y_vel = 3
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

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				y_speed = 0
			if event.key == pygame.K_DOWN:
				y_speed = 0

	# Game Logic

	# Drawing Code
	screen.fill(BLACK)

	pygame.draw.ellipse(screen, WHITE, [rect_x,rect_y,25,25])

	if rect_y > 475 or rect_y < 0:
		rect_y_vel *= -1
	if rect_x > 675 or rect_x < 0:
		rect_x_vel *= -1

	rect_x += rect_x_vel
	rect_y += rect_y_vel

	y_coord += y_speed

	if y_coord > 200:
		y_coord = 200
		print("hit")
	if y_coord < -200:
		y_coord == 0
		print("top")

	drawPaddle(screen, 0, y_coord)
	drawPaddle(screen, 680, 0)

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
