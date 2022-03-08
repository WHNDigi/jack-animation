import pygame

pygame.init()

window = pygame.display.set_mode((900, 750))
action = ["Idle","Walk","Run","Jump","Slide","Dead"]

mode = action[2]
speed = 30

image_sprite = [pygame.image.load("jack/"+mode+" (1).png"),
		pygame.image.load("jack/"+mode+" (2).png"),
		pygame.image.load("jack/"+mode+" (3).png"),
		pygame.image.load("jack/"+mode+" (4).png"),
		pygame.image.load("jack/"+mode+" (5).png"),
		pygame.image.load("jack/"+mode+" (6).png"),
		pygame.image.load("jack/"+mode+" (7).png"),
		pygame.image.load("jack/"+mode+" (8).png"),
		pygame.image.load("jack/"+mode+" (9).png"),
		pygame.image.load("jack/"+mode+" (10).png")]

clock = pygame.time.Clock()
value = 0
for i in range(300):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	clock.tick(speed)
	if value >= len(image_sprite):
		value = 0
	image = image_sprite[value]
	window.blit(image, (0, 0))
	pygame.display.update()
	window.fill((0, 0, 0))
	value += 1
pygame.quit()
