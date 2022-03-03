from pickle import TRUE         #二进制序列文本
import xlwings as xw
import matplotlib.pyplot as plt
import matplotlib
from tqdm import tqdm
import functools

from Graph1 import getAllLists
plt.rcParams['font.sans-serif']=['SimHei']  #显示中文
import time
import json
import os
from collections import Counter

def get_list(target):
    dirs = os.listdir(target)
    file_list = []
    for file in dirs:
         file_list.append(f"{target}/{file}")
    return file_list

def isChina(content):
    for i in content:
        if 12352 <= ord(i) and ord(i) <= 12447:
            return False
    return True

def remainChina(fileList):
    ansChina = []
    for file in tqdm(fileList):
        with open(file, 'r',encoding='utf8',errors='ignore') as f:
            try:
                content = json.load(f)["content"]
                if isChina(content):
                    ansChina.append(file)
            except Exception as e:
                print(e)
        f.close()
    return ansChina

if __name__ == '__main__':
    # 12352-12447
    getposi = remainChina(get_list(r"C:\Users\liuy\Desktop\Results"))
    for posi in tqdm(getposi):
        try:
            os.remove(posi)
        except Exception as e:
            print(e)