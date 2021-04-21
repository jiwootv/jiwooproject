# 이것은 타이머다.
import time
sec = int(input('Sec'))
min = int(input('Min'))
time.sleep(2)
def time(sec, min):
    for i in range(1, sec + 60 * min):
        time.sleep(1)
        sec = sec - 1
        if sec == 0:
            min = min - 1
        print(min, ':', sec)
        print(min, 'min', sec, 'sec')
    return
time(sec, min)
import winsound
winsound.PlaySound('timer_end.wav', winsound.SND_FILENAME)
