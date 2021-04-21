print('mr. 파2썬으로 만든 0이 몇개 있는지  아는 기계(0이 1개: 완성 메시지 출력 (0 2개 이상: 그냥 끝')
import time
time.sleep(2)
print('사실 쌤이 숙제낸건데 코드가 늦게 편집되서 만들다가 또 다른 버전으로 만들어봄')
number = 0
number2 = 0
answer = (input('수 입력'))
int(answer)
answer_len = len(answer)
abc = int(0)
number3 = 0
for number in range(0, answer_len):
    abc = (answer[number])
if int(abc) == 0:
    number3 = number3+1
if number3 == 1:
        print("완성")
