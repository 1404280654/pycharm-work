
# -*- coding: utf-8 -*-
import csv

# 以字节方式读写文件，也就是在原来操作模式的基础上加上字节模式，即：
# rb，wb，xb，ab,这些不可加encoding,编码格式

#读:list
# with open("D:\\text\CSVTEXTa.csv", "r", encoding = "utf-8") as f:
# #读取csv文件，返回的是迭代类型
#     read = csv.reader(f)
#     column = [row[1] for row in reader] #其中一种循环输出方法
#     for row in read:
#         parameterStr = ','.join(row)  # 通过逗号连接每行每个单元格的内容
#         print(row)
# print(read)
# print('-----------------------------------')
# print(parameterStr)

#读:String
with open('D:\\text\CSVTEXTa.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    column =  [row['name'] for row in reader]
    print(column)
    # for row in csvfile:
    #     print("hang1    "+row)


print('-----------------------------------')


#写
# list=['1','1','1','1','1','1','1','1','1','1','1','1']
# with open("D:\\text\CSVTEXTa.csv", "a", newline="") as f2:
#     # dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
#     csvwriter = csv.writer(f2, dialect=("excel"))
#     # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
#     csvwriter.writerow(list)
