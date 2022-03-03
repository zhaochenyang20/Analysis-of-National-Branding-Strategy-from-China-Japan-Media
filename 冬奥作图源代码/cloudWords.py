import numpy as np
import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib as mpl
from tqdm import tqdm
from  math import log,sqrt 


def colormap():
  return mpl.colors.LinearSegmentedColormap.from_list('cmap', ["#000080","#6495ED","#778899","#76ACF3","#B588BE"], 256)
getdata =   {
        "杨倩": 510,
        "全红婵": 439,
        "侯志慧": 246,
        "孙一文": 300,
        "廖秋云": 76,
        "陈雨汐": 0,
        "肖若腾": 183,
        "王宗源": 87,
        "谢思扬": 0,
        "苏炳添": 405,
        "孙颖莎": 292,
        "刘诗雯": 143,
        "许昕": 173,
        "马龙": 466,
        "樊振东": 298,
        "王曼昱": 153,
        "昕雯": 19,
        "巩立姣": 239,
        "谌利军": 243,
        "曹缘": 159,
        "施廷懋": 203,
        "陈雨菲": 169,
        "凡尘组合": 12,
        "陈清晨": 80,
        "吕小军": 226,
        "张雨霏": 445,
        "坚持": 2747,
        "精神": 5554,
        "战胜": 940,
        "开门红": 185,
        "梦想": 1556,
        "全力以赴": 378,
        "奋斗": 2912,
        "拼搏": 1562,
        "世界纪录": 554,
        "中日关系": 42,
        "疫情": 6039,
        "竞争": 750,
        "00后": 387,
        "体育健儿": 344,
        "新生": 258,
        "东京奥运会": 4321,
        "奥运会": 12343,
        "比赛": 11354,
        "中国队": 3191,
        "中国代表队": 37,
        "中国体育代表团": 1006,
        "中国射击队": 85,
        "中国跳水队": 120,
        "中国举重队": 123,
        "中国乒乓球队": 100,
        "运动队": 161,
        "梦之队": 128,
        "乒乓球": 1033,
        "女排": 1054,
        "皮划艇": 314,
        "举重": 766,
        "女篮": 460,
        "金牌": 4845,
        "银牌": 1002,
        "成绩": 4373,
        "运动员": 11490,
        "体育": 15373,
        "孫亜楠": 13,
        "全紅嬋": 11,
        "楊倩": 17,
        "侯志慧": 246,
        "孫一文": 1,
        "鄭賽賽": 4,
        "廖秋雲": 0,
        "陳芋汐": 2,
        "肖若騰": 22,
        "孫穎莎": 72,
        "王宗源": 87,
        "謝思扬": 0,
        "張家斉": 0,
        "許昕・許シ": 0,
        "劉詩雯": 25,
        "蘇炳添": 23,
        "トウ亜萍": 1,
        "龐倩玉": 3,
        "羅嘉翎": 0,
        "張家朗": 1,
        "陳雨菲": 11,
        "陳夢": 33,
        "周倩": 27,
        "李洋": 47,
        "王齊麟": 3,
        "金博洋": 237,
        "張博恒": 17,
        "決勝": 4481,
        "偉": 378,
        "輝いた": 405,
        "中国戦": 303,
        "勝利": 804,
        "五輪": 20616,
        "オリンピック": 7742,
        "中国": 22610,
        "選手": 15864,
        "ペア": 785,
        "卓球": 1008,
        "団体": 2670,
        }

def draw_cloud():
    image = Image.open('background.png')  # 作为背景轮廓图
    graph = np.array(image)
    mask=np.array(image)
    # 参数分别是指定字体、背景颜色、最大的词的大小、使用给定图作为背景形状
            # if getdata[key] > 6666:
        #     getdata[key] *= 0.8
        # elif getdata[key] < 200:
        #     getdata[key] *= 10
        # else:
        #     getdata[key] *= 1.2
    for key in getdata:

        getdata[key] = sqrt(sqrt(sqrt(sqrt(getdata[key]) * 666 + 1000) * 100+100) * 100)
        getdata[key] = sqrt(sqrt(sqrt(sqrt(getdata[key]) * 666 + 1000) * 100+100) * 100)
        getdata[key] = sqrt(sqrt(sqrt(sqrt(getdata[key]) * 666 + 1000) * 100+100) * 100)
        getdata[key] = log(getdata[key] + 100)
        getdata[key] = log(getdata[key] + 100)
        getdata[key] = log(getdata[key] + 100)
    # for key in getdata:
    #     getdata[key] = sqrt(sqrt(sqrt(sqrt(getdata[key]) * 666 + 1000) * 100) * 100)
    #     getdata[key] = sqrt(sqrt(sqrt(sqrt(getdata[key]) * 666 + 1000) * 100) * 100)
    #     getdata[key] = sqrt(sqrt(sqrt(sqrt(getdata[key]) * 666 + 1000) * 100) * 100)
    #     getdata[key] = log(getdata[key] + 100)
    #     getdata[key] = log(getdata[key] + 100)
    #     getdata[key] = log(getdata[key] + 100)
    # for key in getdata:
    #     getdata[key] = sqrt(sqrt(sqrt(sqrt(getdata[key]) * 666 + 1000) * 100) * 100)
    #     getdata[key] = sqrt(sqrt(sqrt(sqrt(getdata[key]) * 666 + 1000) * 100) * 100)
    #     getdata[key] = sqrt(sqrt(sqrt(sqrt(getdata[key]) * 666 + 1000) * 100) * 100)
    #     getdata[key] = log(getdata[key] + 100)
    #     getdata[key] = log(getdata[key] + 100)
    #     getdata[key] = log(getdata[key] + 100)
       

    for i in tqdm(range(4)):
        wc = WordCloud(width = 1400,height = 800,collocations=False,margin=2,font_path = 'simkai.ttf', background_color ='white',min_font_size = 0,max_font_size = 2000,mask = mask, max_words = 1000000,colormap = colormap())
        wc.generate_from_frequencies(getdata)  # 根据给定词频生成词云
        image_color = ImageColorGenerator(graph)
        plt.imshow(wc)
        plt.axis("off")  # 不显示坐标轴
        wc.to_file('冰墩墩.png')  # 图片命名
        file = r"C:\Users\liuy\Desktop\成批冰墩墩来啦！~~"
        name = "\冰墩墩" + str(i + 1) + '.png'
        plt.savefig(file + name)


if __name__ == '__main__':
    draw_cloud()