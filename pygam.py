import pygame, random, time, sys
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1300, 600))
chracter_img = pygame.image.load('sans2 (1).svg').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(chracter_img, (100, 100))
    pygame.display.update()
