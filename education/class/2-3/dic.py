변수 = 0
def v():
    global 변수
    변수 = 변수 + 1
    print(변수)


v() # 1
dict1 = {'name': '김근육', 'age': 22, 'gander': True}
for key in dict1.keys():
    print(key, ':', dict1[key])
v() # 2
for values in dict1.values():
    print(values)
v() # 3
print(dict1)
dict1.update({'weight': 67.8, 'height': 189.7})
dict1['hooby'] = ['술', '춤', '잠', '게임', '등산']
v() # 4
del dict1['weight']
print(dict1)
v() # 5
print(dict1.items())
for data in dict1.items():
    print(data[0], ':', data[1])
