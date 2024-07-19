# 导入tkinter和time模块
import tkinter as tk
import time

# 定义一个专注时钟类
class FocusTimer:

    # 初始化方法，创建窗口和组件
    def __init__(self):
        # 创建一个窗口对象
        self.window = tk.Tk()
        # 设置窗口的标题
        self.window.title("专注时钟")
        # 设置窗口的大小和位置
        self.window.geometry("300x200+500+200")
        # 设置窗口是否可以调整大小
        self.window.resizable(False, False)

        # 创建一个标签对象，用于显示当前时间
        self.current_time_label = tk.Label(self.window, text="", font=("Arial", 16))
        # 将标签对象放置在窗口的上方
        self.current_time_label.pack(side=tk.TOP, pady=10)

        # 创建一个标签对象，用于显示倒计时时间
        self.countdown_time_label = tk.Label(self.window, text="", font=("Arial", 16))
        # 将标签对象放置在窗口的中间
        self.countdown_time_label.pack(side=tk.TOP, pady=10)

        # 创建一个输入框对象，用于输入专注的分钟数
        self.entry = tk.Entry(self.window, width=10)
        # 将输入框对象放置在窗口的下方
        self.entry.pack(side=tk.TOP, pady=10)

        # 创建一个框架对象，用于放置按钮
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(side=tk.TOP, pady=10)

        # 创建一个按钮对象，用于开始专注时钟
        self.start_button = tk.Button(self.button_frame, text="开始", command=self.start)
        # 将按钮对象放置在框架的左边
        self.start_button.pack(side=tk.LEFT, padx=10)

        # 创建一个按钮对象，用于暂停专注时钟
        self.pause_button = tk.Button(self.button_frame, text="暂停", command=self.pause)
        # 将按钮对象放置在框架的中间
        self.pause_button.pack(side=tk.LEFT, padx=10)
        
        # 创建一个按钮对象，用于继续专注时钟
        self.resume_button = tk.Button(self.button_frame, text="继续", command=self.resume)
        # 将按钮对象放置在框架的右边
        self.resume_button.pack(side=tk.LEFT, padx=10)

        # 定义一个布尔变量，用于表示专注时钟是否正在运行
        self.running = False
        # 定义一个整数变量，用于表示专注时钟的剩余秒数
        self.seconds = 0
        # 定义一个字符串变量，用于表示专注时钟的状态
        self.status = ""

        # 调用update方法，更新时间和界面
        self.update()

        # 进入窗口的主循环
        self.window.mainloop()

    # 定义一个开始方法，用于开始专注时钟
    def start(self):
        # 如果专注时钟没有在运行
        if not self.running:
            # 尝试从输入框获取专注的分钟数
            try:
                # 将输入框的内容转换为整数
                minutes = int(self.entry.get())
                # 如果分钟数大于0
                if minutes > 0:
                    # 将分钟数乘以60，得到专注时钟的总秒数
                    self.seconds = minutes * 60
                    # 将专注时钟的状态设置为"专注中"
                    self.status = "专注中"
                    # 将专注时钟的运行状态设置为True
                    self.running = True
                # 否则
                else:
                    # 弹出一个错误提示框，提示输入的分钟数必须大于0
                    tk.messagebox.showerror("错误", "输入的分钟数必须大于0")
            # 如果发生异常
            except:
                # 弹出一个错误提示框，提示输入的内容必须是整数
                tk.messagebox.showerror("错误", "输入的内容必须是整数")

    # 定义一个暂停方法，用于暂停专注时钟
    def pause(self):
        # 如果专注时钟在运行
        if self.running:
            # 将专注时钟的运行状态设置为False
            self.running = False
            # 将专注时钟的状态设置为"已暂停"
            self.status = "已暂停"
    
    # 定义一个继续方法，用于继续专注时钟
    def resume(self):
        # 如果专注时钟没有在运行且还有剩余秒数
        if not self.running and self.seconds > 0:
            # 将专注时钟的运行状态设置为True
            self.running = True
            # 将专注时钟的状态设置为"专注中"
            self.status = "专注中"

    # 定义一个更新方法，用于更新时间和界面
    def update(self):
        # 获取当前时间
        current_time = time.strftime("%H:%M:%S")
        # 更新当前时间标签的文本
        self.current_time_label.config(text=current_time)

        # 如果专注时钟在运行
        if self.running:
            # 如果专注时钟的剩余秒数大于0
            if self.seconds > 0:
                # 将专注时钟的剩余秒数减一
                self.seconds -= 1
                # 计算专注时钟的剩余分钟数和秒数
                minutes, seconds = divmod(self.seconds, 60)
                # 格式化倒计时时间的文本
                countdown_time = "%02d:%02d" % (minutes, seconds)
                # 更新倒计时时间标签的文本
                self.countdown_time_label.config(text=countdown_time)
            # 否则
            else:
                # 将专注时钟的运行状态设置为False
                self.running = False
                # 将专注时钟的状态设置为"已完成"
                self.status = "已完成"
                # 弹出一个信息提示框，提示专注时钟已完成
                tk.messagebox.showinfo("提示", "专注时钟已完成")

        # 更新专注时钟状态标签的文本
        self.window.title("专注时钟 - " + self.status)

        # 1000毫秒后再次调用update方法
        self.window.after(1000, self.update)

# 创建一个专注时钟对象
focus_timer = FocusTimer()
