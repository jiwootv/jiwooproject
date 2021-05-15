a = 1
b = 1
def multiplication():
    global a
    global b
    print(b, '*', a, '=', b * a)
    a +=1
for i in range (9):
    for i in range(9):
        multiplication()
    a = 1
    b += 1
