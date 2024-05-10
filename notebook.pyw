'''https://www.bilibili.com/video/BV1Fz4y1C7r3/?spm_id_from=333.337.search-card.all.click&vd_source=db2399dce33b19d6a7073c296cbfa1e9'''

import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename

filename = ""

def main():
    def c_new():
        global filename
        filename = ""
        text.delete(1.0,"end")
    def c_open():
        global filename
        filename = askopenfilename()
        if filename:
            with open(filename,encoding="utf-8") as f:
                text.delete(1.0,"end")
                text.insert(1.0,f.read())
    def c_save():
        global filename
        if not filename:
            filename = asksaveasfilename(
                filetypes=[("文本文件","*.txt")],
                defaultextension="*.txt"
            )
        if filename:
            with open(filename,"w",encoding="utf-8") as f:
                f.write(text.get(1.0,"end-1c"))
    root = tk.Tk()
    root.title("notebook")
    menu = tk.Menu(root)
    root["menu"] = menu
    m_file = tk.Menu(menu)
    menu.add_cascade(label="文件",menu=m_file)
    m_file.add_command(label="新建",command= c_new)
    m_file.add_command(label="打开",command= c_open)
    m_file.add_command(label="保存",command= c_save)
    text = ScrolledText(root,width=100,height=40)
    text.pack()
    text.focus()
    root.mainloop()

if __name__=="__main__":
    main()