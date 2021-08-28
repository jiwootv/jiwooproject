# 파이게임 기본 코드
import pygame.font
import pygame
import random
vec = pygame.Vector2

pygame.init()
pygame.display.set_caption('게임 제목')
Screen_x = 640  # 화면 넓이
Screen_y = 480  # 화면 높이


class Ui(pygame.sprite.Sprite):
    def __init__(self, root):
        self.game = root
        self.groups = self.game.ui
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((Screen_x, Screen_y))
        self.rect = self.image.get_rect()

        self.image.set_colorkey('Black')

        self.ui_health = self.game.sa.health
    def draw_text(self, text, size, color, x, y):
        font = pygame.font.SysFont('malgungodic', size)
        text_suface = font.render(text, True, color)
        text_rect = text_suface.get_rect()
        text_rect.x = x
        text_rect.y = y
        self.image.blit(text_suface, text_rect)
    def update(self):
        self.image.fill('Black')
        pygame.draw.rect(self.image, 'Gray', (0, 0, Screen_x+3, Screen_y+18), 10, 10)
        self.ui_health = self.game.sa.health
        pygame.draw.line(self.image, 'Sky blue', (100, Screen_y-100), (100+self.ui_health, Screen_y-100), 15)
        self.draw_text(f'Hp: {self.ui_health}', 40, pygame.Color('Blue'), 0, 0)



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
        self.health = 300


    def update(self):
        # self.angle += 1
        self.health -= 1

        self.image = pygame.transform.rotozoom(self.image_t, self.angle, 1)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        if self.pos.x > Screen_x:
            self.pos.x = 0
        self.x123 += 0
        self.pos.y = Screen_y * 8 / 10
        self.rect.centerx = Screen_x / 2
        if self.game.pressed_key[pygame.K_RIGHT]:
            self.pos.x += 2
        if self.game.pressed_key[pygame.K_LEFT]:
            self.pos.x += -2
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
        self.pressed_key = pygame.key.get_pressed()
        self.screen = pygame.display.set_mode((Screen_x, Screen_y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprites = pygame.sprite.Group()
        self.sa = Sa(self)
        self.rains = []
        self.ui = pygame.sprite.GroupSingle()
        self.ui.add(Ui(self))
        self.bg = pygame.image.load(('모양 3 (1).svg'))
        self.bg = pygame.transform.scale(self.bg, (Screen_x, Screen_y))
        pygame.mixer.init()
        pygame.mixer.music.load('JOJO7.mp3')

        self.camra = vec(0, 0)
        self.bgcamra = vec(0, 0)



    def run(self):

        while self.playing:
            self.clock.tick(60)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()

    def event(self):
        self.pressed_key = pygame.key.get_pressed()
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
        self.ui.update()
        self.ui.update()
        for sprite in self.all_sprites:
            if self.pressed_key[pygame.K_RIGHT]:
                sprite.pos.x -= 1
            if self.pressed_key[pygame.K_RIGHT]:
                sprite.pos.x += 1

    def draw(self):
        self.screen.fill((255, 255, 0))
        self.all_sprites.draw(self.screen)
        for rain in self.rains:
            rain.draw()
        self.ui.draw(self.screen)


game = Game()
game.run()
pygame.quit()
