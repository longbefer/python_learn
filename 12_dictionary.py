
# 字典

brand = ['品牌', '关系', '列表', '编程']
slogan = [3, 9, 10, 4]

# 字典由{}括起来
dict1 = {'品牌':3, '关系':9, '列表':10, '编程':4}
print(dict1)
print(dict1['品牌'])

print(type(dict1))
print(type({}))

# print(type({(1, 'one'), (2, 'two'), (3, 'three')})) # set
# print(type(((1, 'one'), (2, 'two'), (3, 'three')))) # tuple

# 输入字典
a1 = dict(((1, 'one'), (2, 'two'), (3, 'three')))
print(a1)
print(a1[1])

a2 = dict(name = 'lsp', sex = 'famale', age = '34')
print(a2)
print(a2['name'])

a3 = dict()
a3['A'] = '甲'
a3['B'] = '乙'
a3['C'] = '丙'
a3['D'] = '丁'
print(a3)
print(a3['A'])

a4 = {}
print(type(a4))
a4['H'] = '氢'
a4['He'] = '氦'
a4['Li'] = '锂'
a4['O'] = '氧'
print(a4)
print(a4['O'])

a5 = {'H':4, 'C':3, 'D':2, 'F': 9}
print(a5)
print(a5['C'])


# fromkey
a6 = {}
print(a6.fromkeys((1, 2, 4))) # fromkey 给前面的索引赋值为后面的内容
print(len(a6))
print(a6.fromkeys((1, 2, 3), 'One')) # 本质上产生一个新的dict，不会改变a6
print(a6)
a6 = dict.fromkeys((1, 2, 3), 'set') # 可以将他赋值即可
print(a6)
a6 = dict.fromkeys(range(32), '赞')  # 使用range生成
print(a6)

# keys() values() items()
for eachKey in a6.keys():
    print(eachKey)
for eachValue in a6.values():
    print(eachValue)
for eachItem in a6.items():
    print(eachItem)

# 若不存在key，则会报错，可以使用 get() 它不会报错
# print(a6[32])
a6.get(32) # 这样程序可以向下执行，而不会报错
print(a6.get(32, "不存在该值")) # 若32不存在该值，则打印后面的“不存在该值”
print(a6.get(31, "不存在该值")) # 若31存在该值，则打印31的值

# 或者使用in查看键keys是否存在
print(32 in a6)
print(31 in a6)

# clear()  清除字典
a6.clear()  

# = 与 copy    = 是赋值地址， copy 是赋值值
a = { 'A': 14, 'B': 9, 'C':10, 'D': 13 }
b = a.copy()   # 深复制（申请了新的内存空间赋给相同值）
c = a          # 浅复制（申请一个指针指向原来的内存空间）
print(id(a))
print(id(b))
print(id(c))  # id()输出地址

# pop 和 popitem()
print('原字典： ',a)
print(a.pop('A'))
print('a.pop("A")后： ' ,a)
print(a.popitem())  # 弹出最后一个
print('a.popitem()后： ' ,a)

# setdefault
a.setdefault("小白") # 若当前不存在小白key则会自动添加，value会变为none
a.setdefault(5, 'five') # 当不存在5：five时自动添加
a.setdefault('B', 10)   # 由于存在B:9故不会更新B:10
print(a)

# update
a.update({'小白':'狗'})  # update 传递 dict 对象
print(a)