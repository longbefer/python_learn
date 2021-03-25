import random

# while True:
#     # 次数
#     i = 5
#     # 获取随机数
#     word = random.randint(1, 101)

#     # 若猜错5次，则结束游戏
#     while i > 0:
#         print('left ',i, 'times', end=' ')
#         num = int(input('enter the number: '))
#         i-=1
#         if num < word:
#             print('too small')
#         elif num == word:
#             print('great')
#             break
#         else:
#             print('too big')

#     print('game over， please try again')


# while True:
#     word = random.randint(1, 101)

#     # 猜5次
#     for i in range(5, -1, -1):
#         print('left',i,'times', end=' ')
#         num = int(input('enter the number: '))
#         if num < word:
#             print('too small')
#         elif num == word:
#             print('great')
#             break
#         else: print('too big')

#     print('game over')


# 一个小球从100米的高度落下，每次弹回原来高度的二分之一
# 请计算：
# 总共经过多少次，最终落地
# 总共经过了多少米
# 


# 累加10-50之间个位不是2，5，9的整数
sum = 0
for num in range(10, 51):
    bit = num % 10
    if bit != 2 and bit != 5 and bit != 9:
        sum += num

print('累加结果为：' + str(sum))


# 一张纸的厚度是0.01毫米，请计算对折多少次超过8844.43
i = 0
height = 0.01 * 0.1 * 0.1 * 0.1 # 高度m
while height < 8844.43:
    height *= 2
    print(height)
    i+=1
print(i)