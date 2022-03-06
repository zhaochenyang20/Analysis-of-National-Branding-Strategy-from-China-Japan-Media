from pickle import TRUE
from sympy import ordered         #二进制序列文本
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
from IPython import embed
# 全局变量，方便修改
startListIndex = [3,3,5,3]
strcolumnSheet3 = ['A','C','E','G','I','K','M','O','Q','S','U','W','Y','AA','AC','AE','AG','AJ']
# strcolumnSheet3 = ['K','M','O','Q']

strcolumnSheet2 = ['A','B','C','D','E','G','H','I','J']
strcolumnSheet1 = ['A','B','C','D','F','G','H']
strcolumnSheet4 = ['A','C','E','G','K']
nameSheet = ["夏奥","冬奥","情感色彩","隐喻分类"]
strColumnPosi = [strcolumnSheet1, strcolumnSheet2, strcolumnSheet3, strcolumnSheet4]

# 一些颜色列表
colorsFoxconn = ['#FEE9CE','#F5D0C7','#BEB2BE','#6A909D','#A8C4E9','#DCEDFD']
colorsPurple = ['#EB7981','#855680','#70618C','#7289A9','#9CBDC4']
colorsFresh = ['#85CBCC','#98D556','#ABDEE0','#D2E0C7','#F9E2AE','#FAD51D','#FBC78D','#D1CF01','#A7D676']

colorsGrass = ['#DCEADB','#9EC6A4','#80B28F','#A2BF87','#698FCD','#749CB5']
colorsElegant = ['#FA9083','#F9BA77','#FDB6B5','#D1A9DE','#FCB4C8','#CFC0EC','#F1D5EE']
colorsBright = ['#6E61AF','#A2C0DC','#15C8CC','#78CCFC','#1AD6E2','#E2C8F8','#EEDDDF']

colorsWarm = ['#E09E09','#B27A63','#DCA77B','#BD6C41','#C1B585','#F0DEAF']
colorsLightPurple = ['#3B5798','#7CA4C8','#B6B2CD','#D8ADC5','#9D6886']
colorsSkyAndGrass = ['#BEB8AA','#EADDBB','#97B2AF','#9AADBB','#7C9FB2','#A2A04B','#CFC382']

app = xw.App(visible=True, add_book=False)  #增加可视化，不添加新文件
app.display_alerts = False                  #展示警报解除
app.screen_updating = True                  #显示屏幕刷新
posi=(r"C:\Users\liuy\Desktop\workFlow\Scanner.xlsx")
wb = app.books.open(posi)  

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('\n start executing %s' % (fn.__name__))
        start_time = time.time()
        result = fn(*args, **kw)
        end_time = time.time()
        t = 1000 * (end_time - start_time)
        print('%s executed in %s ms' % (fn.__name__, t))
        return result
    return wrapper


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

def getListOfExcel(j):

    shtNew = wb.sheets[nameSheet[j]]
    dirLanguage=[]
    startIndex = startListIndex[j]
    strcolumnSheetTemp = strColumnPosi[j]
    for i in range(len(strcolumnSheetTemp)):
        temp = strcolumnSheetTemp[i]
        temp += str(startIndex)
        a = []
        b = shtNew.range(temp).value
        while b != None:
            a.append(b)
            startIndex +=1 
            temp = strcolumnSheetTemp[i]
            temp += str(startIndex)
            b = shtNew.range(temp).value
        dirLanguage.append(a)
        startIndex = startListIndex[j]
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
    lists = []
    hot = False
    for i in range(0,len(dirLanguage)):
        dict = Counter()
        lists.append(dict)
    for file in tqdm(file_list):
        with open(file,"r",encoding="utf-8",errors="ignore") as f:
            try:
                getTitle = json.load(f)["title"]
                for i in range(0,len(dirLanguage)):
                    for word in dirLanguage[i]:
                        lists[i][word] += count_find_str(getTitle,word)
                hot = True
            except Exception as e:
                try:
                    getContent = json.load(f)["Title"]
                    for i in range(0,len(dirLanguage)):
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
    for i in range(0,len(dirLanguage)):
        dict = Counter()
        lists.append(dict)
    for file in tqdm(file_list):
        with open(file,"r",encoding="utf-8",errors="ignore") as f:
            try:
                getContent = json.load(f)["content"]
                for i in range(0,len(dirLanguage)):
                    for word in dirLanguage[i]:
                        lists[i][word] += count_find_str(getContent,word)
                hot = True
            except Exception as e:
                try:
                    getContent = json.load(f)["context"]
                    for i in range(0,len(dirLanguage)):
                        for word in dirLanguage[i]:
                            lists[i][word] += count_find_str(getContent,word)
                    hot = True
                except:
                    try:
                        getContent = json.load(f)["contents"]
                        for i in range(0,len(dirLanguage)):
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


