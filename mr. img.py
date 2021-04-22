from turtle import forward as 앞으로
from turtle import backward as 뒤로
from turtle import left as 왼쪽
from turtle import pensize as 굵기
from turtle import speed as 속도
from turtle import pencolor as 색
from turtle import clear as 지우기
from turtle import circle as 원

import random
import turtle
import winsound
굵기(5)
색종류=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
turtle.shape("turtle")

# 색의 종류 red, orange, yellow, green, blue, indigo, violet
def 사각형_함수():
    for i in range(10):
        속도(10)
        왼쪽(10)
        앞으로(100)
        왼쪽(90)
        앞으로(100)
        왼쪽(90)
        앞으로(100)
        왼쪽(90)
        앞으로(100)
        왼쪽(90)
    return

winsound.PlaySound('f.wav', winsound.SND_FILENAME)
number = 0
사각형_함수()
for i in range(50):

    앞으로(100)
    a = random.randint(10, 50)
    b = random.randint(10, 180)
    속도(100)
    왼쪽(b)
    원(a)

    뒤로(100)
    a = random.randint(10, 50)
    b = random.randint(10, 180)
    속도(100)
    왼쪽(10)
    if number == 6:
        number = 0
    else:
        number=number+1
    색(색종류[number])

    원(a)
for i in range(10):
    winsound.PlaySound('omg.wav', winsound.SND_FILENAME)
지우기()
import time
time.sleep(1)
winsound.Beep(600, 10)
