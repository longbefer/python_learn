# 操纵excel
# 需要引入库文件 xlsxwriter
# 这里使用豆瓣镜像：
# pip install xlsxwriter -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
# pep8 为python的编码风格

import xlsxwriter
import random

# 创建一个excel工作簿
workbook = xlsxwriter.Workbook(filename='myexcel.xlsx')

# 创建一个工作表，名称为数据报表
worksheet = workbook.add_worksheet(name="数据报表")

# 给“数据报表”工作表6行A列添加文字信息
# worksheet.write('A1', '2020年收入表')
# 给“数据报表”工作表的数据合并居中
worksheet.merge_range('A1:C1', '2020年收入表')

# 给工作表添加一行数据
heading = ['月份', '收入', '支出']
worksheet.write_row('A2', heading)

# 给工作表添加一列数据
month = [str(i)+'月' for i in range(1, 12 + 1)]
incomes = [random.randint(10 * i, 10000) for i in range(1, 12 + 1)]
outcomes = [random.randint(10 * i, 1000) for i in range(1, 12 + 1)]
worksheet.write_column('A3', month)
worksheet.write_column('B3', incomes)
worksheet.write_column('C3', outcomes)

# 设置下行高
worksheet.set_row(0, 30)
# 设置下列宽，将B，C两列设置为14
worksheet.set_column('B:C', 14)

# 写入文字
worksheet.write_string('A15', '小计')
# 写入公式
worksheet.write_formula('B15', '=SUM(B3:B14)')
worksheet.write_formula('C15', '=SUM(C3:C14)')
# 写入数字
# worksheet.write_number()
# 写入批注
worksheet.write_comment('A1', 'This is comment')

# 设置单元格格式
border_fmt = workbook.add_format({
    'border': 1,  # 设置单元格四个方向上的边框
    'bold': True,  # 设置字体为粗体
    'bg_color': '#1A1A1A',  # 设置背景颜色
    'align': 'center',  # 水平居中对齐
    'font': '微软雅黑',  # 设置字体样式
    'font_size': 22,  # 设置字体大小
    'font_color': 'red'  # 设置字体颜色
})
worksheet.write_string('A20', '边框样式设置', border_fmt)

# 关闭excel表格，并保存文件
workbook.close()


# 使用with as亦可
# with xlsxwriter.Workbook(filename='mybook.xlsx') as book:
#     book.add_worksheet(name='数据报表')
