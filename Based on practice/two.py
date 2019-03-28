import  re
import random
# 1.输入314.1516,按精确到十位,个位,小数点后3位输出
def onf():
    a=314.85161
    print(round(a,3))
    print(round(a))
    if int(a)%10>=5:
        print(int(a)-int(a)%10+10)
    else:
        print(int(a)-int(a)%10)
# 2.模拟投掷出一对骰子的点数
def two():
    print(random.randint(1,6)+random.randint(1,6))


# 3.假设有一字符串"You're 2B^-^",写出判断其是否是只包含字母的方法
def three():
    parent = re.compile("[^a-zA-Z].*?")
    a="You're 2B^-^"
    m = parent.findall(a)
    if m:
        print("字符串不只含字母还包含了",m)
    else:
        print("只含字母")

# 4.给定一个用;分隔的字符串'zhangsan;lisi;wangwu;zhaoliu',求出其中有多少个用户名
def four():
    customer="zhangsan;lisi;wangwu;zhaoliu"
    a=customer.split(';')
    print(a)
    b=len(a)
    print(b)

# 5.判断'admin;zhangsan;administrator;root;lisi'字符串中是否包含'admin'用户
def five():
    customer="admin;zhangsan;administrator;root;lisi"
    a = customer.split(';')
    b=len(a)
    if b >2:
        print("不只包含'admin'用户")

# 6.列出字符串能够做的操作有哪些
# 7.已知list,info=["zhangsan",["lisi",18],"wangwu",["zhaoliu",18,"shenzhen"]]
#   输出zhaoliu的地址
#   插入lisi的地址"beijing"
def seven():
    info = ["zhangsan", ["lisi", 18], "wangwu", ["zhaoliu", 18, "shenzhen"]]
    for i in info:
        for a in i:
            if a=="zhaoliu":
                print(i[2])
    for i in info:
        for a in i:
            if a=="lisi":
                i.insert(2,"beijing")
    print(info)

# 8.['zhangsan','lisi','zhangsan','wangwu','zhaoliu'],删除列表中的第二个'zhangsan'
def eight():
    a=['zhangsan','lisi','zhangsan','wangwu','zhaoliu',"sdfsdfsdfs"]
    a[2:4]=[]
    print(a)

# 9.列出列表能进行的操作
# 10.输出字典水果中的最大价格 fruits={"apple":10,"pear":5,"banana":12,"grape":8}
def ten():
    fruits = {"apple": 10, "pear": 5, "banana": 12, "grape": 8}
    a=sorted(fruits, key=lambda s: s[2])
    print(a)
   # a.values("banana")

# 11.将字符串"123;abcd;ggg;456"按分隔符;转换成list
def eleven():
    a="123;abcd;ggg;456"
    asd=list(a.split(";"))
    print(asd)

eight()
