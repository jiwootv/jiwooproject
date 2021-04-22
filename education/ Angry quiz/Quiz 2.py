# 이 프로그램은 def 명령어를 이용해 업글한 퀴즈 게임 (빡치는) 2편 입니다.
import time
import random  # 타임 모듈과 랜덤 모듈 불러오기
score = 0
q1 = ['1. 10+10은?', '2. 달은 스스로 빛을 낸다 (o 또는 x)', '3. 독일의 유명한 독재자 이름을 쓰시오.',
    '4. 일산화탄소의 분자 구조를 설명하시오.   1. 산소 1개, 탄소 1개 2. 산소 3개 탄소 2개 3. 탄소 7개 산소 5개', '5. 나치 수용소에서 한 여자아이의 경험을 쓴 일기의 이름은?'
]
q2 = ['20', 'x', '히틀러', '1', '안네의 일기']
# 퀴즈, 퀴즈 답 설정
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
        random_v = random.randint(1, 3)  # 렌덤으로 변수를 설정하고 거기에 랜덤으로 변수에 따라 약올리는 메시지를 출력한다.
        if random_v == 1:
            print('이 세상에서 가장 멍청하군요. 지나가던 개미보다 머리가 안 좋군요.')
            time.sleep(1)
            print('저는 지난번보다 독해졌습니다.')
            time.sleep(1)
        elif random_v == 2:
            print('어머! 이런 멍청한 바보를 보았나!')
            time.sleep(1)
            print('헉!')
            time.sleep(1)
        elif random_v == 3:
            print('사람이 똑똑한 사람도 있지만 이렇게 뇌가 없는 사람보다 멍청한 사람이 있구나!')
            time.sleep(1)
            print('참 신기하네!')
            time.sleep(1)

    return
def im_graund():
    print('빡치는 퀴즈쇼에 온걸 환☆영 합니다.')
    time.sleep(1)
    print('이제 끔찍한 악몽을 겪으셔야 합니다.')
    time.sleep(3)
    return
def quiz_run():
    for number in range(0, 5):
        quiz(q1[number], q2[number])
        number = number + 20
def the_end():
    print('당신의 점수는', score * 10, '입니다.')
    if score * 10 > 60:
        print('잘 하셨네요.')
        time.sleep(1)
        print('당신이 7살 이하라면...')
        time.sleep(5)
    else:
        print('당신. 이 정도 쉬운 문제도 못 풀다니...')
        time.sleep(1)
        print('당신. 초등학교 과정부터 다시 하세요. ')

        time.sleep(5)
im_graund()
quiz_run()
the_end()
