from pickle import TRUE         #二进制序列文本
import xlwings as xw            #导入xlwings库
import math                     #导入math
import statistics as sta        #导入statistics库
from collections import Counter
import matplotlib.pyplot as plt #导入matplotlib.pyplot库
plt.rcParams['font.sans-serif']=['SimHei']  #显示中文
import numpy as np              #导入numpy库
from scipy.stats import norm    #导入scipy库
from collections import Counter
from tqdm import tqdm
import functools
import os
import time
import json


def get_list(target):
    dirs = os.listdir(target)
    file_list = []
    for file in dirs:
         file_list.append(f"{target}/{file}")
    return file_list

if __name__ == "__main__":
    dic = get_list(r"C:\Users\liuy\Desktop\日语新闻 - 副本")
    allThings = []
    for file in tqdm(dic):
        with open(file, 'r',encoding='utf-8',errors='ignore') as f:
            try:
                tempGet = json.load(f)
                allThings.append(tempGet)
            except Exception as e:
                print(e)
                print(file)
    with open(r"C:\Users\liuy\Desktop\DNA图片\日语汇总.json", 'w+',encoding='utf-8',errors='ignore') as f:
        json.dump(allThings, f,ensure_ascii = False,indent = 2)