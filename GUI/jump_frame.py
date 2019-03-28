import wx
import time
from random import randint

class MyFrame(wx.Frame):
  def __init__(self):
    self.dicen=wx.Frame.__init__(self,parent=None, title="很生气，非常生气，灰常生气 ! ! ! ! ! !",pos=(randint(1,1300),randint(1,700)),size=(300,200),style=wx.CAPTION|wx.CLOSE_BOX)
    to_bmp_image = wx.Image('picture\\anger.jpg', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
    self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0))


class MyApp(wx.App):
  def OnInit(self):
    for i in range(20):
      self.i="myframe"+str(i)
      self.i = MyFrame()
      self.i.Show(True)
    return True

  def OnExit(self):
    for i in range(10):
      return True


if __name__=='__main__':
  app = MyApp()
  app.MainLoop()