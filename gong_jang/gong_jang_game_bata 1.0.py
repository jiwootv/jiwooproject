# this is bata version 1.0
def text():
    print()
    return


import pygame, sys
pygame.init()
screen = pygame.display.set_mode((1300, 600))
font = pygame.font.SysFont('malgungothic', 5)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()
