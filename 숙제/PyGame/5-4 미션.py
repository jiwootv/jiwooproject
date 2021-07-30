"""by Mr.z
the game
day: 2021Y July 30D"""

"""이 코드를 만드는 것을 도와주신 우리 frashia 선생님 감사합니다!
코드 만드는데 2시간 걸렸나..?
역시 코딩의 정석은 이거야!
《코딩의 퀄리티 = 지식 ÷ 2 × 시간》"""
import pygame, random, keyboard
import pygame.font

s123 = 1
# if keyboard.read_key() == "p":
#     print("You pressed p")
#     break

pygame.init()  # 초기화


class Gamecode:
    def __init__(self):  # __init으로 변수 생성
        self.RandomAi_Present_key = '<= AI Present_key'  # AI 전용 키 (27번줄 참고)
        self.setplayer_Present_key = '<= Player present_key'  # 사람 전용 키
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'm', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']  # <= 여기에 있는 노가다의 흔적
        # self.txt = ''
        # self.End = None
        # 위에 있는 사라진 비운의 코드 ㅠㅠ

    def randomaisetkey(self):  # 랜덤으로 AI가 누른 키를 설정해 줌. (한 알파벳당 나올 확률: 3.84615384...%
        self.RandomAi_Present_key = self.alphabet[random.randint(0, 26)]

    def manyag(self):  # 말 그대로 만약
        if keyboard.read_key() == self.RandomAi_Present_key:  # 확률의 미띤놈! 3.846153846153846%
            print('GOOD')  # 3.846153846153846%의 확률로 같은 키를 누르면 창에 GOOD 이라고 뜬다.
            pygame.quit()
        else:
            print('bad')
            pygame.quit()  # 그냥 나가짐... 그것도 96.15834615384515%의 확률로...


class Event:
    def __init__(self):  # 그냥 여긴 별로 하는 짓이 없음...

        self.font = pygame.font.SysFont('malgungothic', 10)  # 폰트 생성
        self.screen = pygame.display.set_mode((640 * 2, 320 * 2))  # |

    #                                                                   v 여기에!
    def of_ning(self):
        text1 = self.font.render('이 게임은 간단합니다. 그냥 키만 누르세요.', True,
                                 pygame.Color('red'))  # 운빨이 좋아야 나옴 (그 현질의 전설 냥코보다 높긴 하지만 장난아님(냥코의 울슈레 확률이 0.5%))
        text2 = self.font.render('Ai의 키와 같은 키를 누르면 끝납니다.(파일로는 안뜨지만 터미널에 잘했다고 떠요) 한번 운 테스트 가보죠?', True,
                                 pygame.Color('blue'))
        text3 = self.font.render('그럼, 잔말 말고 시작합시다! 시작하시려면 Z키를 누르세요! 하지만 확률은 3.846153846153846%입니다...', True,
                                 pygame.Color('yellow'))
        self.screen.blit(text1, (0, 100))  # 출력!
        self.screen.blit(text2, (0, 200))
        self.screen.blit(text3, (0, 300))
        pygame.display.flip()
        while True:
            if keyboard.read_key() == 'z':
                #      (원래 코드가 있던 자리)
                # (삼가 코드 고인의 명복을 빕니다...)
                run()
                break


eve = Event()  # 변수에 클래스를 쑤셔넣기
Game = Gamecode()


def run():
    pygame.time.wait(60)  # 멈추는 코드요. 숫자 1당 밀리초입니다.( 1당 0.1초) 저는 5초로 했어요.
    Game.randomaisetkey()  # 코드 실행!

    Game.manyag()
    return


eve.of_ning()
run()  # 최종 코드
