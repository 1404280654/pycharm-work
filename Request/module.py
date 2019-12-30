#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from jiekouProjiect.config import VarConfig as var

'''1.0
一个简单的例子'''

r = requests.get(url='http://www.itwhy.org')  # 最基本的GET请求
print(r.status_code)  # 获取返回状态
r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})  # 带参数的GET请求
print(r.url)
print(r.text)  # 打印解码后的返回数据

'''2.0
不但GET方法简单，其他方法都是统一的接口样式哦！
requests.get(‘https://github.com/timeline.json’) #GET请求
requests.post(“http://httpbin.org/post”) #POST请求
requests.put(“http://httpbin.org/put”) #PUT请求
requests.delete(“http://httpbin.org/delete”) #DELETE请求
requests.head(“http://httpbin.org/get”) #HEAD请求
requests.options(“http://httpbin.org/get”) #OPTIONS请求
'''

'''3.0
POST发送JSON数据：
'''
import requests
import json

r = requests.post('https://api.github.com/some/endpoint', data=json.dumps({'some': 'data'}))
print(r.json())

'''4.0
定制header：
'''
import requests
import json

data = {'some': 'data'}
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

r = requests.post('https://api.github.com/some/endpoint', data=data, headers=headers)
print(r.text)


'''5.0
使用requests方法后，会返回一个response对象，其存储了服务器响应的内容
r = requests.get('http://www.itwhy.org')
响应方法
r.status_code #响应状态码
r.raw #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
r.content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
r.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
r.headers #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
#*特殊方法*#
r.json() #Requests中内置的JSON解码器
r.raise_for_status() #失败请求(非200响应)抛出异常
'''

'''6.0
使用Requests模块，上传文件也是如此简单的，文件的类型会自动进行处理：
'''
import requests

url = 'http://127.0.0.1:5000/upload'
files = {'file': open('/home/lyb/sjzl.mpg', 'rb')}
# files = {'file': ('report.jpg', open('/home/lyb/sjzl.mpg', 'rb'))}     #显式的设置文件名

r = requests.post(url, files=files)
print(r.text)

'''
基本身份认证(HTTPBasicAuth):
'''
import requests
from requests.auth import HTTPBasicAuth

r = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=HTTPBasicAuth('user', 'passwd'))
# r = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=('user', 'passwd'))    # 简写
print(r.json())


# cookie的获取方法
def test(self):
    data = {
        'phoneCode': '86',
        'mobile': '13048967219',
        'password': '123123aA',
        'token': '',
        'deviceId': '864426036659813',
        'clientType': '4',  # 客户端类型 1:IOS App Store版本 2:IOS企业版 3:Android Google Play版本 4:Android 普通版本（必填）
        'clientVersion': '1.0.0',
    }
    r = requests.post(url=var.stem_cell_url + '/user/applogin', data=data)
    print r.cookies
    ck_dict = requests.utils.dict_from_cookiejar(r.cookies) # 类型转换为字典
    print(type(ck_dict))
    print ck_dict.keys()[0]  # 输出字典的第一个键
    print ck_dict.values()  # 输出字典的所有值
    print r.headers['Set-Cookie']  # 直接获取cookie