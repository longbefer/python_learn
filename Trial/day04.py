str1 = 'hello world'
num_int = 3
num_float = 3.14
bConfirme = False

# 通过type()获取变量的数据类型
print(type(str1))
print(type(num_int))
print(type(num_float))
print(type(bConfirme))
print(type([]))  # list 列表
print(type({}))  # dict 字典
print(type(()))  # tuple 元组

map = {'longbofeng': 172052136, 'lihan': 172052102}
print(map['longbofeng'])

# 判断字典是否含有该key
print('name' in map.keys())

# 去除list1中的大于10的元素
list1 = [10, 11, 12, 20, 9, 29, 8]
list2 = []
for d in list1:
    if d <= 10:
        list2.append(d)
print(list2)

# 删除元素
print(list1)
j = 0
while j < len(list1):
    if list1[j] > 10:
        list1.pop(j)
    else: j += 1
print(list1)

# 判断元素是否在list1中
if 8 in list1:
    print("8在list1中")
else: print("8不在list1中")

import time

# insert和append
list3 = []
start = time.time()
for i in range(0 , 10000):
    # list3.append(i) 
    list3.insert(len(list3), i) 
end = time.time()
print(end - start)