# 파이게임 기본(클래스)

import pygame, random

# 전역상수
SCREEN_X = 640  # 화면 넓이
SCREEN_Y = 480  # 화면 높이
FPS = 60
vec = pygame.math.Vector2


class Mogi(pygame.sprite.Sprite):
    def __init__(self, root):
        self.image = pygame.image.load('mr.mogi.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.game = root
        self.groups = self.game.all_sprite, self.game.mogi
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect.center = (100, 30)
        self.pos = vec(random.randint(0, SCREEN_X), 50)
        self.dir = vec(0,0)
        self.time = pygame.time.get_ticks()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.dir = vec(random.random() * random.randint(-20, 20), random.random() * random.randint(-20, 20))
        if pygame.time.get_ticks() - self.time < 2000:
            self.time = pygame.time.get_ticks()
            self.pos += self.dir
            self.rect.center = self.pos
        if self.pos.x < 0 or self.pos.x > SCREEN_X:
            self.kill()
            del self
            return
        self.event()
    def event(self):
        if pygame.sprite.collide_mask(self, self.game.stick) and pygame.mouse.get_pressed(3)[0]==True:
            print(pygame.mouse.get_pressed(3))
            print('잡음')
            self.kill()
            del self
            return



class Mogistick(pygame.sprite.Sprite):
    def __init__(self, root):
        self.image = pygame.image.load('mogi_stic.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.game = root
        self.groups = self.game.all_sprite, self.game.mogichea
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect.center = (100, 30)
        self.pos = vec(random.randint(0, SCREEN_X), 50)
        self.dir = vec(0,0)
        self.time = pygame.time.get_ticks()
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        self.pos = pygame.mouse.get_pos()
        self.rect.bottomright = self.pos - vec(-22, -23)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임 제목')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprite = pygame.sprite.Group()
        self.mogi = pygame.sprite.Group()
        self.mogichea = pygame.sprite.Group()
        self.stick = Mogistick(self)
        self.all_sprite.add(self.stick)
        self.mogichea.add(self.stick)


    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()

    def event(self):
        # 종료 코드
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.all_sprite.update()
        if len(self.mogi)< 50:
            self.mogi_sprite = Mogi(self)
            self.all_sprite.add(self.mogi_sprite)
            self.mogi.add(self.mogi_sprite)

    def draw(self):
        self.screen.fill(pygame.Color('White'))
        self.all_sprite.draw(self.screen)


game = Game()
game.run()
pygame.quit()
