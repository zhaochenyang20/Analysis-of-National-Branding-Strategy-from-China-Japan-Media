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
from IPython import embed
import functools
import os
import time
import json

def count_find_str(str,find_str):

    _str = str
    _find_str = find_str
    _pos = _str.find(_find_str)
    _find_str_count = 0
    while _pos != -1:
        _find_str_count = _find_str_count + 1
        _pos = _pos + len(_find_str)
        _pos = _str.find(_find_str, _pos)
    return _find_str_count

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

def get_list(target):
    dirs = os.listdir(target)
    file_list = []
    for file in dirs:
         file_list.append(f"{target}/{file}")
    return file_list

def getListOfExcel():
    start=5
    strcolumn=['A','C','E','G','I','K','M','O','S','U','W','Y','AA','AC','AE','AG','AJ']


    app = xw.App(visible=True, add_book=False)  #增加可视化，不添加新文件
    app.display_alerts = False                  #展示警报解除
    app.screen_updating = True                  #显示屏幕刷新
    posi=(r"C:\Users\liuy\Desktop\workFlow\Scanner.xlsx")
    wb = app.books.open(posi)                   #打开表格载入至wb中
    sht = wb.sheets['情感色彩']         #载入sheet1
    dirLanguage=[]
    j = 5 
    for i in range(len(strcolumn)):
        temp = strcolumn[i]
        temp += str(j)
        a = []
        b = sht.range(temp).value
        while b != None:
            a.append(b)
            j+=1
            temp=strcolumn[i]
            temp+=str(j)
            b=sht.range(temp).value
        dirLanguage.append(a)
        j=5
    return dirLanguage

def count_find_str(str,find_str):

    _str = str
    _find_str = find_str
    _pos = _str.find(_find_str)
    _find_str_count = 0
    while _pos != -1:
        _find_str_count = _find_str_count + 1
        _pos = _pos + len(_find_str)
        _pos = _str.find(_find_str, _pos)
    return _find_str_count


@metric
def getNumbersOfTitle(file_list,dirLanguage):
    failure = 0
    lists=[]
    hot = False
    for i in range(0,17):
        dict = Counter()
        lists.append(dict)
    for file in tqdm(file_list):
        with open(file,"r",encoding="utf-8",errors="ignore") as f:
            try:
                getTitle = json.load(f)["title"]
                for i in range(0,17):
                    for word in dirLanguage[i]:
                        lists[i][word] += count_find_str(getTitle,word)
                hot = True
            except Exception as e:
                try:
                    getContent = json.load(f)["Title"]
                    for i in range(0,17):
                        for word in dirLanguage[i]:
                            lists[i][word] += count_find_str(getContent,word)
                    hot = True
                except:
                    pass
                if not hot:
                    print(e)
                    print(file)
                    failure += 1
                    print("Reading failed!")
                    continue
    with open("./title_failure.txt", "w+", encoding="utf-8",errors="ignore") as t:
        t.write(str(failure))
    return lists


@metric        
def getNumbersOfContents(file_list,dirLanguage):
    failure = 0
    lists=[]
    hot = False
    for i in range(0,17):
        dict = Counter()
        lists.append(dict)
    for file in tqdm(file_list):
        with open(file,"r",encoding="utf-8",errors="ignore") as f:
            try:
                getContent = json.load(f)["content"]
                for i in range(0,17):
                    for word in dirLanguage[i]:
                        lists[i][word] += count_find_str(getContent,word)
                hot = True
            except Exception as e:
                try:
                    getContent = json.load(f)["context"]
                    for i in range(0,17):
                        for word in dirLanguage[i]:
                            lists[i][word] += count_find_str(getContent,word)
                    hot = True
                except:
                    try:
                        getContent = json.load(f)["contents"]
                        for i in range(0,17):
                            for word in dirLanguage[i]:
                                lists[i][word] += count_find_str(getContent,word)
                        hot = True
                    except:
                        pass
                if not hot:
                    print(e)
                    print(file)
                    print("Reading failed!")
                    failure+=1
                    continue
    with open("./content_failure.txt", "w+", encoding="utf-8",errors="ignore") as t:
        t.write(str(failure))
    return lists


if __name__ == '__main__':
    dir=getListOfExcel()
    dict = {}
    dict["title"] = getNumbersOfTitle(get_list("C:/Users/liuy/Desktop/Results"),dir)
    dict["content"] = getNumbersOfContents(get_list("C:/Users/liuy/Desktop/Results"),dir)
    with open("./results.json", "w+", encoding="utf-8", errors="ignore") as f:
        json.dump(dict, f, ensure_ascii=False, indent=2)