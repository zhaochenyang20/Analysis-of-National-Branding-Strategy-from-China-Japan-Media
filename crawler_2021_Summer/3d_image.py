import os
import json
import numpy as np
import matplotlib.pyplot as plt


file_list = os.listdir("./data")
# print(file_list)
bullet_list = []
video_like_list = []
video_watched_list = []
video_coin_list = []
video_share_list = []
video_collect_list = []

for video in file_list:
    with open(f"./data/{video}", "r", encoding='utf-8') as t:
        file = json.load(t)
        bullet_list.append(float(file["bullet"]))
        video_like_list.append(float(file["video_like"]))
        video_watched_list.append(float(file["video_watched"]))
        video_coin_list.append(float(file["video_coin"]))
        video_share_list.append(float(file["video_share"]))
        video_collect_list.append(float(file["video_collect"]))

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# matplotlib画图中中文显示会有问题，需要这两行设置默认字体

plt.xlabel('观看数量')
plt.ylabel('分享数量')
plt.xlim(xmax=10000, xmin=0)
plt.ylim(ymax=100, ymin=0)
# 画两条（0-9）的坐标轴并设置轴标签x，y

x1 = video_watched_list
y1 = video_share_list

colors1 = '#00CED1'  # 点的颜色
area = np.pi * 0.1 ** 0.1  # 点面积
# 画散点图
plt.scatter(x1, y1, s=area, c=colors1, alpha=0.4, label='观看量在一万以下的视频，观看量与分享数量没有明显的线性关系')
plt.legend()
plt.show()
