from decimal import getcontext
import json
from tqdm import tqdm
import os
import typing
import functools
import time
from collections import Counter
import re


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


def extractTimeFromStr(dateStr):
    year = re.findall(r"2?\d{3,3}",dateStr)
    try:
        startYearIndex = dateStr.find(year[0]) + len(year[0])
    except Exception as e:
        print(dateStr)
        return None
    formerDate = dateStr[startYearIndex:]
    month = re.findall(r"\d{1,2}",formerDate)
    try:
        startMonthIndex = formerDate.find(month[0]) + len(month[0])
    except Exception as e:
        print(dateStr)
        return year[0]
    formerFormerDate = formerDate[startMonthIndex:]
    day = re.findall(r"\d{1,2}",formerFormerDate)
    return int(year[0]) * 10000 + int(month[0]) * 100 + int(day[0])


def get_list(target):
    dirs = os.listdir(target)
    file_list = []
    for file in dirs:
         file_list.append(f"{target}/{file}")
    return file_list


def fixJson(file_list):
    hot = False
    failure = 0
    for file in tqdm(file_list):
        fixedJson = {}
        with open(file, 'r',encoding='utf-8',errors="ignore") as f:
            try:
                getDiction = json.load(f)
            except Exception as e:
                print(e)
                print(file)
                pass

            try:
                getTitle = getDiction["Title"]
                fixedJson["title"] = getTitle
                hot = True
            except Exception as e:
                try:
                    getTitle = getDiction["title"]
                    fixedJson["title"] = getTitle
                    hot = True
                except Exception as e:
                    pass
                if not hot:
                    print(e)
                    print(file_list)
                    print("ReadingTitle failed")

            hot = False     
            try:
                getContent = getDiction["context"]
                fixedJson["content"] = getContent
                hot = True
            except Exception as e:
                try:
                    getContent = getDiction["content"]
                    fixedJson["content"] = getContent
                    hot = True
                except Exception as e:
                    try:
                        getContent = getDiction["contents"]
                        fixedJson["content"] = getContent
                        hot = True
                    except Exception as e:
                        pass
                if not hot:
                    print(e)
                    print(file_list)
                    print("ReadingContent failed")
                
            try:
                getAuthor = getDiction["author"]
                fixedJson["author"] = getAuthor
            except Exception as e:
                pass

            
            hot = False
            try:
                getTime = getDiction["date"]
                fixedJson["date"] = extractTimeFromStr(getTime)
                hot = True
            except Exception as e:
                try:
                    getTime = getDiction["info"]
                    fixedJson["date"] = extractTimeFromStr(getTime)
                    hot = True
                except:
                    pass
                if not hot:
                    print(e)
                    print("ReadingDate failed!")
                    failure += 1

            if not hot:
                try:
                    if fixedJson["date"] != None:
                        if fixedJson["date"] < 20100000 or fixedJson["date"] > 202220227:
                            failure += 1
                except Exception as e:
                    pass

        with open("./date_failure_extract.txt", "w+", encoding="utf-8",errors="ignore") as t:
            t.write(str(failure))

        with open(file,"w+",encoding = 'utf-8',errors = 'ignore') as t:
            json.dump(fixedJson,t,ensure_ascii = False,indent = 2)


if __name__ == '__main__':
    resultPosi = "C:/Users/liuy/Desktop/Results"
    fixJson(get_list(resultPosi))