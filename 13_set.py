#  集合

num = {} # 字典
print(type(num)) 


# 集合的值唯一，故使用 
num = {1, 3, 4, 4, 6}  # 该集合和num1一致（去除重复元素）
num1 = {1, 3, 4, 6} # 集合
print(type(num), num)
print(type(num1), num1)
# 集合是无序的不支持索引
# num1[0] 错误，不支持索引

num2 = set()  # 集合
print(type(num2))
# set()可以传入元组、列表等

# 可以使用它去除重复元素（注意会排序）
num3 = [1, 2, 3, 4, 3, 5, 1, 2, 0]  # 去除num3中的重复元素
num4 = list(set(num3))
print(num4)

# add() remove()
num5 = {1, 3, 5, 6, 9, 0}
num5.add(11)
num5.remove(1)
print(num5)

# frozen
num6 = frozenset({ 1, 3, 5, 6, 9}) # 冻结的集合 不可修改
print(num6)


# 在help文档中按住Q退出
help(set)  # 请自行查阅set的函数