def get_rank(dictions):
    lists=[]
    for diction in tqdm(dictions):
        newDictions = sorted(diction.items(),key=lambda x:x[1],reverse=True)
        lists.append(newDictions)
    return lists

def getTotalTimes(dictions):
    total = []
    for diction in tqdm(dictions):
        total.append(sum(diction.values()))
    return total

@metric
def drawPieGraphs(list1,list2,title):
    if list1 == None:
        return None
    plt.rcParams['font.sans-serif']='SimHei'#设置中文显示
    plt.figure(figsize=(6,6))#将画布设定为正方形，则绘制的饼图是正圆
    explode = []
    for i in range(len(list1)):
        explode.append(0.01)
    try:
        plt.pie(list2,explode=explode,labels=list1,autopct='%1.1f%%',shadow = True,colors = colorsFoxconn)
        plt.title(title)
        posiGraph = r"C:\Users\liuy\Desktop\图表\\"
        posiGraph += str(title)
        plt.savefig(posiGraph,dpi = 200)
    except:
        pass

@metric
def getTwoLists(totalNumberList,orderedList,i):
    tempTotal = totalNumberList[i]
    tempList = orderedList[i]
    length = len(tempList) - 1
    if length < 0:
        return [1],[1]
    others = tempList[length][1] 
    while(others < tempTotal * 0.05):
        length -= 1
        others += tempList[length][1] 
    list1 = []
    list2 = []
    if length > 3 or len(tempList) > 6:
        for i in range(length):
            list1.append(tempList[i][0])
            list2.append(tempList[i][1])
        list1.append('其他')
        list2.append(others - tempList[length][1])
        return list1, list2
    elif length > 18:
        for i in range(0,10):
            list1.append(tempList[i][0])
            list2.append(tempList[i][1])
            list1.append('其他')
            list2.append(sum(list2)/len(list2) / 1.5)
        return list1,list2
    else:
        for i in range(len(tempList)):
            list1.append(tempList[i][0])
            list2.append(tempList[i][1])
        return list1,list2


if __name__ == '__main__':
    for j in range(0,4):
        dir = getListOfExcel(j)
        title_number = getNumbersOfTitle(get_list("C:/Users/liuy/Desktop/中文新闻"),dir)
        content_number = getNumbersOfContents(get_list("C:/Users/liuy/Desktop/中文新闻"),dir)
        # title_number = getNumbersOfTitle(get_list("C:/Users/liuy/Desktop/日语新闻"),dir)
        # content_number = getNumbersOfContents(get_list("C:    /Users/liuy/Desktop/日语新闻"),dir)
        orderedTitle = get_rank(title_number)
        orderedContent = get_rank(content_number)
        totalTitle = getTotalTimes(title_number)
        totalContent = getTotalTimes(content_number)
        
	# 生成标题的图表
        # for i in tqdm(range(0, len(totalTitle))):
        #     sht = wb.sheets[nameSheet[j]]
        #     temp = strColumnPosi[j][i]
        #     temp += str(startListIndex[j] - 1)
        #     tempTitle = sht.range(temp).value
        #     drawPieGraphs(*getTwoLists(totalTitle, orderedTitle,i),tempTitle)
        
        for i in tqdm(range(0, len(totalContent))):
            sht = wb.sheets[nameSheet[j]]
            temp = strColumnPosi[j][i]
            temp += str(startListIndex[j] - 1)
            tempTitle = sht.range(temp).value
            drawPieGraphs(*getTwoLists(totalContent, orderedContent,i),tempTitle)




 