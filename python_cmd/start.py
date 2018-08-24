# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 21:05:09 2018

@author: Administrator
命令行快速查询、启动、运行
"""
import sys
sys.path.append('D:\\pycodes\\命令行快速访问')
import weather
import pyascii
import webopen
import setup
if len(sys.argv) < 2:
    sys.exit()
code= ' '.join(sys.argv[1:2])
word= ' '.join(sys.argv[2:3])
if len(sys.argv)>3:  
    t=' '.join(sys.argv[3:4])
    word=[word,t]
codes=['weather','pyascii','webopen','setup']
if code not in codes: 
    print('Wrong instructions!')
else:
    for i in range(len(codes)):
        if code==codes[i]:
            print('Instructions will be executed！')
            break
    if i==0:
        weather.data_of_tianqi(word)
    elif i==1:
        pyascii.ascii_write(word)
    elif i==2:
        webopen.webopen(word)
    elif i==3:
        setup.setup(word)
    
   
