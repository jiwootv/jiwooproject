# 구름 클래스 추가
# 비가 사선으로 내리기
# 구름 클릭하면 구름 제거 하기
# images 안의 back.png 라는 배경 파일도 같이 있어야 실행이 됩니다.
# images 안의 dino.png 라는 공룡 파일도 같이 있어야 실행이 됩니다.
# images 안의 cloud.svg 라는 구름 파일도 같이 있어야 실행이 됩니다.

import pygame
import random
import pygame.sprite
from pygame.locals import *

# 변수
SCREEN_X = 560 * 2  # 화면 넓이
SCREEN_Y = 280 * 2  # 화면 높이
FPS = 60
CLOUD_NUMBER = 20
CHARACTER_SPEED = 5


class Cloud:
    def __init__(self, x, root):
        self.x = x
        self.y = random.randint(0, 200)
        self.image = root.image_cloud
        self.game = root
        self.speed = random.randint(3, 10)

    def move(self):
        self.x += self.speed
        if self.x > SCREEN_X:
            self.x = 0

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        self.game.rains.append(Rain(self.x + random.randint(0, 130), self.y + 70, self.game))

    def click(self):
        pos = pygame.mouse.get_pos()
        rect = self.image.get_rect()
        rect.x = self.x
        rect.y = self.y
        return rect.collidepoint(pos)


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
        return self.y > SCREEN_Y

    def draw(self):
        pygame.draw.line(self.game.screen, self.color, (self.x, self.y), (self.x, self.y + self.len), self.bold)


class Dino:
    def __init__(self, root):
        self.game = root
        self.image = self.game.image_dino
        self.x = SCREEN_X / 2
        self.y = SCREEN_Y - self.image.get_rect().height
        self.speed = random.randint(1, 2)
        self.dx = 0
        self.dy = 0

    def load_data(self):
        pass

    def move(self, key):
        if key == pygame.K_UP:
            self.dy = -CHARACTER_SPEED
            self.dx = 0
        if key == pygame.K_DOWN:
            self.dy = CHARACTER_SPEED
            self.dy = 0
        if key == pygame.K_LEFT:
            self.dx = -CHARACTER_SPEED
            self.dy = 0
        if key == pygame.K_RIGHT:
            self.dx = CHARACTER_SPEED
            self.dy = 0
        if 0 < self.x < SCREEN_X:
            self.x += self.dx
        else:
            self.dx *= -1
            self.x += self.dx

        if 0 < self.y < SCREEN_Y:
            self.y += self.dy
        else:
            self.dy *= -1
            self.y += self.dy

    def off_screen(self):
        return self.x < -self.image.get_rect().width or self.x > SCREEN_X

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('비 오는 날의 비로 인해 으스러진 공룡')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.load_data()
        self.rains = []
        self.clouds = []
        self.dino = Dino(self)

    def load_data(self):
        self.image = pygame.image.load('back.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (SCREEN_X, SCREEN_Y))
        self.image_dino = pygame.image.load('dino.png').convert_alpha()
        self.image_dino = pygame.transform.scale(self.image_dino, (260, 200))
        self.image_cloud = pygame.image.load('cloud.svg').convert_alpha()

    def ending(self):
        self.screen.fill(pygame.Color('black'))
        font = pygame.font.SysFont('malgungothic', 30)
        stop = True
        e = font.render('스페이스바로 게임 종료', True, pygame.Color('white'))
        f = font.render('뭐 게임이라 할순 없지만...', True, pygame.Color('white'))
        g = font.render('봐주셔서 감사!', True, pygame.Color('white'))
        h = font.render('이 저작권은 ziwootv에게 있으며, 허락 없이 사용을 금합니다.', True, pygame.Color('white'))
        self.screen.blit(e, (0, 150))
        self.screen.blit(f, (0, 250))
        self.screen.blit(g, (0, 350))
        self.screen.blit(h, (0, 450))
        pygame.display.flip()
        while stop:
            self.clock.tick(60)
            pygame.event.get()
            self.pressed_key = pygame.key.get_pressed()
            if self.pressed_key[K_SPACE]:
                stop = False

    def run(self):
        self.opening()

        while self.playing:
            font = pygame.font.SysFont('malgungothic', 30)
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
            a = font.render('이 공룡이 보이시나요? 으스러져 죽어갑니다. 산성비 때문에 죽어가죠.', True, pygame.Color('white'))
            b = font.render('이 산성비라는 괴물과 맞먹는 지구온난화도 물리쳐야 해요.', True, pygame.Color('white'))
            c = font.render('그리고 이 문제의 근원 환경오염! 우리 여러명의 실천으로 없어지게 만듭시다. ', True, pygame.Color('white'))
            d = font.render('일단 구름을 클릭해 소멸시켜 주세요!', True, pygame.Color('white'))
            self.screen.blit(a, (0, 150))
            self.screen.blit(b, (0, 250))
            self.screen.blit(c, (0, 350))
            self.screen.blit(d, (0, 450))
            pygame.display.update()
        self.ending()

    def opening(self):
        self.screen.fill(pygame.Color('black'))
        font = pygame.font.SysFont('malgungothic', 30)
        stop = True
        e = font.render('스페이스바로 게임 시작', True, pygame.Color('white'))
        f = font.render('구름 클릭시 소멸', True, pygame.Color('white'))
        g = font.render('방향키로 공룡 조작 ', True, pygame.Color('white'))
        h = font.render('Q키 => 게임 끝', True, pygame.Color('white'))
        self.screen.blit(e, (0, 150))
        self.screen.blit(f, (0, 250))
        self.screen.blit(g, (0, 350))
        self.screen.blit(h, (0, 450))
        pygame.display.flip()
        while stop:
            self.clock.tick(60)
            pygame.event.get()
            self.pressed_key = pygame.key.get_pressed()
            if self.pressed_key[K_SPACE]:
                stop = False

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            # 마우스 버튼이 구름 클릭시 구름 제거
            if event.type == pygame.MOUSEBUTTONDOWN:
                for cloud in self.clouds:
                    if cloud.click():
                        self.clouds.remove(cloud)
                        del cloud
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.playing = False
                self.dino.move(event.key)

    def update(self):
        # 구름 생성
        while len(self.clouds) < CLOUD_NUMBER:
            self.clouds.append(Cloud(random.randint(0, SCREEN_X), self))
        # 구름에서 비 내리기
        for cloud in self.clouds:
            cloud.rain()
        # 비 움직이게 하고 벗어나면 삭제
        for rain in self.rains:
            rain.move()
            if rain.off_screen():
                self.rains.remove(rain)
                del rain
        # 구름 움직이기
        for cloud in self.clouds:
            cloud.move()
        # 공룡 움직이기
        self.dino.move(None)
        if self.dino.off_screen():
            self.dino.speed *= -1
            self.dino.image = pygame.transform.flip(self.dino.image, True, False)

    def draw(self):
        self.screen.fill((255, 255, 255))
        # 배경화면
        self.screen.blit(self.image, (0, 0))
        # 비 그리기
        for rain in self.rains:
            rain.draw()
        # 구름 그리기
        for cloud in self.clouds:
            cloud.draw()
        # 공룡 그리기
        self.dino.draw()


game = Game()
game.run()

pygame.quit()
