# if else 

a = input("第一个数字为： ")
b = input("第二个数字为： ")

print("最小的数字为", min(a, b))
print("最大的数字为", max(a, b))

c = input("第三个数字为： ")
print("最大的数字为", max(a, b, c))
print("最小的数字为", min(a, b, c))


num1 = int(input('请输入数字1： '))
num2 = int(input('请输入数字2： '))
operate = input('输入操作符： ')

if operate == '+':
    print(num1 + num2)
elif operate == '-':
    print(num1 - num2)
elif operate == '*':
    print(num2 * num1)
elif operate == '/':
    if num2 != 0:
        print(num1/num2)
    else: print('除数不为0')
else: print('非法操作符')


input('输入月份： ')