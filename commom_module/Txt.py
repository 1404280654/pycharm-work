#第一种写法
file_path="D:\Engilsh.txt"
with open(file_path, 'r') as f:
    # line = f.readline()  # 读取一行,之后是循环读取多行
    # while line:
    #     print(line)
    #     line = f.readline()
    #****************************************************************
    a=[]
    lines = f.readlines()  #读取所有行（返回一个列表，一行作为一个元素）
    for i in range(len(lines)):
        a.append(lines[i].rstrip('\n'))   #删除 string 字符串末尾的指定字符（默认为空格）.
    print(a)
    #****************************************************************
    #content = f.read()  # 读取所有行（返回一个字符串，内容为整个文本)


#-----------------------------------------------------
#第二种写法
# file_object = open('D:\Engilsh.txt') #不要把open放在try中，以防止打开失败，那么就不用关闭了
# try:
#     #file_context = file_object.read()              #file_context是一个string，读取完后，就失去了对test.txt的文件引用
#     file_context = file_object.read().splitlines()  #  file_context是一个list，每行文本内容是list中的一个元素
# finally:
#     file_object.close()
# print(file_context)


"""
write(String)方法是写入,在open是W模式下会重写文本，A则是追加，“\n”用来换行
next()方法会在每次循环中调用，该方法返回文件的下一行，如果到达结尾(EOF),则触发 StopIteration
temp1 = line.strip('\n')       #去掉每行最后的换行符'\n'
temp2 = temp1.split(',')     #以','为标志，将每行分割成列表
new.append(temp2)          #将上一步得到的列表添加到new列表中
文件异常（IOError）     try-cath用



list常用操作
join(row)                       # 通过逗号连接每行每个单元格的内容
bicycle.append('xiaodao')       # 末尾添加  list.clear()清空
list.extend(seq)                #在列表末尾一次性追加另一个序列中的多个值
bicycle.index("new")            #搜索是否有new这个值
bicycle.insert(1,'bb')          # 指定位置插入
bicycle.remove("new")           # 删除首次出现的一个值
bicycle_pop = bicycle.pop()     # 删除 list 的最后一个元素, 然后返回删除元素的值。
cars.sort(reverse=True)         #设置排序时是否倒序（永久改变列表）
cars.reverse()                  #列表元素顺序被翻转（再调用一次即可恢复原来顺序）







"""