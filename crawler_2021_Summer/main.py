import json

from requests import get, post
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from json import dump
from time import sleep # 如果⽹站要求以很低的频率爬，那么⼤概率会需要sleep


ua = "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"


def get_video(urlr):
    '''1Eg411V7gP'''
    try:
        # print(urlr)
        response = get(urlr, headers={'User-Agent': ua})
        sleep(0.1)
        soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
        # print(soup)
        title = soup.find('h1', class_='video-title').get_text()
        # print(title)
        description = soup.find_all(itemprop="description")[0]['content']
        # print(description)
        url = soup.find_all('meta', itemprop="url")[0]['content']
        # print(url)
        picture_face = soup.find_all(rel="apple-touch-icon")[0]['href']
        # print(picture_face)
        view = soup.find_all('span', class_='view')[0]['title']
        # print(view)
        dm = soup.find_all('span', class_='dm')[0]['title']
        # print(dm)
        try:
            rank = soup.find_all('span', class_='rank')[0].contents[0].strip()
        except:
            rank = ''
        # print(rank)
        time = soup.find_all('div', class_='video-data')[0].contents[2].get_text()
        # print(time)
        like = soup.find_all(class_='like')[0].contents[-1].strip()
        # print(like)
        coin = soup.find_all(class_='coin')[0].contents[-1].strip()
        # print(coin)
        collect = soup.find_all(class_='collect')[0].contents[-1].strip()
        # print(collect)
        share = soup.find_all(class_='share')[0].contents[1].strip()
        # print(share)
        # print(urlr)
        bvid = urlr[33:-12]
        print(bvid)
        reply_source = get(f'http://api.bilibili.com/x/web-interface/view?bvid={bvid}', headers={'User-Agent': ua}).json()
        sleep(0.1)
        print(reply_source)
        i = reply_source['data']['aid']
        print(i)
        reply_source = get(f'http://api.bilibili.com/x/v2/reply/main?type=1&oid={i}&sort=1&ps=5&pn=1&nohot=1', headers={'User-Agent': ua}).json()
        sleep(0.1)
        # print((reply_source))
        reply_list = reply_source['data']['replies'][0:5]
        reply_result = []
        for reply in reply_list:
            reply_result.append(reply['content']['message'])
        print(reply_result)
        author_name = soup.find('a', class_='username').get_text().strip()
        print(author_name)
        author_id = soup.find('a', class_='fa')['href'][21:]
        # print(author_id)
        # author_description = soup.find('div', class_='desc')['title']
        try:
            author_description = soup.find('div', class_='desc')['title']
            print(author_description)
        except:
            author_description = ''
        reply = get(f'http://api.bilibili.com/x/space/acc/info?mid={author_id}', headers={'User-Agent': ua})
        sleep(0.1)
        author_picture = reply.json()['data']['face']
        #print(author_picture)
        author_follow = soup.find('i', class_="van-icon-general_addto_s").next_sibling.next_sibling.get_text()
        print(author_follow)
        if like == "点赞" or coin == "投币" or share == "分享" or collect == "收藏":
            return
        dic = {'video_title': title, "video_description": description, "video_url": url, 'video_picture': picture_face,
               'video_watched': view, "bullet": dm, "video_rank": rank, "post_time": time, "video_like": like, "video_coin":
                   coin, 'video_collect': collect, 'video_share': share, "reply": reply_result, "author_name": author_name,
               'author_id': author_id, "author_description": author_description,
               "author_picture": author_picture, "author_follow": author_follow, }
        print(dic)
        # print(i)
        f = open(f'./collect/{i}.json', 'w+', encoding='utf-8')
        json.dump(dic, f, ensure_ascii=False, indent=2)
        f.close()
    except:
        pass


#get_video('https://www.bilibili.com/video/BV1QJ411s7tw?from=search')


