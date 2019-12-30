#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import wx
from GUI.jump_frame import MyApp
import random
import time

class my1_frame(wx.Frame):
    """We simple derive a new class of Frame"""
    def __init__(self,parent, title,number):
        wx.Frame.__init__(self, parent, title=title,size=(600,400),style=wx.CAPTION|wx.CLOSE_BOX)
        #创建多行输入框
        #self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE,)
        self.number=number
        self.CreateStatusBar()  # 创建窗口底部的状态栏
        self.Show(True)


    def add_element(self):

        #菜单条
        filemenu = wx.Menu()
        self.menu_exit = filemenu.Append(wx.ID_EXIT, "Exit", "Termanate the program")
        filemenu.AppendSeparator()
        self.menu_about = filemenu.Append(wx.ID_ABOUT, "About", "Information about this program")  # 设置菜单的内容
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, u"设置")
        self.SetMenuBar(menuBar)  # 创建菜单条

        # 图片
        to_bmp_image = wx.Image('picture\\background.jpg', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0))


        #按钮
        #bmp_like = wx.Image("picture\\like_button.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.button_like = wx.Button(self.bitmap, -1, label='喜欢', pos=(100, 220), size=(70, 40))
        self.button_unlike = wx.Button(self.bitmap, -1, label='不喜欢', pos=(440, 220), size=(70, 40))




    def Application(self):
        # 把出现的事件，同需要处理的函数连接起来
        self.Bind(wx.EVT_MENU, self.on_about, self.menu_about)
        self.Bind(wx.EVT_MENU, self.on_exit, self.menu_exit)
        self.Bind(wx.EVT_BUTTON, self.on_like, self.button_like)
        self.Bind(wx.EVT_BUTTON, self.on_unlike, self.button_unlike)
        self.Bind(wx.EVT_CLOSE, self.forwarning)



    """--------------------------------------------------------------------------------------"""
    def forwarning(self,e):
        if(self.number==1):
            dlg=wx.MessageDialog(self, u"还没回答好，就想关闭，太可恶了，我现在很生气，问题很严重", u"问题很严重",
                        wx.OK | wx.ICON_HAND | wx.STAY_ON_TOP | wx.ICON_EXCLAMATION)  # 创建一个对话框，有一个ok的按钮
            dlg.ShowModal()
            app = MyApp(self)
            app.MainLoop()


    #喜欢的情况
    def on_like(self,e):
        dl = wx.MessageDialog(self, "你的眼光非常不错，很有前途，这个选择非常正确", "摸摸哒", wx.OK)  # 创建一个对话框，有一个ok的按钮
        dl.ShowModal()  # 显示对话框

        print("亲爱的美味皮得很：")

        print("漫无目的的刷记录着别人色彩斑斓生活的抖音，而自己却感觉生活在迷雾中，朦朦胧胧，浑浑噩噩的")

        print("而你的出现檫亮了我的整个世界，我开始懂得什么叫做牵挂，什么叫做思念，什么叫做喜欢！")

        print("当我第一眼看到你的时候就知道你是我今生的唯一，你的眼 你的眉 你的眼角太完美，我今生将会一生一世等你，直到永远永远！！")

        print("未来的计划都是你：")

        print("我最想要的生活，就是每天早上起来，能看到你和阳光都在，能给你做早餐;")
        print("我最想要的工作，就是能按时回家看见你，能给你买让你开心的东西;")
        print("我最想要的家庭，就是不用很大，但却有我们两个喜欢的样子，能一起窝在沙发上看电视;")
        print("我想要的有很多，但最想跟你一起经历，我最想要一起的人，只有你!")

        print("相寻梦里路，飞雨落花中。")

        print("思念你的时生")

        print("2019年12月30日")

        time.sleep(1)
        self.Destroy()


    #弹出Message
    def on_unlike(self,e):
            dlg = wx.MessageDialog(self, u"你负责貌美如花，我负责赚钱养家！", u"不要不喜欢我", wx.OK|wx.STAY_ON_TOP)  # 创建一个对话框，有一个ok的按钮
            dlg.ShowModal()   # 显示对话框
            dlg5 = wx.MessageDialog(self, u"家务活我干！", u"不要不喜欢我", wx.OK | wx.STAY_ON_TOP)  # 创建一个对话框，有一个ok的按钮
            dlg5.ShowModal()  # 显示对话框
            dlg2 = wx.MessageDialog(self, u"钱包你管！", u"不要不喜欢我", wx.OK | wx.STAY_ON_TOP)  # 创建一个对话框，有一个ok的按钮
            dlg2.ShowModal()  # 显示对话框
            dlg3 = wx.MessageDialog(self, u"菜我做！", u"不要不喜欢我", wx.OK | wx.STAY_ON_TOP)  # 创建一个对话框，有一个ok的按钮
            dlg3.ShowModal()  # 显示对话框
            dlg4 = wx.MessageDialog(self, u"保大！", u"不要不喜欢我", wx.OK | wx.STAY_ON_TOP)  # 创建一个对话框，有一个ok的按钮
            dlg4.ShowModal()  # 显示对话框
            dlg6 = wx.MessageDialog(self, u"所以应该不会不喜欢我了吧，再选择一次吧，你肯定不会选择不喜欢，赌十包辣条", u"再次选择吧", wx.OK | wx.STAY_ON_TOP)  # 创建一个对话框，有一个ok的按钮
            dlg6.ShowModal()  # 显示对话框
            self.button_unlike.Destroy()
            self.button_nochoice = wx.Button(self.bitmap, -1, label='不喜欢', pos=(440, 220), size=(70, 40))
            self.button_nochoice.Bind(wx.EVT_MOUSE_EVENTS, self.on_nochoice)


    def on_nochoice(self,e):
        pos = (random.randint(1, 530), random.randint(1, 300))
        self.button_nochoice.SetPosition(pos)

    #关于没什么用
    def on_about(self,e):#about按钮的处理函数
        dlg = wx.MessageDialog(self,"希望美味皮得很玩得开心，", "About sample Anything", wx.OK)#创建一个对话框，有一个ok的按钮
        dlg.ShowModal()#显示对话框


    #关闭
    def on_exit(self,e):
        dlg = wx.MessageDialog(self, "以为设置这里真的能关闭吗，太天真了，你皮的很，所以我也要皮一点才行！", "About sample Exit",
                               wx.OK)  # 创建一个对话框，有一个ok的按钮
        dlg.ShowModal()  # 显示对话框
        self.Close(True)

    def test_baidu_01(self):
        dr=self.dr
        dr.get(self.base_url)
        dr.find_element_by_id('kw').send_keys('unittest')
        time.sleep(2)
        dr.find_element_by_id('su').click()
        time.sleep(3)
        self.assertIn('unittest',dr.title)
        print("sdfsd")

    def test_baidu_02(self):
        dr=self.dr
        dr.get(self.base_url)
        dr.find_element_by_id('kw').send_keys('123')
        dr.find_element_by_id('su').click()
        time.sleep(3)
        # 断言
        self.assertIn('123',dr.title)

if __name__=="__main__":
    app = wx.App(False)
    frame = my1_frame(None, '美味皮得很收',1)
    my1_frame.add_element(frame)
    my1_frame.Application(frame)
    app.MainLoop()