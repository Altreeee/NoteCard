'''
将函数分离到其它文件中
状态：未完成，起步
'''



import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename
from datetime import datetime
import os

from mainfunc import find_index,read_contentroad
from timer import start_timer,stop_timer

class CustomNotebook(ScrolledText):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

    def new_file(self):
        self.delete(1.0, "end")

    def open_file(self):
        filename = askopenfilename()
        if filename:
            with open(filename, encoding="utf-8") as f:
                self.delete(1.0, "end")
                self.insert("end", f.read())

    '''def save_file(self, file_path):
        if file_path:
            with open(file_path, "a", encoding="utf-8") as f:
                f.write("\n" + self.get(1.0, "end-1c"))
            self.new_file()'''
    def save_file(self, file_path):
        if file_path:
            with open(file_path, "a", encoding="utf-8") as f:
                now = datetime.now().strftime("%Y-%m-%d")  # 获取当前日期并格式化为 YYYY-MM-DD
                sentence = self.get(1.0, "end-1c")
                sentence_with_date = f"{sentence}#{now}\n"  # 在句子后面添加日期和 #
                f.write(sentence_with_date)
            self.new_file()

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("中央显示界面")

        # 设置窗口大小
        self.geometry("600x500")
        # 设置窗口透明度
        self.attributes("-alpha", 0.8)  # 设置透明度为 80%
        
        # 创建一个主框架
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        #计时器运行标志
        self.timer = 0  #0代表不运行计时器

        #从本地存储中读取数据
        self.items=[]
        self.read()

        # 默认显示一个欢迎界面
        self.show_UpdateCard()

    
    def show_UpdateCard(self):
        # 清除容器中的所有组件
        for widget in self.winfo_children():
            widget.destroy()
        
        #左上Frame
        self.framezuoshang = tk.Frame(self)
        self.framezuoshang.grid(row=0,column=0)
            #添加开始计时按钮
        buttonstart = tk.Button(self.framezuoshang,text="开始计时", command=(self.start_timer))
        buttonstart.grid(row=1,column=0)
            #添加结束计时按钮
        buttonend = tk.Button(self.framezuoshang,text="结束计时", command=(self.stop_timer))
        buttonend.grid(row=1,column=1)
            #添加计时器
        self.timer_label = tk.Label(self.framezuoshang, text="00:00:00", font=("Helvetica", 18))
        self.timer_label.grid(row=0, column=0)
        



        #右上Frame
        self.frameyoushang = tk.Frame(self)
        self.frameyoushang.grid(row=0,column=1,columnspan=2)
        '''self.label_Empty = tk.Label(self.frameyoushang,text="请选择当前工作",font=("Helvetica", 18))
        self.label_Empty.grid(row=0,column=0)'''
        self.WeakAWork(self.items[0][0])    #默认显示za
        


        #左下Frame
        framezuoxia = tk.Frame(self)
        framezuoxia.grid(row=1,column=0)
            # 创建3个按钮，用于切换界面，垂直排列在上侧
        button1 = tk.Button(framezuoxia, text="收藏", command=self.show_shoucang)
        button1.grid(row=0,column=0)
        button2 = tk.Button(framezuoxia, text="加卡", command=self.show_jiaka)
        button2.grid(row=1,column=0)
        button3 = tk.Button(framezuoxia, text="选项", command=self.show_xuanxiang)
        button3.grid(row=2,column=0)



        #右下Frame
        frameyouxia = tk.Frame(self)
        frameyouxia.grid(row=1,column=1,columnspan=2)
            #按照卡牌内容生成按钮,名称#时长#评述内容
        column_item = 0
        i = 0
        for item in self.items:
            button = tk.Button(frameyouxia, text=item[0], command=lambda work_name=item[0]: self.WeakAWork(work_name))
            button.grid(row=0,column=column_item)
            column_item = column_item + 1
            i = i + 1
        

        

