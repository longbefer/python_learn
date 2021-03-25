# 元组
# 元组一旦创建不可修改
tuple1 = (1, 2, 4)    # 元组
tuple2 = ()           # 空元组
tuple3 = 3, 4, 6, 7   # 元组
tuple4 = (4)          # 不是元组，可以使用type查看到为int
tuple5 = 8,           # 元组

# 访问元组
tuple1[1]
tuple1[1:]

# 元组的拷贝
tuple2 = tuple1[:]

# 元组不可修改，下面的代码的解释为
# 将temp前1个值加上中间插入的值
# 加上后面的所有值构成一个新元组
# 并覆盖掉先前的temp元组，此时，
# 前一个元组已经没有标签指向他，
# 稍后 python 将自动回收他
temp = ("我", "是", "猪")
print(temp)
temp = temp[:1] + ("不",) + temp[1:]  # 不可忽略，
print(temp)

del temp  # 可以删除整个元组

tuple5 *= 5 # 元组可以将其复制几份（这个的修改同上？？？）
print(tuple5)
print(tuple5 * 3)