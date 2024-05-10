'''
实现计时器的函数
'''

import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename
from datetime import datetime
import os

from mainfunc import find_index


def start_timer(self):
        self.seconds = 0
        self.timer = 1  #开始运行
        self.work_during = 0    #开始记录当前任务的持续时间，任务名称为self.work_name，是从点击任务按钮后的回调函数WeakAWork中得到的
        self.timer_event = update_timer(self)
    
def update_timer(self):
    while self.timer == 1:
        self.seconds += 1
        hours = self.seconds // 3600
        minutes = (self.seconds % 3600) // 60
        seconds = self.seconds % 60
        time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.timer_label.config(text=time_string)
        self.timer_event = self.after(1000, update_timer(self))
        return self.timer_event

def stop_timer(self):
    self.work_during = self.seconds
    save_worktime(self)
    self.timer = 0
    self.seconds = 0
    hours = self.seconds // 3600
    minutes = (self.seconds % 3600) // 60
    seconds = self.seconds % 60
    time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    self.timer_label.config(text=time_string)

def save_worktime(self):
    #将self.work_during加到self.items元组对应self.work_name名称的列表的第二个元素
    #首先得到这个第二个元素
    self.index = find_index(self.items, self.work_name)
    time_currentwork = self.items[self.index][1]
    second_part = str(self.work_during + int(time_currentwork))
    first_part = self.items[self.index][0]
    third_part = self.items[self.index][2]
    self.items[self.index]= (first_part,second_part,third_part)
    #保存到input.txt中
    self.write()
    gengxin_jishi(self)

def gengxin_jishi(self):
    self.label_time.config(text = "{} {}".format("已用时:", self.items[self.index][1]))