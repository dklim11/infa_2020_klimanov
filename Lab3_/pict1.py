import pygame
from pygame.draw import *

pygame.init()

fps = 30
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))

rect(screen, (255, 255, 255), (50, 50, 400, 400)) #font
circle(screen , (255, 200, 50), (250, 250), 150, 150) #face
rect(screen, (0, 0, 0), (190, 300, 120, 20)) #mouth
circle(screen, (255, 0, 0), (185, 185), 25, 25) #eye1ext
circle(screen, (255, 0, 0), (315, 185), 20, 20) #eye2ext
circle(screen, (0, 0, 0), (185, 185), 15, 15) #eye1int
circle(screen, (0, 0, 0), (315, 185), 15, 15) #eye2int
polygon(screen, (0, 0, 0), [[165, 135], [220, 180]], 15) #eyebrow1
polygon(screen, (0, 0, 0), [[285, 170], [340, 150]], 15) #eyebrow2

pygame.display.update()

while True:
	clock.tick(fps)
	for event in pygame.event.get():
        	if event.type == pygame.QUIT:
            		pygame.quit()