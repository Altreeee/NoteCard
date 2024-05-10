import tkinter as tk
from PIL import Image, ImageTk

class ButtonAnimationApp:
    def __init__(self, master):
        self.master = master
        self.button_images = [
            Image.open("white.png"),
            Image.open("black.png")
        ]
        self.photo_images = [ImageTk.PhotoImage(image) for image in self.button_images]

        self.button = tk.Button(master, image=self.photo_images[0], command=self.toggle_state, borderwidth=0, highlightthickness=0)
        self.button.pack()

    def toggle_state(self):
        # 切换按钮状态
        self.button.config(image=self.photo_images[1])  # 按下时显示第二张图片
        self.master.after(100, self.restore_state)  # 等待一段时间后恢复到正常状态

    def restore_state(self):
        # 恢复按钮状态
        self.button.config(image=self.photo_images[0])  # 恢复显示第一张图片

root = tk.Tk()
app = ButtonAnimationApp(root)
root.mainloop()
