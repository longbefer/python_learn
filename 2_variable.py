teacher = "xiajiayu"
print(teacher)

name = '老家'
print(name)

first = 9
second = 10
print(first+second)

# 变量名不能以数字开头

# 原始字符串（但是最后一个字符不能是 \ 否则就错误）
temp = r"c:\\now" # r 即 row
print(temp)

# 整形、浮点型、e记法（科学计数法）、布尔值类型
some = True
any = False

print(str(369)) # 将其转化为字符
print(float("-345.90")) # 将其转换为浮点型
print(int(456.99)) # 将其转换为整型
print(bool(5)) # bool 类型 0 为 False 非0为 True

# 若自定义的变量名使用和函数名称相同时，一般会使用变量名
# 如下：
# str = "name"
# print(str)
# temp = str("sex") # 错误，此时str为变量
# print(temp)
# 使用type()可以得到变量的类型
print(type(some))
print(type(any))
print(type(first))
print(type(name))
print(type(5.0))
print(type(5e10))
# python 官方建议使用 instance() 比较是否为相同类型
print(isinstance(any, int)) # any 可以是bool 也可以是 int类型
print(isinstance(any, bool)) # true 
print(isinstance(name, str))
