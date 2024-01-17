# 导入time模块
import time

# 定义一个名为focus_timer的函数，接受一个参数minutes，表示要专注的分钟数
def focus_timer(minutes):
    # 将分钟数乘以60，得到专注时钟的总秒数
    seconds = minutes * 60

    # 使用一个while循环来创建倒计时，显示剩余的时间
    while seconds:
        # 计算剩余的分钟数和秒数
        mins, secs = divmod(seconds, 60)
        # 格式化倒计时时间的文本
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # 打印倒计时时间，使用\r来覆盖上一次的输出
        print(timer, end="\r")
        # 等待一秒钟
        time.sleep(1)
        # 将剩余秒数减一
        seconds -= 1

    # 打印"Time's up!"，提示用户专注时钟已完成
    print("Time's up!")
  
