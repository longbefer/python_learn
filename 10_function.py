# 函数

# python创建函数可以使用 def    

def MyFirstFunction():
    print("This is my first function.")
    print("I feel exciting.")

MyFirstFunction()
# 函数向上寻找是否存在函数


# function
def add(lhs, rhs):
    print(lhs + rhs)
add(1, 3)
# add(3, 'a')
add('c', 'a')

# return
def sub(lhs, rhs):
    return (lhs - rhs)
print(sub(3, 5))

# 函数区分形参和实参


# 函数文档
def muilt(lhs, rhs):
    '需要传输lhs-数字， rhs-数字， 将返回 lhs*rhs'
    return lhs * rhs
print(muilt.__doc__) # 显示函数文档
# help(muilt)

# 关键字参数
print(muilt(rhs=5, lhs=4))  # 给定参数名

# 默认参数
def printWord(name = '你', word = '好吧!'):
    print(name + ':' + word)
printWord()
printWord('我')

# 收集参数（可变参数）
def test(*params):
    print('参数长度: ', len(params))
    print('第二个参数是： ', params[1])
test(4, 8, 9, '我是谁', 5, 3)

def test2(*params, exp):  # 若指定了收集参数，且外加了一个参数，则必须使用关键字参数
    print(params[0], exp, " ", len(params))
test2(4, 9, 9, 3, 5, 1, 0, 9, exp = 3)
# print() 同理也使用了收集参数

# 可以使用元组或列表返回多个值
# return 4, 8, 'hello'  # 返回元组
# return [4, 8, 'hello'] # 返回列表

# 有局部变量和全局变量区分 
# 在函数内修改全局变量的值，是新建一个局部变量
# 即，
def setValue():
    c = 9   # 此时的c和全局变量中的c不是同一个c
    print("this value: ", c)
c = 30
setValue()
print("this value: ", c)
# 若需要修改全局变量的值
# 可使用global修饰
def setValue2():
    global c  # 加入global即可使用全局变量中的c
    c = 9
    print("this value2: ", c)
setValue2()
print("this value2", c)  

# 内嵌函数
def fun1():
    print("fun1()正在被调用")
    def fun2():    # 内部函数被认为是闭包
        print("fun2()正在被调用")
    fun2()  # 通过fun1调用fun2，外部无法访问，故只能这样
fun1()

# Lisp-----一个编程语言的样子（可以了解下）

# 闭包
def funX(x):
    def funY(y):
        return x * y
    return funY
i = funX(8) # 此时的i是函数
print(i)
print(type(i))
print(i(9)) # 再次调用即可获得最终值
print(funX(9)(8))  # 这个同理阿，这个可以按函数指针来说明（返回函数，按函数指针来调用内部函数）

# 闭包内部调用内部变量
# def funX1():
#     x = 9
#     def funY1():
#         x *= x
#         return x
#     return funY1()
# 为什么这个函数是错误的？因为funY1()不知道x，故不能将其 x*=x
# 在python3之前没有啥解决方法只有利用容器来解决，即
def funX2():
    x = [8]
    def funY2():
        x[0] *= x[0]
        return x[0]
    return funY2()
print(funX2())
# python3后可以使用nonlocal
def funX3():
    x = 8
    def funY3():
        nonlocal x
        x *= x
        return x
    return funY3()
print(funX3())


# 递归
def set(x):
    if x <= 1:
        return 1
    return x * set(x - 1)
print(set(90)) 
# 可以设置递归的深度
# import sys
# sys.setrecursionlimit(50) # 默认为1000的样子
# print(set(90)) # 此时就运行不下去了

def factorial(x):
    '非递归阶乘，x必须为int类型'
    sum = x
    if type(x) is int:
        for c in range(1, x):
            sum *= c
    else: 
        print(x, "is not the number")
        return
    return sum
print(factorial(4))


# 斐波纳切数列
def solve(x):
    '递归解决斐波纳切数列，非记录'
    if x <= 2: return 1
    return solve(x - 1) + solve(x - 2)
def solve1(x, arr):
    '递归解决斐波纳切数列，记录'
    if x < 2 :
        return x
    arr[x] = solve1(x - 1, arr) + arr[x - 2]
    return arr[x]
    
# 调用第一个solve
print(solve(8))
# 调用第二个solve1
num = 100
arr = [1 for i in range(0, num)]
print(solve1(num - 1, arr))

# print(list(i for i in range(0, 9)))


# 汉罗塔游戏 
def hanoi(n, x, y, z): # n 为盘子个数，x，y，z为柱子
    if (n == 1):
        print(x, '-->', z)
    else:
        hanoi(n - 1, x, z, y)   # 将前n-1个盘子从x移动到y上
        print(x, '-->', z)      # 将最低下的最后一个盘子从x移动到z上
        hanoi(n - 1, y, x, z)   # 将y上的n-1个盘子移动到z上
hanoi(3, 'X', 'Y', 'Z')
