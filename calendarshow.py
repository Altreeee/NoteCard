import calendar
from datetime import datetime

def generate_calendar(year, month):
    # 创建一个日历对象
    cal = calendar.Calendar()

    # 获取指定年月的所有日期
    dates = list(cal.itermonthdays(year, month))

    # 获取本月的第一天是星期几
    first_weekday = calendar.weekday(year, month, 1)

    # 输出日历表头
    print("Mon Tue Wed Thu Fri Sat Sun")

    # 补充空白
    for i in range(first_weekday):
        print("    ", end=" ")

    # 输出日期和对应的星期几
    for date in dates:
        if date != 0:
            print(f"{date:3}", end=" ")
        else:
            print("   ", end=" ")
        # 输出换行符
        if (first_weekday + date) % 7 == 6:
            print()

if __name__ == "__main__":
    # 获取当前年份和月份
    current_date = datetime.now()
    year = current_date.year
    month = current_date.month

    # 生成并输出日历
    generate_calendar(year, month)

    # 输入任意字符以退出程序
    input("按 Enter 键退出程序...")
