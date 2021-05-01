y = 100

import pygame, sys
sound = pygame.mixer.sound('')
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1300, 600))
chracter_img = pygame.image.load('sans2 (1).svg')
font = pygame.font.SysFont('malgungothic', 50)
x = 0
key = 0
key_y = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # x += random.randint(1,10)
        if event.type == pygame.KEYDOWN:
            if event.key == (pygame.K_a or pygame.K_RIGHT):
                key = -1
            if event.key == (pygame.K_d or pygame.K_LEFT):
                key = 1
            if event.key == (pygame.K_s or pygame.K_UP):
                key_y = 1
            if event.key == (pygame.K_w or pygame.K_UP):
                key_y = -1
        if event.type == pygame.KEYUP:
            key = 0
            key_y = 0
        if x > 1300:
            x = 0



    x += key
    y += key_y
    screen.fill((255, 255, 255))
    a = font.render(f'x 좌표: {x} y 좌표:{y}', True, (255, 0, 0))
    screen.blit(chracter_img, (x, y))
    screen.blit(a, (650, 150))
    if x > 1300:
        x = 0
    if -320 > x:
        x = 1300
    clock.tick(60)
    pygame.display.update()
