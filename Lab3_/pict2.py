import pygame
from pygame.draw import *

pygame.init()

def fish():	
	ellipse(screen, (13, 110, 60), [400, 570, 80, 30])
	circle(screen, (0, 0, 250), (460, 585), 5, 5)
	circle(screen, (0, 0, 0), (461, 585), 2, 2)
	polygon(screen, (136, 5, 0), [[400, 585], [380, 588], [385, 570], [403, 578]], 0)
	polygon(screen, (136, 5, 0), [[440, 570], [430, 555], [455, 560], [450, 572]], 0)
	polygon(screen, (136, 5, 0), [[440, 600], [450, 599], [455, 605], [438, 610]], 0)
	polygon(screen, (136, 5, 0), [[420, 597], [430, 599], [430, 605], [418, 610]], 0)
def bodyBird():
	ellipse(screen, (255, 255, 255), [150, 500, 130, 70])
	ellipse(screen, (255, 255, 255), [250, 510, 80, 30])	
	ellipse(screen, (255, 255, 255), [310, 495, 50, 30])
	ellipse(screen, (0, 0, 0), [340, 500, 8, 8])
	ellipse(screen, (255, 255, 255), [170, 540, 80, 50])
	ellipse(screen, (255, 255, 255), [176, 550, 40, 50])
	ellipse(screen, (255, 255, 255), [220, 575, 70, 15])
	ellipse(screen, (255, 255, 255), [185, 590, 65, 15])

	#tail
	polygon(screen, (255, 255, 255), [[150, 540], [110, 530], [120, 500], [160, 520]], 0)	

def wingsBird():
	polygon(screen, (255, 255, 255), [[180, 510], [160, 480], [100, 465], [90, 450], [165, 445], [220, 450], [223, 500]], 0)
	polygon(screen, (255, 255, 255), [[190, 500], [170, 470], [110, 455], [100, 440], [155, 435], [230, 440], [233, 520]], 0)

def font():
	rect(screen, (23, 11, 125), (0, 0, 600, 80))
	rect(screen, (88, 93, 238), (0, 80, 600, 50))
	rect(screen, (225, 137, 201), (0, 130, 600, 80))
	rect(screen, (235, 93, 197), (0, 210, 600, 100))
	rect(screen, (243, 165, 49), (0, 310, 600, 90))
	rect(screen, (6, 120, 195), (0, 400, 600, 300))	

def albatrosses():
	arc(screen, (255, 255, 255), [30, 30, 60, 30], pi/6, 7*pi/6, 2)
	arc(screen, (255, 255, 255), [85, 25, 60, 30], pi/12, pi, 2)

	arc(screen, (255, 255, 255), [300, 150, 70, 40], 0, pi, 3)
	arc(screen, (255, 255, 255), [370, 150, 70, 40], 0, pi, 3)

	arc(screen, (255, 255, 255), [50, 220, 60, 40], 0, 11*pi/12, 3)
	arc(screen, (255, 255, 255), [108, 223, 60, 40], 0, 11*pi/12, 3)

def beak():
	polygon(screen, (255, 232, 0), [[357, 505], [383, 505], [375, 512], [357, 512]], 0)

def clutches():
	polygon(screen, (255, 232, 0), [[285, 578], [305, 582], [290, 585], [300, 590], [285, 592], [280, 600], [280, 586]])
	polygon(screen, (255, 232, 0), [[250, 595], [270, 599], [255, 602], [265, 607], [250, 609], [245, 617], [245, 599]])

fps = 30
pi = 3.14
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 700))

font()
albatrosses()
bodyBird()
wingsBird()
fish()
beak()
clutches()

pygame.display.update()
finised = False

while True:
	clock.tick(fps)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True
pygame.quit()