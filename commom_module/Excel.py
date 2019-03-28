import xlrd

def read_excel():
     # 打开文件
     workbook = xlrd.open_workbook(r'D:\text\Secret.xlsx')

     # 获取所有sheet
     #print(workbook.sheet_names()) # [u'sheet1', u'sheet2']

     #获取sheet2
     sheet2_name= workbook.sheet_names()[1]
     #print(sheet2_name)

     # 根据sheet索引或者名称获取sheet内容
     #sheet1 = workbook.sheet_by_index(0)
     sheet2 = workbook.sheet_by_name('Sheet2')
     print(sheet2)

     # sheet的名称，行数，列数
     # print(sheet2.name,sheet2.nrows,sheet2.ncols)

     # rows = sheet2.row_values(1) # 获取第四行内容
     # cols = sheet2.col_values(1) # 获取第三列内容
     # print(rows)
     # print(cols)
     str="A1"
     #获取单元格内容的三种方法
     print(sheet2.cell(1,0).value)
     print(sheet2[str].value)
     # print(sheet2.cell_value(1,0).encode('utf-8')) #设置编码格式
     # print(sheet2.row(0)[1].value)

     # 简单的写入，table.put_cell()

     # 方法有5个参数：rowx, colx, ctype, value, xf_index
     # rowx　　　　     # 要写的行索引
     # colx　　　　     #  要写的列索引
     # ctype　　　　    # 要写的值的类型： 0 empty, 1 string,  2 number,  3 date,  4 boolean,  5 error
     # value　　　　    # 要写入的值的数据
     # xf_index　　     # 扩展的格式化，默认是0



if __name__ == '__main__':
     read_excel()