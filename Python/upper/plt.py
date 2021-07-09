#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random
from tkinter import *
from tkinter import ttk
import _thread
import time


filename = 'Data.txt'

def readData():
    try:
        data = [] #清空 y 轴数据
        timelines = [] #清空 x 时间轴
        with open(filename) as file_object:
            lines = file_object.readlines()
            for line in lines[:50]:
                perdata, pertime = line.split(',')
                data.append(int(perdata.rstrip()))
                timelines.append(float(pertime.rstrip()))
        return data, timelines
    except:
        pass

if __name__ == "__main__":
    plt.ion() # 图表实时更新数据

    main = Tk()  # 表格初始框申明
    treeview = ttk.Treeview(main, show="headings", columns=("x", "y"))  # 表格
    treeview.heading("x", text="x") # 显示表头
    treeview.heading("y", text="y")
    treeview.pack()

    # app = Application()
    while True:
        data, timelines = readData() # 读取文件数据
        for i in range(len(data)):
            treeview.insert('', i, values=(data[i], timelines[i]))
        plt.rcParams['figure.figsize'] = (15, 5) # 显示尺寸
        plt.clf() # 刷新图表
        plt.plot(timelines, data) # 画图
        plt.xlabel("time")  # 横坐标名字
        plt.ylabel("data")  # 纵坐标名字
        plt.pause(0.5)
