print('1번째 문제')
number = 0
for i in range(1000):
    number += 1
    if number % 3 == 0 or number % 5 == 0:
        print(number)
print('2번째 문제')
number2 = int(input('숫자 내놔. 안 숫자 안 주면 죽인다.'))
if 10000 < number2:
    print('아주 큰수 (아.. 너무 크다)')
elif 1000 < number2:
    print('큰수 (조금 큰 수)')
elif 100 < number2:
    print('작은수 (그리 크지 않은 수)')
print('3번째 문제')
number3 = input('글자 아니면 숫자 내놔. 안 주면 죽인다.')
key = 0
if number3.isalpha():
    print('문.자.열(str)')
else:
    for i in number3:
        if i == '.':
            print('소.수.다(float)')
            key = 0
            break
        else:
            key = 1
    if key == 1:
        print('숫.자.다(int)')
