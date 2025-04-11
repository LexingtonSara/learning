"""JSON概述"""
# 在python中，可以将程序中的数据以JSON格式进行保存。JSON(JavaScript Object Notation)是一种轻量级的数据交换格式。
# 它基于ECMAScript的一个子集。JSON是纯文本格式，易于人阅读和编写，同时也易于机器解析和生成。

# 使用方法：
# 1. 将数据转换为JSON格式的字符串,dumps()方法可以将Python对象转换为JSON格式的字符串。
# 2. 将JSON格式的字符串写入文件,dump()方法可以将Python对象写入JSON格式的字符串到文件。
# 3. 从文件中读取JSON格式的字符串，并将其转换为Python对象,loads()方法可以将JSON格式的字符串转换为Python对象。
# 4. 从文件中读取JSON格式的字符串，并将其转换为Python对象,load()方法可以将JSON格式的字符串转换为Python对象。

"""Python读写CSV文件"""
# CSV文件(Comma Separated Values)全称逗号分隔值文件，广泛用于应用程序数据的导入导出以及异构系统之间的数据交换。
# Python中可以使用csv模块来读写CSV文件。

# 读写CSV文件的方法：
# 1. 写文件：Python标准库中有csv模块，该模块的writer()方法会返回一个csvwriter对象，通过writerrow或者writerrows方法将数据写入csv文件中。
# import csv
# import random
# with open("scores.csv", "w", newline='') as f:
#     writer = csv.writer(f,delimiter='|', quoting=csv.QUOTE_ALL)
#     writer.writerow(['姓名', '语文', '数学', '英语'])
#     names = ['关羽', '张飞', '赵云', '马超', '黄忠']
#     for name in names:
#         scores = [name] + [random.randint(80, 100) for _ in range(3)]
#         # scores.insert(0, name)
#         writer.writerow(scores)

# 2. 读取CSV文件,通过csv.reader()方法可以读取CSV文件。创建出csvreader对象，该对象是一个迭代器。
# with open("scores.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


# with open('scores.csv', 'r') as file:
#     reader = csv.reader(file, delimiter='|')
#     for data_list in reader:
#         print(reader.line_num, end='\t')
#         for elem in data_list:
#             print(elem, end='\t')
#         print()

# 3.读写excel文件
# 读写excel文件的方法：
# 1. 安装openpyxl模块：pip install openpyxl
# 2. 读写excel文件：
# 读文件：
# from openpyxl import load_workbook# 加载工作簿
# wb = load_workbook(filename='example.xlsx')# 打开工作簿
# ws = wb.active# 获取当前活动的工作表
# for row in ws.rows:
#     for cell in row:
#         print(cell.value, end='\t')
#     print()
# 写文件：
# import random
# from openpyxl import Workbook


# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# scores = [[random.randint(80, 100) for _ in range(3)] for _ in range(5)]

# wb = Workbook()
# ws = wb.active
# ws.title = '四年级八班成绩表'

# ws.append(['姓名', '语文', '数学', '英语', '总分'])
# for row in range(5):
#     ws.append([names[row]] + scores[row] + [sum(scores[row])])

# ws.append(['平均分']+[sum([scores[i][j] for i in range(5)])/5 for j in range(3)])

# wb.save('考试成绩表.xlsx')

# import datetime
# import openpyxl

# wb = openpyxl.load_workbook('2022年股票数据.xlsx')
# print(wb.sheetnames)

# sheet = wb.worksheets[0]
# print(sheet.dimensions)
# print(sheet.max_row, sheet.max_column)

# print(sheet.cell(row=1, column=1).value)
# print(sheet.cell(row=1, column=2).value)
# print(sheet["A1"].value)
# print(sheet["A2"].value)

# print()

# print(sheet["A2:C5"])

# for row in range(2, sheet.max_row+1):
#     for col in "ABCDEFG":
#         value=sheet[f'{col}{row}'].value
#         if type(value) == datetime.datetime:
#             print(value.strftime("%Y年%m月%d日"), end="\t")
#         elif type(value) == int:
#             print(f'{value:<10d}', end="\t")
#         elif type(value) == float:
#             print(f'{value:<.4f}', end="\t")
#         else:
#             print(value,end="\t")
#     print()

# wb.close()