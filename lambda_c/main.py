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


def slp():
    t = settings['sleep'] + random.uniform(0, settings['uniform_max'])
    print(f"sleep {t}s")
    sleep(t)


def nap():
    sleep(settings['small_interval'])


def get_page(url: str):
    header = {
        'User-Agent': random.choice(ua_list),
        'Referer': url,
        'Cookie': settings['cookie']
    }

    res = ses.get(url, headers=header)

    if res.status_code != 200:
        return res.status_code

    try:
        content = str(res.content, "gbk")
    except:
        try:
            content = str(res.content, "utf-8")
        except:
            return -2  # decode error

    with conn.cursor() as cur:
        sql = "INSERT INTO raw(html_content, url) VALUES ('" + es(content) + "', '" + url + "');"
        cur.execute(sql)
    conn.commit()
    return 200


# get_page("http://ent.people.com.cn/n1/2021/1013/c1012-32251747.html")

# with conn.cursor() as cur:
#     sql = "SELECT * FROM raw WHERE ID = 0;"
#     cur.execute(sql)
#     print(str(cur.fetchone()[1], "utf-8"))


def get_search_list(kw: str):

    def record_page(p_res):
        for j in p_res['data']['records']:
            with conn.cursor() as cur:
                sql = f"INSERT INTO urls(kw, url, title) VALUES('{es(kw)}', '{j['url']}', '{es(j['title'])}')"
                cur.execute(sql)
        conn.commit()

    url_encoded = p.quote(kw.encode('gb2312'))
    time_stamp = int(round(time.time() * 1000))
    post_url = "http://search.people.cn/api-search/front/search"
    headers = {
        'User-Agent': random.choice(ua_list),
        'Referer': f"http://search.people.cn/s?keyword={url_encoded}&st=0&_={time_stamp}",
        'Cookie': settings['search_cookie'],
        'Content-Type': 'application/json'
    }

    contents = '{"key":"%s","page":%d,"limit":100,"hasTitle":true,"hasContent":true,"isFuzzy":false,"type":0,"sortType":0,"startTime":1625068800000,"endTime":1630425599000}'

    initial = ses.post(url=post_url, headers=headers, data=(contents % (kw, 1)).encode("utf-8"))

    try:
        res = json.loads(str(initial.content, "utf-8"))
    except:
        print(str(initial.content, "utf-8"))
        exit(-1)


    if res['code'] != "0":
        print(f"Initial request for {kw} unsuccessful on code {res['code']} with:\n {res['data']} \n Abort.")
        exit(res['code'])

    pages = res['data']['pages']
    print(f"Initial request for {kw} successful, {pages} page(s) in total")
    record_page(res)

    for i in range(2, pages + 1):
        slp()
        print(f"Now begin on page {i}")
        req = ses.post(url=post_url, headers=headers, data=(contents % (kw, i)).encode("utf-8"))
        res = json.loads(str(req.content, "utf-8"))

        if res['code'] != "0":
            print(f"Request for {kw} unsuccessful on code {res['code']} with:\n {res['data']} \n Abort.")
            exit(res['code'])
        record_page(res)


def get_keywords():
    res = []
    with conn.cursor() as cur:
        cur.execute("SELECT ID, kw, done FROM kw")
        res = cur.fetchall()

    print(res)

    for k in [i for i in res]:
        if k[2] is not None:
            continue

        print("Ready to launch search for", k[1])
        with conn.cursor() as cur:
            cur.execute("UPDATE kw SET begin = 1 WHERE ID=" + str(k[0]))
        get_search_list(k[1])
        with conn.cursor() as cur:
            cur.execute("UPDATE kw SET done = 1 WHERE ID=" + str(k[0]))


def get_unloaded_raw_pages():
    global intercept_cnt
    with conn.cursor() as cur:
        cur.execute("SELECT title, url FROM urls WHERE ISNULL(loaded) AND kw='奥运' GROUP BY title ORDER BY ID")
        res = cur.fetchall()

    for item in res:
        try:
            status = get_page(item[1])
        except:
            with conn.cursor() as cur:
                cur.execute(f"UPDATE urls SET loaded=-1 WHERE title='{item[0]}'")
            conn.commit()
            print("Exception @", item[1])
            continue

        if status == 403:
            intercept_cnt += 1
            if intercept_cnt >= 10:
                for i in range(7):
                    sleep(60)
            continue

        elif status == 200:
            intercept_cnt = 0

        with conn.cursor() as cur:
            cur.execute(f"UPDATE urls SET loaded={status} WHERE title='{item[0]}'")
        conn.commit()
        print("title", item[0], "url", item[1], status)
        slp()

get_unloaded_raw_pages()
