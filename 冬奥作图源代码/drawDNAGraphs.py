from pickle import TRUE
import xlwings as xw
import matplotlib.pyplot as plt
import matplotlib
from tqdm import tqdm
import functools
plt.rcParams['font.sans-serif']=['SimHei']  #显示中文
import time
import json
import os
from collections import Counter
from IPython import embed
import random
import datetime as dt
# 全局变量,需要讨论的词汇
sports = ["卓球","体操","エアリアル","フリースキー","ビッグエア","ペア","飛込","バドミントン","射撃"]
sportsManSummer = ["孫穎莎","蘇炳添","許昕","劉詩雯","孫亜楠","肖若騰",]
sportsManWinter = ["谷愛凌","蘇毅鳴","任子威","武大靖","韓聡"]
political = ["中国","台湾","香港","ヴィグール","コロナ","共産党","人権問題","独裁"]
allObjects = [sports,sportsManSummer,sportsManWinter,political]
nameObjets = ["运动(日文)","夏季运动员(日文)","冬季运动员(日文)","政治相关(日文)"]

# 中文相关词汇
sportsChina=["乒乓球","体操","自由滑","大跳台","花滑","跳水","羽毛球","射击"]
sportsManSummerChina = ["孙颖莎","苏炳添","许昕","刘诗雯","孙亚楠","肖若腾"]
sportsManWinterChina = ["谷爱凌","苏毅鸣","任子威","武大靖","韩聪"]
allObjectsChina = [sportsChina,sportsManSummerChina,sportsManWinterChina]
nameObjetsChina=["运动(中文)","夏季运动(中文)","冬季运动(中文)"]
yearPoint = [20210705,20210710,20210715,20210720,20210725,20210730,20210801,20210805,20210810,20210815,20210820,20210825,20210830,20210901,20211001,20211101,20211201,20220101,20220105,20220110,20220115,20220120,20220125,20220130,20220201,20220205,20220210,20220215,20220220,20220225,20220301]

showData = []


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


def findSection(day,dayList):
    for i in range(0,len(dayList)):
        if(day == dayList[i]):
            return i
    return random(range(0,len(dayList)))


def draw(i, tempJson):
    numOfObjects = len(tempJson)
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    for j in range(0,len(tempJson)):
        
        if(tempJson[j] == None):
            numOfObjects -= 1
            continue
        max = 0
        for key in tempJson[j]:
            if tempJson[j][key] > max:
                max = tempJson[j][key]
        for key in tempJson[j]:
            validFrequency = tempJson[j][key]
            posiX = findSection(int(key), yearPoint) / 2.5
            posiXAll = []
            for k in range(0, 7):
                posiXAll.append((findSection(yearPoint[5 *k],yearPoint)) / 2.5)
            plt.xticks(posiXAll, showData)
            rect = plt.Rectangle((posiX, 2 + 3.0 * (numOfObjects - j)), 0.6, 0.8, color='#00CED1', alpha\
                = validFrequency / max)
            ax1.add_patch(rect)
    posiYAll = []
    for j in range(0,len(tempJson)):
        posiYAll.append(2 + 3 * (numOfObjects - j))
    plt.yticks(posiYAll, allObjects[i], fontsize=7)
    plt.xlim(0, 12)
    plt.ylim(0, 4 * numOfObjects)
    titleName = nameObjets[i] + "报道趋势图"
    plt.title(titleName)
    plt.savefig(r"C:\Users\liuy\Desktop\DNA图片" + "\\" + titleName + ".png")


if __name__ == '__main__':
    for i in range(0, 7):
        showData.append(
            str(yearPoint[5 * i] // 10000) + str(".") + str(yearPoint[5 * i] % 10000 // 100) + str('.') + str(yearPoint[5 * i] % 100))
    for i in tqdm(range(0,len(nameObjets))):
        addNamePosi = r"C:\Users\liuy\Desktop\workFlow\重点词词频（中文）" + "\\" + nameObjets[i] + ".json"
        with open(addNamePosi,"r",encoding="utf8",errors = "ignore") as f:
            tempJson = json.load(f)
            draw(i,tempJson)