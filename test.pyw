import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("中央显示界面")
        
        # 创建一个主框架
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建一个容器框架，用于显示界面
        self.container = tk.Frame(self.main_frame)
        self.container.pack(fill=tk.BOTH, expand=True)
        
        # 创建3个按钮，用于切换界面，垂直排列在上侧
        button1 = tk.Button(self, text="收藏", command=self.show_frame1)
        button1.pack(side=tk.TOP, padx=5, pady=5)
        button2 = tk.Button(self, text="加卡", command=self.show_frame2)
        button2.pack(side=tk.TOP, padx=5, pady=5)
        '''button3 = tk.Button(self, text="界面3", command=self.show_frame3)
        button3.pack(side=tk.LEFT, padx=5, pady=5)'''
        
        # 默认显示一个欢迎界面
        self.show_welcome()
        
    def show_welcome(self):
        # 清除容器中的所有组件
        for widget in self.container.winfo_children():
            widget.destroy()
        '''
        # 在容器中央显示欢迎信息
        label = tk.Label(self.container, text="欢迎使用！", font=("Helvetica", 24))
        label.grid(side=tk.BOTTOM,expand=True)
        '''
        

    def show_frame1(self):
        # 清除容器中的所有组件
        for widget in self.container.winfo_children():
            widget.destroy()
        
        # 在容器中央显示界面1内容
        label = tk.Label(self.container, text="界面1内容", font=("Helvetica", 24))
        label.pack(expand=True)
        
        # 创建返回按钮
        back_button = tk.Button(self.container, text="返回", command=self.show_welcome)
        back_button.pack()
    
    def show_frame2(self):
        # 清除容器中的所有组件
        for widget in self.container.winfo_children():
            widget.destroy()
        
        # 在容器中央显示界面2内容
        label = tk.Label(self.container, text="界面2内容", font=("Helvetica", 24))
        label.pack(expand=True)
        
        # 创建返回按钮
        back_button = tk.Button(self.container, text="返回", command=self.show_welcome)
        back_button.pack()
        
    def show_frame3(self):
        # 清除容器中的所有组件
        for widget in self.container.winfo_children():
            widget.destroy()
        
        # 在容器中央显示界面3内容
        label = tk.Label(self.container, text="界面3内容", font=("Helvetica", 24))
        label.pack(expand=True)
        
        # 创建返回按钮
        back_button = tk.Button(self.container, text="返回", command=self.show_welcome)
        back_button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
