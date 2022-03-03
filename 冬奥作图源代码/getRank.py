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

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('start executing %s' % (fn.__name__))
        start_time = time.time()
        result = fn(*args, **kw)
        end_time = time.time()
        t = 1000 * (end_time - start_time)
        print('%s executed in %s ms' % (fn.__name__, t))
        return result
    return wrapper


def get_rank(file):
    lists=[]
    with open(file, 'r',encoding='utf8',errors='ignore') as f:
        try:
            dictions = json.load(f)
            for diction in tqdm(dictions):
                newDictions = sorted(diction.items(),key=lambda x:x[1],reverse=True)
                lists.append(newDictions)
        except Exception as e:
            print(e)
            print("Error rank")
    return lists


def getTotalTimes(file):
    total = []
    with open(file, 'r',encoding='utf-8',errors='ignore') as f:
        try:
            dictions = json.load(f)
            for diction in tqdm(dictions):
                total.append(sum(diction.values()))
        except Exception as e:
            print(e)
            print()
    return total

if __name__ == "__main__":
    fileTitle = r"C:\Users\liuy\Desktop\workFlow\resultsTitle.json"
    fileContent = r"C:\Users\liuy\Desktop\workFlow\resultsContents.json"
    orderedTitle = get_rank(fileTitle)
    orderedContent = get_rank(fileContent)
    totalTitle = getTotalTimes(fileTitle)
    totalContent = getTotalTimes(fileContent)

    with open("./orderedTitle.json", "w+", encoding = "utf-8", errors = "ignore") as f:
        json.dump(orderedTitle, f, ensure_ascii = False, indent = 2)
    with open("./orderedContent.json", "w+", encoding = "utf-8", errors = "ignore") as f:
        json.dump(orderedContent, f, ensure_ascii = False, indent = 2)
    
    with open("./totalTitle.json", "w+", encoding = "utf-8", errors = "ignore") as f:
        json.dump(totalTitle, f, ensure_ascii = False, indent = 2)
    with open("./totalContent.json", "w+", encoding = "utf-8", errors = "ignore") as f:
        json.dump(totalContent, f, ensure_ascii = False, indent = 2)

