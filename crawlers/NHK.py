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
import sys
import os
from urllib import parse as p

ua_list = core.load_ua()
conn = core.load_mysql()
settings = core.load_settings()

intercept_cnt = 0

ses = requests.session()

with open('nhk.json', 'rb') as f:
    str_content = str(f.read(), "utf-8")


def get_raw_pages(url: str, index: int):
    header = {
        'User-Agent': random.choice(ua_list),
        'Referer': url
    }

    res = ses.get(url, headers=header)

    with open(f'./raw/{index}.html', 'wb') as file:
        file.write(res.content)


lib = json.loads(str_content)
index = 0
for item in lib:
    print(f"begin getting {index} from {item['Url']}")
    get_raw_pages(item['Url'], index)
    index += 1
    t = 1 + random.uniform(0, 1)
    print(f"now begin to sleep {t} seconds")
    sleep(t)



