number_st = input('숫자 내놔')
number2 = 1
list = []
len_1 = len(number_st)


for i in range(len_1):
    a = number_st[number2 - 1: number2]
    a = int(a)
    list.append(a)
    number2 += 1
number3 = 1
string = ''
for i in range(len_1):
    string = ''
    for j in range(list[i]):
        string = string + '♥'
    print(string)


number_st = input('숫자 내놔')
for i in number_st:
    for j in range(int(i)):
        print('♥', end='')
    print()