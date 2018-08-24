# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 10:59:15 2018
命令行启动应用程序
@author: Administrator
"""
import subprocess
def setup(word):
    words=['excel','word','ppt','visio','pycharm']
    if word not in words:
        print('打开失败！')
    else:
        for i in range(len(words)):
            if word==words[i]:
                print(word+'应用程序正在打开中。。。')
                break
        if i==0:
            subprocess.Popen('C:\\Program Files\\Microsoft Office\\Office16\\EXCEL.exe')
        if i==1:
            subprocess.Popen('C:\\Program Files\\Microsoft Office\\Office16\\WINWORD.exe')
        if i==2:
            subprocess.Popen('C:\\Program Files\\Microsoft Office\\Office16\\POWERPNT.exe')
        if i==3:
            subprocess.Popen('C:\\Program Files\\Microsoft Office\\Office16\\VISIO.exe')
        if i==4:
            subprocess.Popen('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2017.2.4\\bin\\pycharm64')
