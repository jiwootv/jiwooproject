# 파이게임 기본 코드
import pygame, random

pygame.init()
pygame.display.set_caption('게임 제목')
Screen_x = 640  # 화면 넓이
Screen_y = 480  # 화면 높이


# 파이게임 기본 코드(클래스)

class Sa(pygame.sprite.Sprite):
    def __init__(self, root):
        self.game = root
        self.image = pygame.image.load('DARK Knight.png')
        self.image = pygame.transform.scale(self.image, (200, 200))
        # self.image = pygame.Surface((200, 50))
        # self.image.fill('Red')
        self.image_t = self.image
        self.rect = self.image.get_rect()
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect.centerx = Screen_x / 2
        self.rect.centery = Screen_y / 2
        self.rect.centerx += 1
        self.angle = 0
        self.mask = self.image.get_masks()
        self.pos = pygame.math.Vector2(0, 0)
        self.x123 = 1

    def update(self):
        # self.angle += 1
        self.image = pygame.transform.rotozoom(self.image_t, self.angle, 1)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.pos.x += self.x123
        if self.pos.x > Screen_x:
            self.pos.x = 0
        self.x123 += 0.1
        self.pos.y = Screen_y * 8 / 10
        self.rect.centerx = Screen_x / 2
        self.rect.centerx += 1
        self.rect.centery = Screen_y * 8 / 10
        self.rect.center = self.pos
class Rain:
    def __init__(self, x, y, root):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 58)
        self.bold = random.randint(1, 4)
        self.game = root
        self.len = random.randint(5, 35)
        self.color = pygame.Color('black')

    def move(self):
        self.y += self.speed
        self.x += 4

    def off_screen(self):
        return self.y > Screen_y

    def draw(self):
        pygame.draw.line(self.game.screen, self.color, (self.x, self.y), (self.x, self.y + self.len), self.bold)


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('화면 보호기(?)')
        self.screen = pygame.display.set_mode((Screen_x, Screen_y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprites = pygame.sprite.Group()
        self.sa = Sa(self)
        self.rains = []

    def run(self):
        while self.playing:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        self.rains.append(Rain(random.randint(0, Screen_x), 100, self))

    def update(self):
        self.all_sprites.update()
        for rain in self.rains:
            rain.move()
            if rain.off_screen():
                self.rains.remove(rain)
                del rain

    def draw(self):
        self.screen.fill((255, 255, 0))
        self.all_sprites.draw(self.screen)
        for rain in self.rains:
            rain.draw()


game = Game()
game.run()
pygame.quit()
