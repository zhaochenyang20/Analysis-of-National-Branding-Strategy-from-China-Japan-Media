import os
import json

file_list = os.listdir("./author")
for author in file_list:
    f = open(f"./author/{author}", encoding='utf-8')
    t = json.load(f)
    # print(len(t['video_post']))
    if len(t['video_post']) != 1:
        print(author)
    f.close()
