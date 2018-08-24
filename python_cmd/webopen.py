
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 11:06:53 2018
快速搜索（百度、360、必应）&快速打开常用网站
csdn 百度 MOOC  新华社
@author: Administrator
"""
import webbrowser
def search(word):
    if word[0]=='baidu':
        print('百度搜索'+word[1]+'内容正在打开。。。')
        webbrowser.open('https://www.baidu.com/s?wd='+word[1])
    if word[0]=='360':
        print('360搜索'+word[1]+'内容正在打开。。。')
        webbrowser.open('https://www.so.com/s?q='+word[1])
    if word[0]=='biying':
        print('必应搜索'+word[1]+'内容正在打开。。。')
        webbrowser.open('http://global.bing.com/search?q='+word[1])
def webopen(word):
    name=['csdn','百度','MOOC','新华社']
    words=['csdn','baidu','mooc'，'xhs']
    if type(word)==list:
        search(word)
    elif word not in words:
        print('访问失败！')
    else:
        for i in range(len(words)):
            if word==words[i]:
                print('您访问的'+name[i]+'正在打开。。。')
                break
        if i==0:
            webbrowser.open('https://download.csdn.net/my')
        elif i==1:
            webbrowser.open('https://www.baidu.com/')
        elif i==2:
            webbrowser.open('http://www.icourse163.org/home.htm?userId=7816710#/home/course')
        elif i==3:
            webbrowser.open('http://www.xinhuanet.com/english/home.htm') 