#############################################################启用卡牌后的动作################################################

    def WeakAWork(self,work_name):
        self.work_name=work_name    #得到当前任务名称
        # 清除容器中的所有组件
        for widget in self.frameyoushang.winfo_children():
            widget.destroy()
        #加载当前任务的详情
        index = find_index(self.items, work_name)
        self.label_time = tk.Label(self.frameyoushang,text = "{} {}".format("已用时:", self.items[index][1]),font=("Helvetica", 18))
        self.label_time.grid(row=0,column=0,columnspan=2)

        label_content_road = self.items[index][2]
        content = read_contentroad(label_content_road)
        #self.label_content = tk.Label(self.frameyoushang,text = "{} {}".format("注释：", content),font=("Helvetica", 18))
        self.label_content = tk.Label(self.frameyoushang,text = content,font=("Helvetica", 18))
        self.label_content.grid(row=1,column=0,columnspan=2)
         
        #notebook
        self.custom_notebook = CustomNotebook(self.frameyoushang, width=50, height=20)
        self.custom_notebook.grid(row=2, column=0,columnspan=2,sticky="nsew")
            # 添加保存按钮
        self.save_button = tk.Button(self.frameyoushang, text="保存", command=lambda file_path=label_content_road: (self.custom_notebook.save_file(file_path),self.gengxin(label_content_road)))
        self.save_button.grid(row=3, column=0,sticky="ew")
            # 添加清空按钮
        self.clear_button = tk.Button(self.frameyoushang, text="清空", command=self.custom_notebook.new_file)
        self.clear_button.grid(row=3, column=1,sticky="ew")

    #点击保存后更新上面显示的content内容
    def gengxin(self,label_content_road):
        content = read_contentroad(label_content_road)
        #self.label_content.config(text="{} {}".format("注释：", content))
        self.label_content.config(text=content)

####################################################################################################界面切换显示##################

    def show_shoucang(self):
        '''
        收藏
            显示所有卡片的按钮(给卡片修改名称也要在这里实现)
                点击后
                    日历
                        读取卡片名称对应的content文件
                            读取content文件中每一行结尾处的日期
                                显示一个日历，点亮读取到的所有日期
                    按钮
                        查看对应txt文件
                    按钮
                        修改名称
                    按钮
                        返回
        '''
        # 清除容器中的所有组件
        for widget in self.winfo_children():
            widget.destroy()
        
        # 在容器中央显示界面1内容
        label = tk.Label(self, text="收藏", font=("Helvetica", 24))
        label.pack(expand=True)
        
        # 创建返回按钮
        back_button = tk.Button(self, text="返回", command=self.show_UpdateCard)
        back_button.pack()
    
################################################################################加卡部分代码#####################################
    def show_jiaka(self):
        # 清除容器中的所有组件
        for widget in self.winfo_children():
            widget.destroy()
        
        # 在容器中央显示界面2内容
        '''label = tk.Label(self, text="加卡", font=("Helvetica", 24))
        label.grid(row=0,column=0)'''
        #左侧名称，右侧输入名称
        label_name = tk.Label(self, text="name", font=("Helvetica", 24))
        label_name.grid(row=0,column=0)
        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0,column=1,columnspan=2)
        #确认按钮，获得名称内容
        ok_button = tk.Button(self, text="OK", command=self.get_entry_content)
        ok_button.grid(row=1,column=0)
        # 创建返回按钮
        back_button = tk.Button(self, text="返回", command=self.show_UpdateCard)
        back_button.grid(row=2,column=0)

    def get_entry_content(self):
        self.newcardname = self.entry_name.get()
        num = len(self.items)
        #print("用户输入的内容是:", content)
        self.items.append((self.newcardname, "0", "content{}.txt".format(num-1)))
        self.write()
        self.show_UpdateCard()
#########################################################################################################################

    
    def show_xuanxiang(self):
        # 清除容器中的所有组件
        for widget in self.winfo_children():
            widget.destroy()
        
        # 在容器中央显示界面2内容
        label = tk.Label(self, text="选项", font=("Helvetica", 24))
        label.pack(expand=True)
        
        # 创建返回按钮
        back_button = tk.Button(self, text="返回", command=self.show_UpdateCard)
        back_button.pack()

##############################################################################################计时器########################
    def start_timer(self):
        start_timer(self)
    
    def stop_timer(self):
        stop_timer(self)


###########################################################################################读写数据文件###########################
    def read(self):
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                # 逐行读取文件内容
                if len(lines) >= 1:
                    for i, line in enumerate(lines):
                        '''if i == 0:  # 跳过第一行,第一行默认为第一次打开时生成的杂
                            continue'''
                        # 去除行末的换行符并分割字符串
                        item_info = line.strip().split('#')
                        # 提取卡牌名称和价格
                        item_name = item_info[0]
                        item_time = item_info[1]
                        iten_content_road = item_info[2]    #content的内容首先用文件路径存储
                        # 添加卡牌信息到列表
                        self.items.append((item_name, item_time, iten_content_road))
        except FileNotFoundError:
            self.items = [("za","0","content.txt")]  # 存储卡牌信息的列表
            self.write()

    def write(self):
        with open(file_path, 'w') as file:
            for item in self.items:
                # 将元组中的数据格式化为字符串，并写入文件
                line = '#'.join(item) + '\n'
                file.write(line)
        

if __name__ == "__main__":
    #file_path = "D:\\Desktop\\notebook\\input.txt"
    file_path = "input.txt"
    app = SampleApp()
    app.mainloop()
