import random
import time

class Cuckie:  # 항상 클래스는 대문자로 쓴다.
    def __init__(self):
        self.x = random.randint(0, 100) # '독이 들어있는 쿠키{청산가리 함유, 우라늄 함유}'
    def burn(self):
        print("쿠키가 gu워졌어요. 그런데 nog았어요.")
print(Cuckie)
cuckie1 = Cuckie()
cuckie22 = Cuckie()
cuckie333 = Cuckie()
cuckie4444 = Cuckie()

cuckie1.burn()
print(cuckie1.x)
time.sleep(5)
print(cuckie22.x)
time.sleep(5)
print(cuckie333.x)
time.sleep(5)
print(cuckie4444.x)
time.sleep(5)
