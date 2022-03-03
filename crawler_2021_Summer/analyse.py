import os
import json

file_list = os.listdir("./data")
# print(file_list)

for video in file_list:
    f = open(f"./data/{video}", encoding='utf-8')
    t = json.load(f)
    # print(t['video_title'])
    author_name = t['author_name']
    author_id = t['author_id']
    author_description = t['author_description']
    author_picture = t['author_picture']
    author_follow = t['author_follow']
    video_post = []
    video_title = t['video_title']
    dic = {"video_title": video_title, \
           'video_picture': t['video_picture'], \
           "video_url": t['video_url'],\
           }
    video_post.append(dic)
    diction = {'author_name': author_name,\
               'author_id': author_id,\
               'author_description': author_description,\
               'author_picture': author_picture,\
               'author_follow': author_follow,\
               'video_post': video_post, }
    if os.path.exists(f'./author/{author_id}.json'):
        print(author_id)
        with open(f'./author/{author_id}.json', "r", encoding='utf-8') as fi:
            ti = json.load(fi)
            ti['video_post'].append(dic)
            fi.close()
        with open(f'./author/{author_id}.json', "w+", encoding='utf-8') as fi:
            json.dump(ti, fi, ensure_ascii=False, indent=2)
            print(ti['video_post'])
            fi.close()
    else:
        fi = open(f'./author/{author_id}.json', 'w+', encoding='utf-8')
        json.dump(diction, fi, ensure_ascii=False, indent=2)
        fi.close()
    f.close()
