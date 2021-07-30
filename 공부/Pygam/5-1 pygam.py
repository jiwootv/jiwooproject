import pygame
import random

SCREEN_X = 580 * 2
SCREEN_Y = 280 * 2
FPS = 60


class Rain:
    def __init__(self, x, y, root):
        self.x = x
        self.speed = random.randint(1, 20)
        self.bold = random.randint(1, 4)
        self.y = y
        self.root = root

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > SCREEN_Y + 30

    def draw(self):
        pygame.draw.line(self.root.screen, (0, 0, 220), (self.x, self.y), (self.x, self.y + 5), self.bold)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        self.clock = pygame.time.Clock()
        self.playing = True
        self.rains = []

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.move()
            self.draw()
            pygame.display.update()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        # 비생성
        for _ in range(10):
            self.rains.append(Rain(random.randint(0, SCREEN_X), 10, self))
        # 비가 화면 넘어가면 삭제
        for rain in self.rains:
            if rain.off_screen():
                self.rains.remove(rain)
                del rain


    def draw(self):
        self.screen.fill((255, 255, 255))
        for rain in self.rains:
            rain.draw()
    def move(self):
        for rain in self.rains:
            rain.move()


game = Game()
game.run()
pygame.quit()
