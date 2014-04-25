import pygame

# Definitions
pi = 3.1415926535

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("A Game?")

done = False
clock = pygame.time.Clock()

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

	# Game Logic


	# Drawing Code
	screen.fill(BLACK)

	pygame.draw.rect(screen, WHITE, [rect_x,rect_y,50,50])
	pygame.draw.rect(screen, BLACK, [rect_x+10,rect_y+10,30,30])
	if rect_y > 450 or rect_y < 0:
		rect_y_vel *= -1
	if rect_x > 650 or rect_x < 0:
		rect_x_vel *= -1

	rect_x += rect_x_vel
	rect_y += rect_y_vel

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
