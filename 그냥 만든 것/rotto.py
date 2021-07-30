import random

import time
# time 모듈과 random 모듈을 불러온다. (import random, time)

score = 0  # 점수를 0으로 정한다. (Set the score to 0)
x = random.randint(1, 63)  # x, y, z, a, b, c 이 변수들을 1 ~ 64 사이의 수로 정한다.
y = random.randint(1, 63)  # (x, y, z, a, b, c set these variables to numbers between 1 and 64.)
z = random.randint(1, 63)
a = random.randint(1, 63)
b = random.randint(1, 63)
c = random.randint(1, 63)

print('1부터 63 사이의 숫자를 입력해 주세요. (Please enter a number between 1 and 63.) ')
time.sleep(1)
x_answer = int(input('number 1 (첫 번째 숫자)'))  # 사용자의 답을 받는다
y_answer = int(input('number 2 (두 번째 숫자)'))  # Receive the user's answer
z_answer = int(input('number 3 (세 번째 숫자)'))
a_answer = int(input('number 4 (네 번째 숫자)'))
b_answer = int(input('number 5 (다섯 번째 숫자)'))
c_answer = int(input('number 6 (여섯 번째 숫자)'))
time.sleep(1)
print('번호는 다음과 같습니다. (The number is as follows)')
if x == x_answer:
    score = score + 2
else:
    print('아... 원래 1번째 번호는', x, '였는데...', 'Oh... Originally the first number was', x, '...')
time.sleep(1)
if y == y_answer:
    score = score + 2
else:
    print('아... 원래 2번째 번호는', y, '였는데...', 'Oh... the original second number is', y, '...')
time.sleep(1)
if z == z_answer:
    score = score + 2
else:
    print('아... 원래 3번째 번호는', z, '였는데...', 'Oh... the 3rd number was originally', z, '...')
time.sleep(1)
if a == a_answer:
    score = score + 2
else:
    print('아... 원래 4번째 번호는', a, '였는데...', 'Oh... the 4rd number was originally', a, ' ...')
time.sleep(1)
if b == b_answer:
    score = score + 2
else:
    print('아... 원래 5번째 번호는', b, '였는데...', 'Oh... the 5rd number was originally', b, ' ...')
time.sleep(1)
if c == c_answer:
    score = score + 2
else:
    print('아... 원래 6번째 번호는', c, '였는데...', 'Oh... the 6rd number was originally', c, ' ...')
time.sleep(1)
print('당신의 점수는', score*10, '입니다. (120점 만점)', 'Your score is', score*10, '. (Out of 120 points) ')
time.sleep(5)
input('이 프로젝트를 끝내시려면 아무 글자나 입력해 주세요.')
