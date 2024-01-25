# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 18:32:13 2021

@author: Marco
"""
import os
import pandas as pd
import numpy as np

total_label = pd.read_csv(r'C:\Users\Marco\Desktop\清华大学\2021秋 大三上\机器学习\大作业数据集\train_labels.csv')
total_data = pd.read_csv(r'C:\Users\Marco\Desktop\清华大学\2021秋 大三上\机器学习\大作业数据集\全部excel\P1\002\00a22713-68d5-372a-a009-b948ce453442.csv')
#print(total_data)

splitpoint = 0 #风机分叉行数

def getlabel(name, df, i): #name:excel名称， df：写入label的文件名，i:label中开始寻找name的行数
    global splitpoint
    label = 0 
    while total_label.loc[i,'file_name'] != name:
        i+=1
    label = total_label.loc[i,'ret']
    df['label']= label
    if i>splitpoint:
        splitpoint = i

#print(Output)
splitpoint = 0
Output = []
tempstart = 0

for part in os.listdir(r'C:\Users\Marco\Desktop\清华大学\2021秋 大三上\机器学习\大作业数据集\全部excel'):#风机文件夹目录
    domain = os.path.abspath(r'C:\Users\Marco\Desktop\清华大学\2021秋 大三上\机器学习\大作业数据集\全部excel')
    upperlayer = os.path.join(domain,part)
    for filenum in os.listdir(upperlayer):#excel文件夹目录
        domain=os.path.join(upperlayer, filenum)
        startpoint = splitpoint
        print("startpoint:", startpoint)
        print(domain)
        count = 0
        tempstart = splitpoint
        for info in os.listdir(domain):#excel文件夹
            name = os.path.join(domain, info)
            if count == 0:
                data = pd.read_csv(name)
                getlabel(info, data, tempstart)
                data = np.array(data)
                Output=data
            else:
                data = pd.read_csv(name)
                getlabel(info, data, tempstart)
                data = np.array(data)
                Output = np.concatenate((Output, data), axis = 0)
            count+=1
            print(count)#风机编号内excel数量 
        print(filenum)#风机文件夹
        np.save(domain, Output)
        Output=[]
    
    
        
    






    

