import random

temp = input("输入一个数字: ")
guess = int(temp)
number = 9

if (guess == number):
    print("right")
elif (guess < number):
    print("low")
else: print("high")
print("game over")



print("\n part two")
temp = input("输入一个数字: ")
guess = int(temp)
while guess != number:
    if (guess < number):
        print("low")
    else: print("high")
    # 重新输入
    temp = input("输入一个数字: ")
    guess = int(temp)
print("you're right")
print("end game")

# 与门
print(3<3 and 3>6)
print(6<9 and 4<9)
# 或门
print(3 == 3 or 4 == 4)
# 非门
print(not (3==3))

print("\n part three\n")
secret = random.randint(0, 100)
temp = input("输入一个数字: ")
guess = int(temp)
while guess != secret:
    if (guess < secret):
        print("low")
    else: print("high")
    # 重新输入
    temp = input("输入一个数字: ")
    guess = int(temp)
print("you're right")
print("end game")
