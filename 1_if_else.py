import random

temp = input("不妨猜测下一个数字: ")
guess = int(temp) # 如果temp非数字，则会报错

if guess == 8:
    print("right")
else:
    print("error")
print("game over")

# bif 
# build-in function 内置函数

# 打印python的内置函数
dir(__builtins__)
# 显示函数信息（作用）
help(input)
