import xlrd
import pandas  as pd
from datetime import date,datetime

file = '线上系统服务统计v1.2.0-仿真数量20210305-底表.xlsx'

def read_excel():

	wb = xlrd.open_workbook(filename=file)#打开文件

	# print(wb.sheet_names())#获取所有表格名字

	# sheet1 = wb.sheet_by_index(0)#通过索引获取表格

	sheet2 = wb.sheet_by_name('等比环境服务编排')#通过名字获取表格

	# print(sheet1,sheet2)
	#
	# print(sheet2.name,sheet2.nrows,sheet2.ncols)

	rows = sheet2.nrows
	cols = sheet2.ncols
	for c in range(1, cols):
		for r in range(2,rows):

			v = sheet2.cell(r, c).value
			if v == 1:
				app = sheet2.cell(1, c).value
				ip = sheet2.cell(r, 0).value
				print(app,ip)

		# print(r,'------------------')
	# print(sheet2.col_values())
	# rows = sheet2.row_values(2)#获取行内容
	#
	# cols = sheet2.col_values(3)#获取列内容
	#
	# print(rows)
	#
	# print(cols)
	#
	# print(sheet1.cell(1,0).value)#获取表格里的内容，三种方式
	#
	# print(sheet1.cell_value(1,0))
	#
	# print(sheet1.row(1)[0].value)

	# df = pd.read_excel(file,sheet_name='等比环境服务编排')
	# data = df.values()
	# print("获取到所有的值:\n{0}".format(data))  # 格式化输出


read_excel()
