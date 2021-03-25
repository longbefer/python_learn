# 函数形式
def ds(x):
    return 2*x + 1
print(ds(5))

# lambda形式
# lambda x : 2 * x + 1
g = lambda x : 2 * x + 1
print(g(5))
g = lambda x,y : x + y
print(g(5, 9))

# lambda代码简洁，可读性强

# lambda使用的例子 -- filter
print(list(filter(None, [1, 0, True, False, 9, 0, 1])))
# filter(None, [])  -- 为None时过滤掉非True的值
f = lambda x : x % 2 == 0   # 判断是否为偶数 (直接 x % 2 就行)
print(list(filter(f, [3, 6, 9, 8, 12]))) # 调用过滤器

# map  -- 映射 迭代器内容通过前面的函数映射成为一个新的函数
f = lambda x, y : x + y
print(list(map(f, [1, 2, 4, 5], [3, 4, 5, 11])))  # 两个list相加（取最短的）
f = lambda x : x ** 2     # x的2次幂
print(list(map(f, [3, 6, 9, 12, 13])))
