
# python 的列表可以存放不同类型
arr_name = ["aa", "bb", "cc", 23, 45.0, 46.9, True, [3, 5, 9], [], ["string"]]

# 向列表添加元素
arr_name.append(arr_name)
arr_name.append('小朋友')
arr_name.append(["someday", "someone"]) # 这是作为列表加入

# 同时加入多个
arr_name.extend(["大朋友", 34])          # 这是向列表加入两个元素

# 在位置中插入元素
arr_name.insert(0, "c++")

# 从位置删除元素
arr_name.remove("aa")   # 若参数中不存在aa则会报错
del arr_name[0]         # 删除列表中的第一个元素
print(arr_name.pop())   # 删除最后一个元素，并可以返回这个元素
print(arr_name.pop(2))  # 删除列表中第三个元素

# 取得位置中的元素
print(arr_name[0])
print(arr_name[1])
print(arr_name[1:3])           # 输出列表位置2到3的元素（即不包含位置为4的元素）
print(arr_name[1:])            # 从列表位置2到最后
print(arr_name[:3])            # 从列表第一个到第三个
# print(arr_name[5][2])          # 列表中的列表（不建议？）

print("\n\n 分割线")
for i in arr_name:
    print(i)

# 列表的比较
list1 = [123, 345]
list2 = [123, 456]
print(list1 < list2)  # 没错，比较列表内对应元素的大小

# 对应类型不匹配时无法通过
list3 = ['world', 123]
list4 = [123, 'world']
# print(list3 < list4)

# 列表长度 len()
print(len(list1))

# 判断元素是否在列表中
print(123 in list3)
print('world' in list3)
print('i' in list3)
print('i' not in list3)

# 元素出现的次数
list3.count("world")   # world字符出现的次数

# 元素的位置
list3.index("world")   # world字符的位置
list3.index("world", 0, 2) # 从0到2world出现的次数

# 排序
list3.sort()             # 归并排序
list3.sort(reverse=True) # 从大到小排序（确认反转） 
# list3.sort(func, key)  # 自定义排序算法

# 反转
list3.reverse()

list4 *= 4  # 将列表复制4份给自己（不会累加）
print(list4)
list4 += list3 # 列表的相加
print(list4)

# +号两边的对象要一致
# 列表的拷贝和引用
list5 = list4     # 引用，改变list5或list4均会改变列表
list6 = list4[:]  # 拷贝，list6或lilst4改变不会改变对方的值

