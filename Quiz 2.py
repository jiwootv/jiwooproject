# 이 프로그램은 def 명령어를 이용해 업글한 퀴즈 게임 (빡치는) 2편 입니다.
import time
import random
score = 0
q1=['1. 10+10은?','2. 달은 스스로 빛을 낸다 (o 또는 x)', '3. 독일의 유명한 독재자 이름을 쓰시오. ']
q2=['20', 'o','히틀러']
def quiz(quiz, answer):
    global score
    global radom_v
    user_answer = input(quiz)
    if answer == user_answer:
        score = score+1
        print('맞으셨균요. 하지만 이 퀴즈를 맞췄다고 잘 한다고 말하는 바보 따위는 없겠죠. ')
        time.sleep(1)
        print('저는 지난번보다 독해졌습니다.')
        time.sleep(1)
    else:
        random_v=random.randint(1, 3)
        if random_v==1:
            print('이 세상에서 가장 멍청하군요. 지나가던 개미보다 머리가 안 좋군요.')
            time.sleep(1)
            print('저는 지난번보다 독해졌습니다.')
            time.sleep(1)
        elif random_v==2:
            print('어머! 이런 멍청한 바보를 보았나!')
            time.sleep(1)
            print('헉!')
            time.sleep(1)
        elif random_v==3:
            print('사람이 똑똑한 사람도 있지만 이렇게 뇌가 없는 사람보다 멍청한 사람이 있구나!')
            time.sleep(1)
            print('참 신기하네!')
            time.sleep(1)

    return
def im_graund():
    print ('빡치는 퀴즈쇼에 온걸 환☆영 합니다.')
    time.sleep(1)
    print ('이제 끔찍한 악몽을 겪으셔야 합니다.')
    time.sleep(3)
    return
def quiz():

    global number
    for number in range(0, 3):
        quiz(q1[number], q2[number])
        number = number + 1
im_graund()
number=int()


