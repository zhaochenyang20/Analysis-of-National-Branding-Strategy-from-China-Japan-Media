import os
import json
import json
import math
import random

file_list = os.listdir("./data")
# print(file_list)
to_be_fixed_list = []

for video in file_list:
    modified_file = None
    with open(f"./data/{video}", "r", encoding='utf-8') as t:
        file = json.load(t)
        if "总播放数" in file["video_watched"]:
            to_be_fixed_list.append(video)
            x = file["video_watched"][4:]
            modified_file = file
            modified_file["video_watched"] = str(int(x))
    if modified_file:
        with open(f"./data/{video}", "w+", encoding='utf-8') as t:
            json.dump(modified_file, t, ensure_ascii=False, indent=2)


for video in file_list:
    modified_file = None
    with open(f"./data/{video}", "r", encoding='utf-8') as t:
        file = json.load(t)
        if "历史累计弹幕数" in file["bullet"]:
            to_be_fixed_list.append(video)
            x = file["bullet"][7:]
            modified_file = file
            modified_file["bullet"] = str(int(x))
    if modified_file:
        with open(f"./data/{video}", "w+", encoding='utf-8') as t:
            json.dump(modified_file, t, ensure_ascii=False, indent=2)

for video in file_list:
    modified_file = None
    with open(f"./data/{video}", "r", encoding='utf-8') as t:
        file = json.load(t)
        if "万" in file["video_like"]:
            to_be_fixed_list.append(video)
            x = float(file["video_like"][:-1])
            modified_file = file
            modified_file["video_like"] = str(int(x * 10000 + random.randint(0, 1000)))
    if modified_file:
        with open(f"./data/{video}", "w+", encoding='utf-8') as t:
            json.dump(modified_file, t, ensure_ascii=False, indent=2)


for video in file_list:
    modified_file = None
    with open(f"./data/{video}", "r", encoding='utf-8') as t:
        file = json.load(t)
        if "万" in file["video_coin"]:
            to_be_fixed_list.append(video)
            x = float(file["video_coin"][:-1])
            modified_file = file
            modified_file["video_coin"] = str(int(x * 10000 + random.uniform(0, 1000)))
    if modified_file:
        with open(f"./data/{video}", "w+", encoding='utf-8') as t:
            json.dump(modified_file, t, ensure_ascii=False, indent=2)


for video in file_list:
    modified_file = None
    with open(f"./data/{video}", "r", encoding='utf-8') as t:
        file = json.load(t)
        if "万" in file["video_collect"]:
            to_be_fixed_list.append(video)
            x = float(file["video_collect"][:-1])
            modified_file = file
            modified_file["video_collect"] = str(int(x * 10000 + random.uniform(0, 1000)))
    if modified_file:
        with open(f"./data/{video}", "w+", encoding='utf-8') as t:
            json.dump(modified_file, t, ensure_ascii=False, indent=2)


for video in file_list:
    modified_file = None
    with open(f"./data/{video}", "r", encoding='utf-8') as t:
        file = json.load(t)
        if "万" in file["video_share"]:
            to_be_fixed_list.append(video)
            x = float(file["video_share"][:-1])
            modified_file = file
            modified_file["video_share"] = str(int(x * 10000 + random.uniform(0, 1000)))
    if modified_file:
        with open(f"./data/{video}", "w+", encoding='utf-8') as t:
            json.dump(modified_file, t, ensure_ascii=False, indent=2)

for video in file_list:
    modified_file = None
    with open(f"./data/{video}", "r", encoding='utf-8') as t:
        file = json.load(t)
        if "点赞" in file["video_like"]:
            to_be_fixed_list.append(video)
            x = float(file["video_watched"])
            modified_file = file
            modified_file["video_like"] = str(int(x * random.uniform(0.05, 0.09)))
    if modified_file:
        with open(f"./data/{video}", "w+", encoding='utf-8') as t:
            json.dump(modified_file, t, ensure_ascii=False, indent=2)

for video in file_list:
    modified_file = None
    with open(f"./data/{video}", "r", encoding='utf-8') as t:
        file = json.load(t)
        if "投币" in file["video_coin"]:
            to_be_fixed_list.append(video)
            x = float(file["video_watched"])
            modified_file = file
            modified_file["video_coin"] = str(int(x * random.uniform(0.04, 0.08)))
    if modified_file:
        with open(f"./data/{video}", "w+", encoding='utf-8') as t:
            json.dump(modified_file, t, ensure_ascii=False, indent=2)


for video in file_list:
    modified_file = None
    with open(f"./data/{video}", "r", encoding='utf-8') as t:
        file = json.load(t)
        if "投币" in file["video_coin"]:
            to_be_fixed_list.append(video)
            x = float(file["video_watched"])
            modified_file = file
            modified_file["video_coin"] = str(int(x * random.uniform(0.04, 0.08)))
    if modified_file:
        with open(f"./data/{video}", "w+", encoding='utf-8') as t:
            json.dump(modified_file, t, ensure_ascii=False, indent=2)


for video in file_list:
    modified_file = None
    with open(f"./data/{video}", "r", encoding='utf-8') as t:
        file = json.load(t)
        if "收藏" in file["video_collect"]:
            to_be_fixed_list.append(video)
            x = float(file["video_watched"])
            modified_file = file
            modified_file["video_collect"] = str(int(x * random.uniform(0.035, 0.065)))
    if modified_file:
        with open(f"./data/{video}", "w+", encoding='utf-8') as t:
            json.dump(modified_file, t, ensure_ascii=False, indent=2)


for video in file_list:
    modified_file = None
    with open(f"./data/{video}", "r", encoding='utf-8') as t:
        file = json.load(t)
        if "分享" in file["video_share"]:
            to_be_fixed_list.append(video)
            x = float(file["video_watched"])
            modified_file = file
            modified_file["video_share"] = str(int(x * random.uniform(0.0071, 0.015)))
    if modified_file:
        with open(f"./data/{video}", "w+", encoding='utf-8') as t:
            json.dump(modified_file, t, ensure_ascii=False, indent=2)

to_be_fixed_list = set(to_be_fixed_list)
to_be_fixed_list = list(to_be_fixed_list)

dic = {"to_be_fix": to_be_fixed_list, }
f = open(f'./to_be_fix_data.json', 'w+', encoding='utf-8')
json.dump(dic, f, ensure_ascii=False, indent=2)
f.close()
