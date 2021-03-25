import random
import time
score = 0
x = random.randint(1, 64)
y = random.randint(1, 64)
z = random.randint(1, 64)
a = random.randint(1, 64)
b = random.randint(1, 64)
c = random.randint(1, 64)
x_anser = int(input('number 1 (첫 번째 숫자'))
y_anser = int(input('number 2 (두 번째 숫자'))
z_anser = int(input('number 3 (세 번째 숫자'))
a_anser = int(input('number 4 (네 번째 숫자'))
b_anser = int(input('number 5 (다섯 번째 숫자'))
c_anser = int(input('number 6 (여섯 번째 숫자'))
print(z)
print(x)
print(c)
print(a)
print(b)
print(c)
time.sleep(1)
print('번호는 다음과 같습니다.')
if x == x_anser:
    score=score + 2
else:
    print ('아... 원래 1번째 번호는', x, '였는데...')
if y == y_anser:
    score = score + 2
else:
    print('아... 원래 2번째 번호는', y, '였는데...')
if z == z_anser:
    score = score + 2
else:
    print('아... 원래 3번째 번호는', z, '였는데...')
if a == a_anser:
    score = score + 2
else:
    print('아... 원래 4번째 번호는', a, '였는데...')

