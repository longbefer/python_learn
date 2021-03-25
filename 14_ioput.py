# 文件读写
# r - 以只读方式打开文件（默认）
# w - 以写的方式打开文件，会覆盖已存在的文件
# x - 如果文件已存在，则报错
# a - 以写入模式打开，如果文件存在，则在末尾追加 append
# rb - 以二进制打开 binary
# t - 以文本模式打开 text
# + - 可读写模式
# U - 通用换行符支持

text = open("record.txt", 'r')
print(text)


print(text.readline()) # 读取一行
# print(text.readlines()) # 读取整个文本
# print(text.read())  # 读到文件尾
print(text.read(100)) # 读取100个字符
print(text.tell())   # 当前所在行位置
print(text.seek(101, 0))  # 移动文件指针到所在位置（100字节），第二个参赛 0 表示文件起始位置， 1 表示当前位置， 2 表示文件末尾
print(text.readline()) # 注意上面的seek(101) 因为为UTF-8编码，故需要一个比较确切的字节地址


text.seek(0, 0) # 回到文件头
# 每次读取一行并往下读取
for each_line in text:
    print(each_line)

# 写入文件
# 这里不测试
# text.write("Write some things")

text.close()