v1 = 0


def v():
    global v1
    v1 = v1 + 1
    print(v1)


v()  # 1
dict1 = {'name': '김근육', 'age': 22, 'gander': True}
for key in dict1.keys():
    print(key, ':', dict1[key])
v()  # 2
for values in dict1.values():
    print(values)
v()  # 3
print(dict1)
dict1.update({'weight': 67.8, 'height': 189.7})
dict1['hooby'] = ['술', '춤', '잠', '게임', '등산']
v()  # 4
del dict1['weight']
print(dict1)
v()  # 5
print(dict1.items())
for data in dict1.items():
    print(data[0], ':', data[1])
tuple1 = 1, 2, 3, 4
print(tuple1, type(tuple))
#  요소값 변경
setType1 = {1, 2, 3, 4}
setType2 = {3, 4, 5, 6}

unionset = setType1.union(setType1)
interset = setType1.intersection(setType2)
difference = setType1.difference(setType2)
difference2 = setType2.difference(setType1)
print(unionset, '\n', interset, '\n',
      difference, '\n', difference2)

print(setType1 - setType2)
print(setType1 & setType2)
print(setType1 | setType2)
