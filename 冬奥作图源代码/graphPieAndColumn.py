from pickle import TRUE         #二进制序列文本
import xlwings as xw
import matplotlib.pyplot as plt
import matplotlib
from tqdm import tqdm
import functools
plt.rcParams['font.sans-serif']=['SimHei']  #显示中文
import time
import json

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


strcolumn = ['A','C','E','G','K']
fileTitle = [r"C:\Users\liuy\Desktop\workFlow\orderedTitle.json",r"C:\Users\liuy\Desktop\workFlow\totalTitle.json"]
fileContent = [r"C:\Users\liuy\Desktop\workFlow\orderedContent.json",r"C:\Users\liuy\Desktop\workFlow\totalContent.json"]

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


@metric
def drawPieGraphs(list1,list2,title):
    if list1 == None:
        return None
    plt.rcParams['font.sans-serif']='SimHei'#设置中文显示
    plt.figure(figsize=(6,6))#将画布设定为正方形，则绘制的饼图是正圆
    explode = []
    for i in range(len(list1)):
        explode.append(0.01)
    plt.pie(list2,explode=explode,labels=list1,autopct='%1.1f%%',shadow = True,colors = colorsFoxconn)
    plt.title(title)
    posiGraph = './饼状图/'
    posiGraph +=str(title)
    plt.savefig(posiGraph)


@metric
def drawColumnGraphs(list1,list2,title):
    plt.rcParams['font.sans-serif']='SimHei'#设置中文显示
    plt.figure(figsize=(10,10))#将画布设定为正方形，则绘制的饼图是正圆
    plt.bar(list1,list2,color = colorsWarm,width = 0.66)
    plt.xticks(list1, list1, rotation = -55)

    plt.title(title)
    posiGraph = './柱状图/'
    posiGraph +=str(title)
    plt.savefig(posiGraph)

@metric
def getTotalTimes(filetype,i):
    with open(filetype[1],'r',encoding='utf-8',errors='ignore') as f:
        try:
            totalLists = json.load(f)
            return int(totalLists[i])
        except Exception as e:
            print(e)
            print("Error get Total times!")

@metric
def getAllLists(filetype):
    with open(filetype[0],'r',encoding='utf-8',errors='ignore') as f:
        return json.load(f)

@metric
def getTwoLists(filetype,allLists,i):
    tempTotal = getTotalTimes(filetype,i)
    tempList = allLists[i]
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
        list1.append('その他')
        list2.append(others - tempList[length][1])
        return list1, list2
    else:
        for i in range(len(tempList)):
            list1.append(tempList[i][0])
            list2.append(tempList[i][1])
        return list1,list2
    


if __name__ == '__main__':
    app = xw.App(visible = True,add_book = False)
    app.display_alerts = False               
    app.screen_updating = True
    posi = (r"C:\Users\liuy\Desktop\workFlow\Scanner.xlsx")
    wb = app.books.open(posi)
    sht = wb.sheets['隐喻分类']
    for i in tqdm(range(len(strcolumn))):
    # for i in range(0,1):
        temp = strcolumn[i]
        temp += str(2)
        print(sht.range(temp).value)
        temptitle = sht.range(temp).value
        objectProcess = fileContent
        drawPieGraphs(*getTwoLists(objectProcess,getAllLists(objectProcess),i),temptitle)
    # drawPieGraphs(["竞技运动相关性较高","竞技运动相关性较低","含褒贬义名词"],[239663,183732,23711],"名词")
    # Str = []
    # Num = []
    # warGraph =[[
    #   "競技",
    #   7047
    # ],
    # [
    #   "決勝",
    #   4481
    # ],
    # [
    #   "試合",
    #   4443
    # ],
    # [
    #   "獲得",
    #   3799
    # ],
    # [
    #   "優勝",
    #   2440
    # ],
    # [
    #   "予選",
    #   2263
    # ],
    # [
    #   "応援",
    #   1363
    # ],
    # [
    #   "連覇",
    #   1217
    # ],
    # [
    #   "壁",
    #   1199
    # ],
    # [
    #   "挑戦",
    #   1142
    # ],
    # [
    #   "進出",
    #   1138
    # ],
    # [
    #   "準決勝",
    #   1036
    # ],
    # [
    #   "攻撃",
    #   978
    # ],
    # [
    #   "負け",
    #   962
    # ],
    # ["その他",1111]
    # ]
    

    # for i in range(0,len(warGraph)):
    #     Str.append(warGraph[i][0])
    #     Num.append(warGraph[i][1])
    # drawPieGraphs(Str,Num,"战争类")