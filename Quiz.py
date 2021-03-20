# 이 프로그램은 아주아주아주 간단한 퀴즈를 내는 프로그램 입니다.
import time
anser=0
score=0
답=3
print ("이제부터 간단한 퀴즈를 내겠습니다.")  #퀴즈 내겠다고 말하는 코드
print ("첫 번째 문제입니다.")
time.sleep(1)
print('''(24×20)÷10은 무엇인가요?
      1) 30
      2) 29
      3) 48
      4) 18''')     # 머리아픈 수학문제. 답은 3번
anser=int(input())
if anser==답 :
    print ('두구두구두구두구...')
    time.sleep(1)
    print ("정답!!! ^-^") #맞으면 축하해줌
    score=score+1
else:
    print('두구두구두구두구...')
    time.sleep(1)
    print("틀렸습니다... 당신, 성적이 어느정도길래 이렇게 쉬운 문제를 틀린 겁니까?")#틀리면 아쉬워함

#2번째 문제
print("두 번째 문제입니다.")
time.sleep(1)
답=4
print('''이 세상에서 가장 똑똑한 사람은?
      1) 알버트 아인슈타인
      2) 제작자
      3) 니콜라 테슬라
      4) 지나가던 아저씨''')    # 지나가던 아저씨가 젤 똑똑함....(실제론 당근 아님 장난식 문제임 )답은 4번
anser=int(input())
if anser==답 :
    print ('두구두구두구두구...')
    time.sleep(1)
    print ("정답!!! ^-^") #맞으면 축하해줌
    score=score+1
else:
    print('두구두구두구두구...')
    time.sleep(1)
    print("틀렸습니다... 이걸 모르다니 우주에서 가장 멍청한 똥멍청이군요")#틀리면 아쉬워함
    print("세 번째 문제입니다.")
time.sleep(1)
답=746531
print('''수 카드 1,3,4,5,6,7 이 숫자 카드를 단 한 번씩만 사용하여 만들수 있는 만의 자리가 4인 가장 큰 수는?(대신 콤마는 답에 넣지 말아주세요''')
anser=int(input())
if anser==답 :
    print ('두구두구두구두구...')
    time.sleep(1)
    print ("정답!!! ^-^") #맞으면 축하해줌
    score=score+1
else:
    print('두구두구두구두구...')
    time.sleep(1)
    print("틀렸습니다... 당신, 성적이 어느정도길래 이렇게 쉬운 문제를 틀린 겁니까?")#틀리면 아쉬워함
print ('당신의 점수는 ', score*10, '점입니다.(30점 만점)')
if score==3 :
    print ('정말 똑똑합니다!')
    time.sleep(1)
    print ("최고!!!")
    time.sleep(5)
else:
    print('두구두구두구두구...')
    time.sleep(1)
    print("틀렸습니다... 당신, 성적이 어느정도길래 이렇게 쉬운 문제를 틀린 겁니까? 우주 바깥과 우주에서 가장 똥멍청이군요.")#틀리면 아쉬워함
    time.sleep(5)