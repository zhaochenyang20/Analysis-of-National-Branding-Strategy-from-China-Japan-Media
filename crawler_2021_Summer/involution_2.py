import os
import json

involution_list = ["卷王", "车神", "内卷", "卷怪", "卷"]
thu_involution_list = []
pku_involution_list = []
sjtu_involution_list = []
fdu_involution_list = []
zju_involution_list = []
ruc_involution_list = []

with open("./school.json", encoding="utf-8") as t:
    file = json.load(t)
    for each_video in file["thu"]:
        x = 0
        print(each_video)
        with open(f"./data/{each_video}", encoding="utf-8") as ti:
            info_list = []
            video = json.load(ti)
            print(video)
            info_list.append(video["video_title"])
            info_list.append(video["video_description"])
            info_list.extend(video["reply"])
            info_list.append(video["author_name"])
            info_list.append(video["author_description"])
            for each_word in involution_list:
                for each_info in info_list:
                    if each_word in each_info:
                        if x == 0:
                            thu_involution_list.append(each_video)
                        x += 1

    for each_video in file["pku"]:
        x = 0
        print(each_video)
        with open(f"./data/{each_video}", encoding="utf-8") as ti:
            info_list = []
            video = json.load(ti)
            print(video)
            info_list.append(video["video_title"])
            info_list.append(video["video_description"])
            info_list.extend(video["reply"])
            info_list.append(video["author_name"])
            info_list.append(video["author_description"])
            for each_word in involution_list:
                for each_info in info_list:
                    if each_word in each_info:
                        if x == 0:
                            pku_involution_list.append(each_video)
                        x += 1

    for each_video in file["pku"]:
        x = 0
        print(each_video)
        with open(f"./data/{each_video}", encoding="utf-8") as ti:
            info_list = []
            video = json.load(ti)
            print(video)
            info_list.append(video["video_title"])
            info_list.append(video["video_description"])
            info_list.extend(video["reply"])
            info_list.append(video["author_name"])
            info_list.append(video["author_description"])
            for each_word in involution_list:
                for each_info in info_list:
                    if each_word in each_info:
                        if x == 0:
                            pku_involution_list.append(each_video)
                        x += 1

    for each_video in file["fdu"]:
        x = 0
        print(each_video)
        with open(f"./data/{each_video}", encoding="utf-8") as ti:
            info_list = []
            video = json.load(ti)
            print(video)
            info_list.append(video["video_title"])
            info_list.append(video["video_description"])
            info_list.extend(video["reply"])
            info_list.append(video["author_name"])
            info_list.append(video["author_description"])
            for each_word in involution_list:
                for each_info in info_list:
                    if each_word in each_info:
                        if x == 0:
                            fdu_involution_list.append(each_video)
                        x += 1

    for each_video in file["sjtu"]:
        x = 0
        print(each_video)
        with open(f"./data/{each_video}", encoding="utf-8") as ti:
            info_list = []
            video = json.load(ti)
            print(video)
            info_list.append(video["video_title"])
            info_list.append(video["video_description"])
            info_list.extend(video["reply"])
            info_list.append(video["author_name"])
            info_list.append(video["author_description"])
            for each_word in involution_list:
                for each_info in info_list:
                    if each_word in each_info:
                        if x == 0:
                            sjtu_involution_list.append(each_video)
                        x += 1

    for each_video in file["zju"]:
        x = 0
        print(each_video)
        with open(f"./data/{each_video}", encoding="utf-8") as ti:
            info_list = []
            video = json.load(ti)
            print(video)
            info_list.append(video["video_title"])
            info_list.append(video["video_description"])
            info_list.extend(video["reply"])
            info_list.append(video["author_name"])
            info_list.append(video["author_description"])
            for each_word in involution_list:
                for each_info in info_list:
                    if each_word in each_info:
                        if x == 0:
                            zju_involution_list.append(each_video)
                        x += 1

    for each_video in file["ruc"]:
        x = 0
        print(each_video)
        with open(f"./data/{each_video}", encoding="utf-8") as ti:
            info_list = []
            video = json.load(ti)
            print(video)
            info_list.append(video["video_title"])
            info_list.append(video["video_description"])
            info_list.extend(video["reply"])
            info_list.append(video["author_name"])
            info_list.append(video["author_description"])
            for each_word in involution_list:
                for each_info in info_list:
                    if each_word in each_info:
                        if x == 0:
                            ruc_involution_list.append(each_video)
                        x += 1

zju_num = len(zju_involution_list)
fdu_num = len(fdu_involution_list)
thu_num = len(thu_involution_list)
pku_num = len(pku_involution_list)
sjtu_num = len(sjtu_involution_list)
ruc_num = len(ruc_involution_list)

dic = {"zju_involution_list": zju_involution_list, "zju_num": zju_num, "fdu_involution_list": fdu_involution_list,
       "fdu_num": fdu_num, "thu_involution_list": thu_involution_list, "thu_num": thu_num, "pku_involution_list":
           pku_involution_list, "pku_num": pku_num, "sjtu_involution_list": sjtu_involution_list, "sjtu_num": sjtu_num,
       "ruc_involution_list": ruc_involution_list, "ruc_num": ruc_num, }

print(dic)

school_list = open(f'./school_involution_result.json', 'w+', encoding='utf-8')
json.dump(dic, school_list, ensure_ascii=False, indent=2)
