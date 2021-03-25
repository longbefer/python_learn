import random
# 模块是可用代码的打包


for i in range(0, 10):
    print(random.randint(0, 10))

import os
print(os.getcwd()) # 当前工作目录

os.chdir('/home/longbefer')  # cd命令，切换到指定目录
print(os.getcwd())

os.chdir('/home/longbefer/文档/Progarm/C')
print(os.listdir(os.getcwd())) # 显示目录下的内容（文件夹等）

# os.mkdir("Python") # 创建文件夹
# os.makedirs() # 创建多层目录
# os.rmdir(path) # 删除单层目录，该目录非空则异常
# os.remove() # 删除文件
# os.removedirs() # 递归擅长目录，目录非空（包含文件、子目录下还存在目录）异常
# os.rename(old_name, new_name)  # 重命名
os.system("gnome-terminal") # 打开Ubuntu的终端 （win 改为cmd）

print(os.curdir) # 返回 .  返回当前目录的表示
print(os.pardir) # 返回 .. 返回上级目录的表示
print(os.name) # posix nt mac os2 ce java   posix表示linux
print(os.linesep) # 输出系统的终止符 \r\n 或 \n
print(os.sep) # 输出系统的路径分割符 \\ 或 /

# =================================
# os.path
print(os.path.basename("/home/longbefer/six.avi")) # 获取文件名
# os.path.join('A', "B", "c") # 将各部分组成对应操作系统的文件路径
# os.path.splitext(" ") # 获取文件扩展名（两部分，目录和文件扩展名）
# os.path.split(" ") # 获取文件目录和目录的最终子文件/文件夹（两部分）
# os.path.getsize("") # 对应文件大小
# os.path.getctime(" ") # 文件创建时间 create
# os.path.getatime(" ")  # 文件最近访问时间  access
# os.path.getmtime(" ")  # 文件最近修改时间 modify
# 时间 可以 放入 time.localtime()  可以得到更详细的时间
#              time.gmtime()    # 格林制时间
# os.path.isabs("") # 是否是绝对路径
# os.path.isdir(" ") # 是否为目录
# os.path.isfile(" ") # 是否为文件
# os.path.islink(" ") # 是否为符号链接（快捷方式）
# os.path.ismount(" ") # 是否为挂载点
# os.path.samefile("", "") # 判断两个路径是否指向同一个文件



# ============================================
import pickle
# 将文件保存为二进制
my_list = [123, 3.14, 'file', ['some', 'thing']]
pickle_file = open('my_list.pkl', 'wb') # 将文件保存为my_list.pkl
pickle.dump(my_list, pickle_file) # 将 my_list 的数据写入my_list.pkl中
pickle_file.close()

# 读取pkl文件
pickle_file = open('my_list.pkl', 'rb') # 读取pkl
my_list2 = pickle.load(pickle_file)
print(my_list2)
