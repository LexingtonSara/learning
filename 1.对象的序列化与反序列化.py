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


# from docx import Document
# from docx.shared import Pt,Cm

# document = Document()#创建代表word文档的对象

# document.add_heading("快快乐乐学Python", 0)#添加标题

# p = document.add_paragraph("Python是一门非常优秀的语言，学习它可以提高工作效率，提升编程能力。")#添加段落
# p.add_run("它")
# run=p.add_run("简单")#添加运行对象
# run.bold=True#设置粗体
# run.font.size = Pt(18)#设置字体大小
# p.add_run("而且")
# run=p.add_run("优雅")
# run.underline=True#设置下划线
# run.font.size = Pt(18)
# p.add_run("。")

# document.add_heading("Heding, level 1", level=1)#添加一级标题
# document.add_paragraph("Intense quote", style="Intense Quote")#添加强调的段落
# document.add_paragraph("first item in unordered list", style="List Bullet")#添加无序列表
# document.add_paragraph("second item in ordered list", style="List Bullet")#添加无序列表
# document.add_paragraph("first item in ordered list", style="List Number")#添加有序列表
# document.add_paragraph("second item in ordered list", style="List Number")#添加有序列表
# # document.add_picture("python.png", width=Cm(15))#添加图片,width为图片宽度,需要图片路径

# document.add_section()#添加分节符

# records=(('张三', 25, 180), ('李四', 23, 160), ('王五', 22, 170))
# table = document.add_table(rows=1, cols=3)#添加表格
# table.style = 'Dark List'#设置表格样式
# hdr_cells = table.rows[0].cells#获取表格的第一行的单元格
# hdr_cells[0].text = "姓名"
# hdr_cells[1].text = "年龄"
# hdr_cells[2].text = "身高"

# for name,age,height in records:#为表格添加行
#     row_cells = table.add_row().cells
#     row_cells[0].text = name
#     row_cells[1].text = str(age)
#     row_cells[2].text = str(height)

# document.add_page_break()#添加分页符

# document.save("test.docx")#保存文档

# doc = Document("离职证明.docx")
# for no,para in enumerate(doc.paragraphs):
#     print(no,para.text)


# employees = [
#     {
#         'name': '骆昊',
#         'id': '100200198011280001',
#         'sdate': '2008年3月1日',
#         'edate': '2012年2月29日',
#         'department': '产品研发',
#         'position': '架构师',
#         'company': '成都华为技术有限公司'
#     },
#     {
#         'name': '王大锤',
#         'id': '510210199012125566',
#         'sdate': '2019年1月1日',
#         'edate': '2021年4月30日',
#         'department': '产品研发',
#         'position': 'Python开发工程师',
#         'company': '成都谷道科技有限公司'
#     },
#     {
#         'name': '李元芳',
#         'id': '2102101995103221599',
#         'sdate': '2020年5月10日',
#         'edate': '2021年3月5日',
#         'department': '产品研发',
#         'position': 'Java开发工程师',
#         'company': '同城企业管理集团有限公司'
#     },
# ]
# for employee in employees:
#     doc=Document("离职证明.docx")
#     for para in doc.paragraphs:
#         if "{" not in para.text:
#             continue
#         for run in para.runs:
#             if "{" not in run.text:
#                 continue
            
#             start=run.text.find("{")
#             end=run.text.find("}")
#             key,placeholder=run.text[start+1:end],run.text[start:end+1]
#             run.text=run.text.replace(placeholder,employee[key])

#     doc.save(f"{employee['name']}离职证明.docx")


"""
正则表达式
"""
# import re
# username=input("请输入用户名：")
# qq=input("请输入QQ号：")
# m1=re.match(r"^[a-zA-Z0-9_]{6,20}$",username)
# if not m1:
#     print("用户名格式不正确,请输入6-20位字母、数字、下划线")
# m2=re.fullmatch(r"^[1-9]\d{4,11}$",qq)
# if not m2:
#     print("QQ号格式不正确,请输入11位数字")
# if m1 and m2:
#     print("用户名和QQ号格式正确")

import re
pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也不是110或119，王大锤的手机号才是15600998765。'''

result = pattern.findall(sentence)
for r in result:
    print(r)
print("-----------华丽的分割线-----------")
result = pattern.finditer(sentence)
for r in result:
    print(r.group())
print("-----------华丽的分割线-----------")
m=pattern.search(sentence)
while m:
    print(m.group())
    m=pattern.search(sentence,m.end())