#!/usr/bin/env python
#-*- coding: utf-8 -*-

import xlsxwriter

workbook = xlsxwriter.Workbook('test.xlsx') 	# 创建一个excel文件
worksheet = workbook.add_worksheet()		# 创建一个工作表格

worksheet.set_column('A:A',20)			# 设定第一列宽为20个像素
bold = workbook.add_format({'bold': True})	# 定义一个加粗的格式对象

worksheet.write('A1','Hello')			# A1写入'Hello'
worksheet.write('A2','World',bold)		# A2写入world，并加粗
worksheet.write('B2',u'中文测试',bold)		# B2写入中文

worksheet.write(2,0,32)				# 用行列表示法写入数字32与35.5
worksheet.write(3,0,35.5)
worksheet.write(4,0,'=SUM(A3:A4)')		# 求A3:A4的各，并将结果写入'4,0'，即A5

worksheet.insert_image('B5','img/demo.png')	# 在B5单元插入图片
workbook.close()				# 关闭excel
