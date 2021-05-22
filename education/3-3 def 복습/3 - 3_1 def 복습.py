def myfuc(a_def, b, type_custum='+', repeat=1):
    result = 0
    for i in range(repeat):
        if type_custum == '+':
            result += a_def + b
        if type_custum == '-':
            result += a_def - b
        if type_custum == '*':
            result += a_def * b
        if type_custum == '/':
            result += a_def / b
    return result


number = myfuc(1, 5, type_custum='*', repeat=1)

print(number)