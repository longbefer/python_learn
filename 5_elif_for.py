for std in range(0,10):
    print("i love you " + str(std))


for i in range(0, 5):
    temp = input("输入成绩"+str(i)+" :")
    grade = int(temp)

    rank = grade // 10
    if rank == 9 or rank == 10:
        print("A")
    elif rank == 8:
        print("B")
    elif rank == 7:
        print("C")
    elif rank <= 6:
        print("D")

# python的三目运算符 a if condiction else b
x,y = 4,5
small = x if x < y else y 

# 断言，当执行错误时，自爆（抛出异常）
# assert 3>4
assert 3 < 4  # 没有错误就忽略

favorite = "Some one has someone's stupid dream\n"
for c in favorite:
    print(c, end="")
print('\n')

# 列表
arr_name = [3, 4, 5, 6, 9]
for i in arr_name:
    print(i)

arr_sex = ["男生", 4, 6, "女生"]
for c in arr_sex:
    print(c)

for i in range(1, 10, 2): # 2为步进
    print(i)

for i in range(10):
    if i % 2 != 0:
        print(i)
        continue
    i += 2   # 尽管这里改变了i的值，但下次执行不受其影响
    print(i)

