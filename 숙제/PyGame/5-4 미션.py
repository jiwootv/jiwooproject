"""by ziwootv
the game
day: 2021Y July 30D"""
import pygame
import keyboard
s123 = 1
# if keyboard.read_key() == "p":
#     print("You pressed p")
#     break

pygame.init()


class Game123:
    def __init__(self):
        global s123
        self.key = str()
        self.screen = pygame.display.set_mode((640 * 2, 320 * 2))
        self.player_key = str()
        self.stops = True
        s123 = self

    def of_ning(self):
        text1 = self.screen.fill(self, '이 게임은 간단합니다. 그냥 키만 누르세요.')
        text2 = self.screen.fill(self, '제가 말하는 키를 누르시면 됩니다..')
        text3 = self.screen.fill(self, '그럼, 잔말 말고 시작합시다! 시작하시려면 Z키를 누르세요!')
        self.screen.blit(text1, (0, 100))
        self.screen.blit(text2, (0, 200))
        self.screen.blit(text3, (0, 300))
        while self.stops:
            if keyboard.read_key() == 'z':
                text4 = self.screen.fill(self, '알겠습니다. 잔말 말고 갑시다!', pygame.Color('yellow'))

Game = Game123
Game.of_ning()
