import math
import  re
import random
#石头剪刀布游戏
def shitou():
    guess_list = ["石头", "剪刀", "布"]
    win_combination = [["布", "石头"], ["石头", "剪刀"], ["剪刀", "布"]]

    while True:
        computer = random.choice(guess_list)
        people = input('请输入：石头,剪刀,布\n').strip()
        if people not in guess_list:
            continue
        elif computer == people:
            print ("平手，再玩一次！")
        elif [computer, people] in win_combination:
            print ("电脑获胜，再玩，人获胜才能退出！")
        else:
            print ("人获胜！")
            break
shitou()

# 3.打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
# 其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
def shuixianhua():
    for i in range(100,999):
        a=str(i)
        if math.pow(int(a[0]),3)+math.pow(int(a[1]),3)+math.pow(int(a[2]),3)==int(i):
            print(int(a))

def shuixianhua2():
    for i in range(100, 999):
        a=i%10
        b=int((i%100-a)/10)
        c=int((i%1000-b)/100)
        if math.pow(a,3)+math.pow(b,3)+math.pow(c,3)==i:
            print(i)

# 4.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
def four():
    asd=input();
    chinazhenze = re.compile("[\u4ea0-\u9fa5a-zA-Z].*?")
    kongge = re.compile(" .*?")
    shuzi = re.compile("[0-9].*?")
    qitazifu = re.compile("[`~!@#$^&*()=|{}':;',\\[\\].<>/?~！@#￥……&*（）——|{}【】‘；：”“'。，、？].*?")
    china = chinazhenze.findall(asd)
    konggea = kongge.findall(asd)
    shuzia = shuzi.findall(asd)
    qitazifua = qitazifu.findall(asd)
    print(len(china))
    print(len(konggea))
    print(len(shuzia))
    print(len(qitazifua))
#s输出匹配的字符
    # print(china)
    # print(konggea)
    # print(shuzia)
    # print(qitazifua)
