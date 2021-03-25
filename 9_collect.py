


# 列表、元组、数组

# list(iterable) -> new list initializer from iterable's item
# str()

a = list()
print(a)

b = 'I love you'
b = list(b)
print(b)

c = (1, 1, 2, 3, 5, 8, 13, 21, 34)
c = list(c)
print(c)

print(len(a))
print(len(b))
print(len(c))

# 必须保证所有元素均相同，为空时报错
# max(a)
print(max(b))
print(max(c))

# min(a)
print(min(b)) # 空格小！
print(min(c))

# sum(iterable[, start = 0])
print(sum(c))
# sum 无法对字符串进行相加

# sored排序 和 c.sort()一致
sorted(c)
print(c)

# reversed 返回器迭代，可以使用list(reversed(c)) 查看，其将元素倒置
print(list(reversed(c)))
# reversed无法改变原数据的值
print(c)

# enumerate 返回迭代器，枚举，即返回它的数据和它的位置
enumerate(c)
print(list(enumerate(c)))
# enumerate不改变元素的值
print(c)

# zip 打包，成双成对
d = [1, 2, 4, 5, 7, 9, 0]
e = [4, 9, 9, 0, 8]
f = ['a', 'b', 'c', 'e', 'f']
print(list(zip(d, f)))