import json
import math

import numpy as np
from matplotlib import pyplot as plt
# -*- coding: utf-8 -*-
thu = [0, 0, 0]
pku = [0, 0, 0]
sjtu = [0, 0, 0]
fdu = [0, 0, 0]
ruc = [0, 0, 0]
zju = [0, 0, 0]

with open("./school.json") as t:
    file = json.load(t)
    thu[0] = float(file["thu_data"])
    pku[0] = float(file["pku_data"])
    sjtu[0] = float(file["sjtu_data"])
    fdu[0] = float(file["fdu_data"])
    zju[0] = float(file["zju_data"])
    ruc[0] = float(file["ruc_data"])

with open("./school_involution_result.json") as t:
    file = json.load(t)
    thu[1] = float(file["thu_num"])
    pku[1] = float(file["pku_num"])
    sjtu[1] = float(file["sjtu_num"])
    fdu[1] = float(file["fdu_num"])
    zju[1] = float(file["zju_num"])
    ruc[1] = float(file["ruc_num"])

thu[2] = float(format(thu[1]*100/thu[0], ".2f"))
pku[2] = float(format(pku[1]*100/pku[0], ".2f"))
zju[2] = float(format(zju[1]*100/zju[0], ".2f"))
sjtu[2] = float(format(sjtu[1]*100/sjtu[0], ".2f"))
ruc[2] = float(format(ruc[1]*100/ruc[0], ".2f"))
fdu[2] = float(format(fdu[1]*100/fdu[0], ".2f"))


print(thu)
print(pku)
print(fdu)
print(sjtu)
print(zju)
print(ruc)

name_list = ['THU', 'PKU', 'FDU', 'SJTU', "ZJU", "RUC"]
x = [1, 2, 3, 4, 5, 6]
y = [thu[2], pku[2], fdu[2], sjtu[2], zju[2], ruc[2]]
plt.bar(x, y, align='center', color="lightblue", tick_label=name_list)
plt.title('Bar graph')
plt.ylabel('involution grade of school')
plt.xlabel("school")
for xx, yy in zip(x, y):
    plt.text(xx, yy+0.1, str(yy), ha='center')
plt.show()
