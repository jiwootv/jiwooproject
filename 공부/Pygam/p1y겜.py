import pygame
import sys
import random

k = 0

pygame.init()
pygame.display.set_caption("비에 의해서 사람이 죽는 게임")

Screen_x = 1300
Screen_y = 657

screen = pygame.display.set_mode((Screen_x, Screen_y))
clock = pygame.time.Clock()
playing = True


class Rain:
    def __init__(self, x, y, root):
        self.x = x
        self.speed = random.randint(5, 50)
        self.bold = random.randint(1, 10)
        self.y = y

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > Screen_y + 20

    def draw(self):
        pygame.draw.line(self.root.screen, (0, 0, 0), (self.x, self.y), (self.x, self.y + 5), self.bold)

rains = []
for i in range(100):
    rains.append(Rain(random.randint(10, 630), 10))

while playing:

    for event in pygame.event.get():
        pass
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill((255, 255, 255))
    clock.tick(60)
    for rain in rains:
        rain.move()
        rain.draw()


        def event(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False

    game = Game()
    game.run()
    pygame.quit()

    pygame.display.update()
