# 成像代码
import pandas as pd
#import pyqtgraph as pg
import numpy as np
import array
import matplotlib.pyplot as plt
from matplotlib.pyplot import style



from sklearn.ensemble import IsolationForest

# 定义坐标左右边界
X_Left = 0
X_Right = 30
# 定义目标上下边界
Y_Left = -15
Y_Right = 15


# ===============数据预处理===============
def sovle(data):
    x = []
    y = []
    time = []
    rcs = []
    ret_id = []
    for i in range(len(data)):
        # 将静态的点摘出来
        if data['Target_DynProp'][i] == 1 or data['Target_DynProp'][i] == 3 or \
                data['Target_DynProp'][i] == 5 or data['Target_DynProp'][i] == 7:
            # 将测试范围内的点摘出来
            if X_Left <= data['Target_DistLong'][i] <= X_Right and \
                    Y_Left <= data['Target_DistLat'][i] <= Y_Right:
                x.append(data['Target_DistLong'][i])
                y.append(data['Target_DistLat'][i])
                time.append(data['TarTimestamp'][i])
                rcs.append(data['Target_RCS'][i])
                ret_id.append(data['Target_ID'][i])
    return x, y, rcs, time, ret_id


# ===============时间转时间戳===============
def time_to_sec(t, n):
    ret = []
    for i in range(n):
        h = t[i].split(":")[0]
        m = t[i].split(":")[1]
        s = t[i].split(":")[2]
        # ns = t[i].split(":")[3]
        ret.append(int(h)*360+int(m)*60+int(s))
    # print(ret)
    return ret


# ============绘图=================
def draw(x, y, Id, rcs):
    # 格式美化
    style.use('ggplot')
    # 设置坐标轴
    ax = plt.gca()
    ax.set_xlim(X_Left, X_Right)
    ax.set_ylim(Y_Left, Y_Right)
    ax.set_xlabel('x/m')
    ax.set_ylabel('y/m')
    plt.scatter(np.array(x), np.array(y), c='orange')  # scatter函数只支持array类型数据，画散点图
    plt.title('points')

    # 寻找最大的rcs
    maxx_rcs = -1
    for i in range(len(rcs)):
        maxx_rcs = max(rcs[i], maxx_rcs)
    for i in range(len(rcs)):
        if rcs[i] == maxx_rcs:
            # 把这个点存入database，每隔一段时间拿出来与准确值的进行对比
            plt.scatter(x[i], y[i], c='r')  #画散点图
            nows = "("+str(x[i])+","+str(y[i])+")"
            s = "(x, y)="+nows+" rcs="+str(rcs[i])
            plt.text(x[i], y[i], s)
            print(maxx_rcs)
            break
    plt.show()


if __name__ == '__main__':
    # 读取数据
    Data = pd.read_csv(r'10m96_0du_2ci(1).csv')

    # 处理data
    Target_x, Target_y, Target_rcs, Time, ID = sovle(Data)

    # 获取物体当前时间（时间转为时间戳）
    Target_time = time_to_sec(Time, len(Time))
    # print(Target_time)

    # 记录每一秒内数据个数
    num = []  # 存放每周期数据个数的list
    cnt = 0  # 每周期数据个数
    for i in range(len(Target_time) - 1):
        cnt = cnt + 1
        if Target_time[i] != Target_time[i + 1]:
            num.append(cnt)
            cnt = 0
    num.append(cnt)


    # 1秒内绘制一张图
    n = len(num)
    now = 0
    plt.ion()  # 开启交互模式 展示动态图或多个窗口
    plt.subplots()
    for i in range(n):
        plt.clf()  # 清空画布
        # 截取每秒的数据
        Target_x_split = Target_x[now:now + num[i]]
        Target_y_split = Target_y[now:now + num[i]]
        Target_rcs_split = Target_rcs[now:now + num[i]]
        Target_id_split = ID[now:now + num[i]]
        now = now + num[i]
        draw(Target_x_split, Target_y_split, ID, Target_rcs_split)
        plt.pause(1)  # 每次绘图后暂停X秒
    plt.ioff()
    plt.show()  #