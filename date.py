import tkinter as tk
from datetime import datetime
from tkinter import ttk

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Calendar")
        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)
        self.create_calendar()

    def create_calendar(self):
        self.labels = []
        for i in range(6):
            for j in range(7):
                label = ttk.Label(self.frame, text="", width=5, relief="ridge")
                label.grid(row=i, column=j, padx=5, pady=5)
                self.labels.append(label)

    def update_calendar(self, dates_with_color):
        for label in self.labels:
            label.config(bg="white")  # 重置所有标签的背景颜色
        for date, color in dates_with_color.items():
            try:
                date_obj = datetime.strptime(date, "%Y-%m-%d")
                row = (date_obj.day - 1) // 7
                col = (date_obj.day - 1) % 7
                index = row * 7 + col
                self.labels[index].config(bg=color)
            except ValueError:
                print("Invalid date format:", date)

# 示例的调用
if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    dates_with_color = {"2024-05-10": "red", "2024-05-15": "blue", "2024-05-20": "green"}
    app.update_calendar(dates_with_color)
    root.mainloop()
