# 字符串python 2和 python 3 有所不同 

# 字符串也是不可修改的
# 同元组，只能新建了一个修改
str1 = "i love you"
print(str1)
str1 = str1[:1] + " not" + str1[1:]
print(str1)

# 首字母大写
str1.capitalize() 
# 小写以及很多没用的小秘密函数
str1.center(10)
str1.casefold()
str1.endswith('si')    # 已 si 结束
str1.expandtabs()      # 空格加Tab
str1.find('s')
str1.index('l')        # 同find，但是找不到就自爆了
str1.replace('l', 'k')
str1.split(' ')        # 去除所有空格
# 自行查询吧。。。


# 字符的格式化
print("{0} is {1} and {2} is also".format("i", "pig", "me"))
print("{a} is {b} and {c} is also".format(a="i", b="pig", c="me"))
print("{0:.1f}{1}".format(27.094, "GB"))
# 0后面的：属于格式化工具，.1f表示保留1位小鼠

# %c 格式化字符及其ASCII码
print('%c' % 97)
print('%c, %c, %c' % (97, 98, 99)) # 注意要使用元组
# %s 格式化字符串
print("%s" % "i is pig")
# %o 8进制

# %x 16进制 %X

# %f 定点数，指定精度

# %e 科学计数法 %E

# %g 根据值的大小决定使用 %f 或 %e    %G


# 格式化辅助命令
# 见视频吧。。。
# https://www.bilibili.com/video/BV1xs411Q799?p=16