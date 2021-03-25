# 一个任务


# 分割语句
# 分别保存


def save_file(A, B, count):
    file_name_A = "A_spoken_" + str(count) + ".txt"
    file_name_B = "B_spoken_" + str(count) + ".txt"

    file_A = open(file_name_A, 'w')
    file_B = open(file_name_B, 'w')

    file_A.writelines(A)
    file_B.writelines(B)

    file_A.close()
    file_B.close()

def split_file(file_name):
    A = []
    B = []
    count = 0
    text = open(file_name)
    for each_line in text:
        if (each_line[:6] != "======"):
            (role, line_spoken) = each_line.split(": ", 1)
            if role == "A":
                A.append(line_spoken)
            elif role == "B":
                B.append(line_spoken)
            else: print("The error file.")
            # if (each_line[:1] == "A"):
            #     A.append(each_line[3:]) # 从3个字符开始往后
            # elif each_line[:1] == "B":
            #     B.append(each_line[3:]) 
        else:
            save_file(A, B, count)
            count += 1
            A.clear()
            B.clear()
    save_file(A, B, count)
    text.close()

split_file("Python\\resource\\record.txt")