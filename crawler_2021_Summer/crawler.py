import json
import main
from requests import get, post
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from json import dump
from time import sleep # 如果⽹站要求以很低的频率爬，那么⼤概率会需要sleep
index = 0


ua = "Mozilla/5.0 (compatible; Baiduspider/2.0; + http://www.baidu.com/search/spider.html)"


for page in range(1, 51):
    response = get(f'https://search.bilibili.com/all?keyword=%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6&order=totalrank&duration=4&tids_1=0&page={page}',
                   headers={'User-Agent': ua})
    sleep(2)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    lis = soup.find_all('a', class_="title")
    BVList = []
    for element in lis:
        BVList.append('https:' + element['href'])
        print(element['href'])
    for url in BVList:
        main.get_video(url)
        index += 1
        print(index)


for page in range(1, 51):
   response = get(f'https://search.bilibili.com/all?keyword=%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6&order=totalrank&duration=3&tids_1=0&page={page}',
                  headers={'User-Agent': ua})
   sleep(2)
   soup = BeautifulSoup(response.text, 'html.parser')
   # print(soup)
   lis = soup.find_all('a', class_="title")
   BVList = []
   for element in lis:
       BVList.append('https:' + element['href'])
       print(element['href'])
   for url in BVList:
       main.get_video(url)
       index += 1
       print(index)


for page in range(1, 51):
   response = get(f'https://search.bilibili.com/all?keyword=%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6&order=totalrank&duration=1&tids_1=0&page={page}',
                  headers={'User-Agent': ua})
   sleep(2)
   soup = BeautifulSoup(response.text, 'html.parser')
   lis = soup.find_all('a', class_="title")
   BVList = []
   for element in lis:
       BVList.append('https:' + element['href'])
       print(element['href'])
   for url in BVList:
       main.get_video(url)
       index += 1
       print(index)

for page in range(1, 51):
    response = get(
        f'https://search.bilibili.com/all?keyword=%E6%B5%99%E6%B1%9F%E5%A4%A7%E5%AD%A6&order=totalrank&duration=2&tids_1=0&page={page}',
        headers={'User-Agent': ua})
    sleep(2)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    lis = soup.find_all('a', class_="title")
    BVList = []
    for element in lis:
        BVList.append('https:' + element['href'])
        print(element['href'])
    for url in BVList:
        main.get_video(url)
        index += 1
        print(index)

