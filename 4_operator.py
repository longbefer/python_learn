# python 2 以前 d/=8 得到的d为int
# python 3 d/=8 得到float

# 为了兼容，使用 // 
# 则， d // 3 得到 int
#     d // 3.0 得到 float

d = 9
print(d // 4) # int
print(d / 4)  # float

# 次幂
d **= 2       # d^2
print(d)
print(d ** 2)