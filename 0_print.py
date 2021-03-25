print("Hello world")

teacher = 13
print(teacher)

teacher = "Hello"
print(teacher)

# print "hello world" 在python2是兼容的，但是python3已经不兼容了
# printf("hello world")属于C语言的语法，不可以
# python数值不会产生溢出
print("water"+" some") # 连接字符串
print("water\n" * 8) # 将字符串打印8次

# 不可以输出 water+8 这种东西
# print("water\n" + 8)
# can only concatenate str (not "int") to str

print("\"i'm you father.\" someone repied.\n")

# 格式化输出
print("%d 数字是 %s, 并且 %s 是 %d" %(20, '二十', '貳拾' , 20.0))
# %s - string
# %d - int
# %f - float
