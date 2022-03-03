import os
import json
import numpy as np
from matplotlib import pyplot as plt


def str_convert(thu_mean):
    if 50942<=thu_mean<=55555:
        thu_mean = int(thu_mean)
        hour = thu_mean // 3600
        minute = (thu_mean - 3600 * hour) // 60
        seconds = thu_mean - 3600 * hour - 60 * minute
        if hour < 10:
            hour = "0" + str(hour)
        if minute < 10:
            minute = "0" + str(minute)
        if seconds < 10:
            seconds = "0" + str(seconds)
        time = str(hour) + ":" + str(minute) + ":" + str(seconds)
        return time
    else:
        return str(thu_mean)


data_list = []
name_list = []
pku_list = []
thu_list = []
fdu_list = []
zju_list = []
ruc_list = []
sjtu_list = []

pku_time_list = []
thu_time_list = []
fdu_time_list = []
zju_time_list = []
ruc_time_list = []
sjtu_time_list = []

with open("./school.json", encoding="utf-8") as t:
    file = json.load(t)
    thu_list = file["thu"]
    pku_list = file["pku"]
    sjtu_list = file["sjtu"]
    fdu_list = file["fdu"]
    ruc_list = file["ruc"]
    zju_list = file["zju"]

for video in thu_list:
    with open(f"./data/{video}", encoding="utf-8") as t:
        file = json.load(t)
        hour = int(file["post_time"][11:13])
        minute = int(file["post_time"][14:16])
        seconds = int(file["post_time"][17:19])
        time = hour * 3600 + minute * 60 + seconds
        thu_time_list.append(time)

for video in pku_list:
    with open(f"./data/{video}", encoding="utf-8") as t:
        file = json.load(t)
        hour = int(file["post_time"][11:13])
        minute = int(file["post_time"][14:16])
        seconds = int(file["post_time"][17:19])
        time = hour * 3600 + minute * 60 + seconds
        pku_time_list.append(time)

for video in sjtu_list:
    with open(f"./data/{video}", encoding="utf-8") as t:
        file = json.load(t)
        hour = int(file["post_time"][11:13])
        minute = int(file["post_time"][14:16])
        seconds = int(file["post_time"][17:19])
        time = hour * 3600 + minute * 60 + seconds
        sjtu_time_list.append(time)

for video in fdu_list:
    with open(f"./data/{video}", encoding="utf-8") as t:
        file = json.load(t)
        hour = int(file["post_time"][11:13])
        minute = int(file["post_time"][14:16])
        seconds = int(file["post_time"][17:19])
        time = hour * 3600 + minute * 60 + seconds
        fdu_time_list.append(time)

for video in zju_list:
    with open(f"./data/{video}", encoding="utf-8") as t:
        file = json.load(t)
        hour = int(file["post_time"][11:13])
        minute = int(file["post_time"][14:16])
        seconds = int(file["post_time"][17:19])
        time = hour * 3600 + minute * 60 + seconds
        zju_time_list.append(time)

for video in ruc_list:
    with open(f"./data/{video}", encoding="utf-8") as t:
        file = json.load(t)
        hour = int(file["post_time"][11:13])
        minute = int(file["post_time"][14:16])
        seconds = int(file["post_time"][17:19])
        time = hour * 3600 + minute * 60 + seconds
        ruc_time_list.append(time)

thu_mean = float(format(np.mean(thu_time_list), ".2f"))
thu_var = float(format(np.var(thu_time_list)/10000, ".2f"))
thu_std = float(format(np.std(thu_time_list, ddof=1), ".2f"))
data_list.append(thu_mean)
data_list.append(thu_var)
data_list.append(thu_std)

pku_mean = float(format(np.mean(pku_time_list), ".2f"))
pku_var = float(format(np.var(pku_time_list)/10000, ".2f"))
pku_std = float(format(np.std(pku_time_list, ddof=1), ".2f"))
data_list.append(pku_mean)
data_list.append(pku_var)
data_list.append(pku_std)

sjtu_mean = float(format(np.mean(sjtu_time_list), ".2f"))
sjtu_var = float(format(np.var(sjtu_time_list)/10000, ".2f"))
sjtu_std = float(format(np.std(sjtu_time_list, ddof=1), ".2f"))
data_list.append(sjtu_mean)
data_list.append(sjtu_var)
data_list.append(sjtu_std)

fdu_mean = float(format(np.mean(fdu_time_list), ".2f"))
fdu_var = float(format(np.var(fdu_time_list)/10000, ".2f"))
fdu_std = float(format(np.std(fdu_time_list, ddof=1), ".2f"))
data_list.append(fdu_mean)
data_list.append(fdu_var)
data_list.append(fdu_std)

zju_mean = float(format(np.mean(zju_time_list), ".2f"))
zju_var = float(format(np.var(zju_time_list)/10000, ".2f"))
zju_std = float(format(np.std(zju_time_list, ddof=1), ".2f"))
data_list.append(zju_mean)
data_list.append(zju_var)
data_list.append(zju_std)

ruc_mean = float(format(np.mean(ruc_time_list), ".2f"))
ruc_var = float(format(np.var(ruc_time_list)/10000, ".2f"))
ruc_std = float(format(np.std(ruc_time_list, ddof=1), ".2f"))
data_list.append(ruc_mean)
data_list.append(ruc_var)
data_list.append(ruc_std)

name_list.append("thu_mean")
name_list.append("thu_var")
name_list.append("thu_std")
name_list.append("pku_mean")
name_list.append("pku_var")
name_list.append("pku_std")
name_list.append("fdu_mean")
name_list.append("fdu_var")
name_list.append("fdu_std")
name_list.append("sjtu_mean")
name_list.append("sjtu_var")
name_list.append("sjtu_std")
name_list.append("zju_mean")
name_list.append("zju_var")
name_list.append("zju_std")
name_list.append("ruc_mean")
name_list.append("ruc_var")
name_list.append("ruc_std")
print(name_list)
print(data_list)

x = range(1, 19, 1)
y = data_list
plt.bar(x, y, align='center', color=["lightblue", "purple", "green"]*6, tick_label=name_list)
plt.title('Bar graph')
plt.ylabel('average video post time of school')
plt.xlabel("school")


for xx, yy in zip(x, y):
    plt.text(xx, yy + 0.1, str_convert(yy), ha='center')
plt.show()
