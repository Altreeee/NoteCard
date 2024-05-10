'''
基础功能函数
'''

import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename
from datetime import datetime
import os



def find_index(items, target):
    # 使用列表推导来找到第一个值为 target 的元组的索引
    index = next((index for index, item in enumerate(items) if item[0] == target), None)
    return index

def read_contentroad(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            last_sentence = None
            for line in file:
                # 解析日期和句子内容
                parts = line.strip().split('#')
                if len(parts) == 2:
                    sentence, date_str = parts
                    # 格式化日期
                    date = datetime.strptime(date_str.strip(), "%Y-%m-%d")
                    # 拼接日期和句子内容
                    formatted_sentence = f"{date.strftime('%Y-%m-%d')}:{sentence.strip()}"
                    last_sentence = formatted_sentence
            return last_sentence
    except FileNotFoundError:
        with open(file_path, 'w') as file:
            # 将元组中的数据格式化为字符串，并写入文件
            line = ' ' + '\n'
            file.write(line)
        return line