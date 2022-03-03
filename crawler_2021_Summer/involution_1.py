import os
import json

school_list = {"pku", "thu", "sjtu", "fdu", "zju", "ruc"}
pku = ["北大", "北京大学", "pku", "PKU", "贫困大学", "p大"]
thu = ["清华", "清华大学", "thu", "THU", "t大"]
sjtu = ["上交", "上海交通大学", "上海脚痛大学", "脚痛大学", "sjtu"]
fdu = ["复旦", "复旦大学", "复日大学", "fdu", "五角场魔法学院"]
zju = ["浙大", "浙江大学", "zju"]
ruc = ["人大", "中国人民大学", "人民大学", "ruc"]
pku_data = [0, 0]
thu_data = [0, 0]
sjtu_data = [0, 0]
fdu_data = [0, 0]
zju_data = [0, 0]
ruc_data = [0, 0]
pku_list = []
thu_list = []
fdu_list = []
zju_list = []
ruc_list = []
sjtu_list = []

file_list = os.listdir("./data")
for video in file_list:
    x = 0
    belong = ''
    with open(f"./data/{video}", "r", encoding='utf-8') as f:
        t = json.load(f)

        for index in pku:
            if (index in t["video_title"]) or (index in t["video_description"]) or (index in t["author_description"]) \
                    or (index in t["author_name"]):
                x += 1
                belong = "pku"

                # 不考虑reply是因为reply里面可能同时出现多个学校的名字，而视频内容往往反应的是一个学校的内卷
        for index in thu:
            if (index in t["video_title"]) or (index in t["video_description"]) or (index in t["author_description"]) \
                    or (index in t["author_name"]):
                x += 1
                belong = "thu"

        for index in sjtu:
            if (index in t["video_title"]) or (index in t["video_description"]) or (index in t["author_description"]) \
                    or (index in t["author_name"]):
                x += 1
                belong = "sjtu"

        for index in fdu:
            if (index in t["video_title"]) or (index in t["video_description"]) or (index in t["author_description"]) \
                    or (index in t["author_name"]):
                x += 1
                belong = "fdu"

        for index in zju:
            if (index in t["video_title"]) or (index in t["video_description"]) or (index in t["author_description"]) \
                    or (index in t["author_name"]):
                x += 1
                belong = "zju"

        for index in ruc:
            if (index in t["video_title"]) or (index in t["video_description"]) or (index in t["author_description"]) \
                    or (index in t["author_name"]):
                x += 1
                belong = "ruc"

        if x == 1:
            if belong == "pku":
                pku_data[0] += 1
                pku_list.append(video)
            if belong == "thu":
                thu_data[0] += 1
                thu_list.append(video)
            if belong == "fdu":
                fdu_data[0] += 1
                fdu_list.append(video)
            if belong == "sjtu":
                sjtu_data[0] += 1
                sjtu_list.append(video)
            if belong == "zju":
                zju_data[0] += 1
                zju_list.append(video)
            if belong == "ruc":
                ruc_data[0] += 1
                ruc_list.append(video)

        x = 0
        belong = ""

dic = {"thu": thu_list, "thu_data": thu_data[0], "pku": pku_list, "pku_data": pku_data[0], "sjtu": sjtu_list,
       "sjtu_data": sjtu_data[0], \
       "fdu": fdu_list, "fdu_data": fdu_data[0], "zju": zju_list, "zju_data": zju_data[0], "ruc": ruc_list,
       "ruc_data": ruc_data[0], }

with open(f'./school.json', 'w+', encoding='utf-8') as f:
    json.dump(dic, f, ensure_ascii=False, indent=2)
