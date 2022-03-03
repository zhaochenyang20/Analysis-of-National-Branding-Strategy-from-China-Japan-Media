# -*-coding:utf8-*-

import requests
import requests
import json
from time import sleep
import random
import core
from bs4 import BeautifulSoup as b
import re
from pymysql.converters import escape_string as es
import time
import asyncio
from pyppeteer import launch
import sys
import os
from urllib import parse as p

ua_list = core.load_ua()
conn = core.load_mysql()
settings = core.load_settings()

intercept_cnt = 0

ses = requests.session()

kw = '冬奥'

url_encoded = p.quote(kw.encode('gb2312'))
time_stamp = int(round(time.time() * 1000))
post_url = "http://search.people.cn/api-search/front/search"
headers = {
    'User-Agent': random.choice(ua_list),
    'Referer': f"http://search.people.cn/s?keyword={url_encoded}&st=0&_={time_stamp}",
    'Cookie': settings['search_cookie'],
    'Content-Type': 'application/json'
}

contents = '{"key":"%s","page":%d,"limit":100,"hasTitle":true,"hasContent":true,"isFuzzy":false,"type":0,"sortType":0,"startTime":1633017600000,"endTime":0}'

initial = ses.post(url=post_url, headers=headers, data=(contents % (kw, 1)).encode("utf-8"))

print(str(initial.content, "utf-8"))

every = json.loads(str(initial.content, "utf-8"))

res = json.loads(str(initial.content, "utf-8"))['data']['records']

print(len(res))
print(every['data']['total'])


for i in res:
    print(i['title'], i['displayTime'])


# with conn.cursor() as cur:
#     sql = "SELECT * FROM raw WHERE ID = 2276;"
#     cur.execute(sql)
#     print(str(cur.fetchone()[1], "utf-8"))

