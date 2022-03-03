from pickle import TRUE         #二进制序列文本
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

# 全局变量,需要讨论的词汇
sports = ["卓球","体操","エアリアル","フリースキー","ビッグエア","ペア","飛込","バドミントン","射撃"]
sportsManSummer = ["孫穎莎","蘇炳添","許昕","劉詩雯","孫亜楠","肖若騰",]
sportsManWinter = ["谷愛凌","蘇毅鳴","任子威","武大靖","韓聡"]
political = ["中国","台湾","香港","ウイグル","コロナ","共産党","人権問題","独裁"]
allObjects = [sports,sportsManSummer,sportsManWinter,political]
nameObjets = ["运动(日文)","夏季运动员(日文)","冬季运动员(日文)","政治相关(日文)"]



# 中文相关词汇
sportsChina=["乒乓球","体操","自由滑","大跳台","花滑","跳水","羽毛球","射击"]
sportsManSummerChina = ["孙颖莎","苏炳添","许昕","刘诗雯","孙亚楠","肖若腾"]
sportsManWinterChina = ["谷爱凌","苏毅鸣","任子威","武大靖","韩聪"]
allObjectsChina = [sportsChina,sportsManSummerChina,sportsManWinterChina]
nameObjetsChina=["运动(中文)","夏季运动(中文)","冬季运动(中文)"]
yearPoint = [20210705,20210710,20210715,20210720,20210725,20210730,20210801,20210805,20210810,20210815,20210820,20210825,20210830,20210901,20211001,20211101,20211201,20220101,20220105,20220110,20220115,20220120,20220125,20220130,20220201,20220205,20220210,20220215,20220220,20220225,20220301]


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


def findSection(day,dayList):
    if day < dayList[0]:
        return -1
    for i in range(0,len(dayList)):
        if(day < dayList[i]):
            return i - 1
    return len(dayList) - 1


@metric
def getSectionTimes(typeList,fileList):
    ans = []
    for i in range(0,len(typeList)):
        eachDict = Counter()
        ans.append(eachDict)
    for i in tqdm(range(0,len(typeList))):
        for fileEach in tqdm(fileList):
            with open(fileEach,"r",encoding = 'utf-8',errors = 'ignore') as f:
                getJsonEach = json.load(f)
                num = count_find_str(getJsonEach["content"],typeList[i])
                day = 0 
                if num == 0:
                    continue
                else:
                    try:
                        day = getJsonEach["date"]
                    except Exception as e:
                        try:
                            day = getJsonEach["time"]
                        except Exception as e:
                            pass
                    pass
                if day == None:
                    continue
                index = findSection(day,yearPoint)
                if index == -1:
                    continue
                else:
                    try:
                        ans[i][yearPoint[index]] += num
                    except Exception as e:
                        pass
    return ans


@metric
def get_list(target):
    dirs = os.listdir(target)
    fileList = []
    for file in dirs:
         fileList.append(f"{target}/{file}")
    return fileList


@metric
def getTime(fileList):
    listTime = []
    for fileEach in tqdm(fileList):
        with open(fileEach,"r",encoding="utf8",errors="ignore") as f:
            dicJsonEach = json.load(f)
            try:
                if not listTime.count(dicJsonEach["time"]):
                    if dicJsonEach["time"] != None:
                        listTime.append(dicJsonEach["time"])
                else:
                    pass
            except Exception as e:
                try:
                    if not listTime.count(dicJsonEach["date"]):
                        if dicJsonEach["date"] != None:
                            listTime.append(dicJsonEach["date"])
                    else:
                        pass
                except Exception as e:
                    print(e)
                    print(dicJsonEach)
    listTime.sort()
    return listTime



if __name__ == "__main__":
    
    # listOrderedTime = getTime(get_list("C:/Users/liuy/Desktop/Results"))
    # 时间区间从 2021 年 7 月 -- 2022 年 2 月 28 日
    allList = get_list("C:/Users/liuy/Desktop/日语新闻")
    # Frequency = getSectionTimes(sports,allList)
    for i in tqdm(range(0,len(allObjects))):
        tempDict = getSectionTimes(allObjects[i],allList)
        with open("./重点词词频（中文）/" + nameObjets[i] + ".json","w+",encoding = "utf8",errors = "ignore") as f:
            json.dump(tempDict,f,ensure_ascii = False, indent = 2)
