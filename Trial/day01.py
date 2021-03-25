# 文件流对象
f = open('Python/1_if_else.py', encoding='utf8')
# 判断是否文件关闭
print(f.closed)
# 判断文件的权限
print(f.mode)
# 判断文件名字
print(f.name)
# 文件关闭
# f.close()

# 文件流对象
for item in f:
    print('xxxxxxxxxxxxxxxxx')
    print(item)
    print('xxxxxxxxxxxxxxxxx')
# f.close()

f.seek(0,0)
while True:
    s = f.readline()
    if not s:
        break
    if s[-1] == '\n':
        print('>>>', s[:-1])
    else:
        print('>>>', s)

f.close()

with open('Python/1_if_else.py', encoding='utf-8') as f:
    print("=================")
    print(f.read())
    print("=================")

# 使用with as 可以不用调用close()

with open('pic1.jpg', 'rb') as jpg1, open('pic2.jpg', 'wb') as jpg2:
    jpg2.write(jpg1.read())