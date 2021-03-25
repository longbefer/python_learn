# file operator

import time

# open the file stream
# @param "file_name" 文件名
# @param mode 文件读写方式
# @param encoding 编码方式
# @more 其他参数可以使用 help(open)来获取
# @return 返回文件流
fo = open('Python/1_if_else.py', mode='r', encoding = 'utf-8')

# read the file stream
print("file name is: \n" + fo.name)

# read all file 
# @return 返回整个文章的字节流
print(fo.read())

# get the point position 
print('指针当前位置'+str(fo.tell()))

# set the point position
# seek(offset, [whence])
# @param offset 光标位置
# @param whence 默认为0，只能为0，1，2
# @example 使用seek(0,0)表示将光标置于文档开头
#          使用seek(0,2)表示将光标移至文档末尾
fo.seek(0, 0)
end = fo.seek(0, 2) # 移动至文档末尾
print('指针当前位置'+str(fo.tell()))
fo.seek(0,0) # 移动至文档开头

# read a line
print(fo.readline())

auto = input('是否开启自动翻页')
if auto == 'Y':
    while True:
        for i in range(3):
            print(fo.readline())
        time.sleep(2)
        if fo.tell() == end:
            break
else: 
    con = 'n'
    while True:
        if con=='n':
            for i in range(3):
                print(fo.readline())
        else:
            print('请输入n')
        if fo.tell() == end: 
            break
        con = input('请输入下一页')

# close the file stream
fo.close()