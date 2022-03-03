import requests as r
import json
from copy import deepcopy as dc
from urllib import parse
from time import sleep
import random
from pathlib import Path
from tqdm import tqdm
import sys

proxies = {
        'http': 'socks5h://127.0.0.1:1080',
        'https': 'socks5h://127.0.0.1:1080'
}
with open('info.json', encoding='utf-8') as f:
    common_headers = json.load(f)


def get_list(keyword: str, page_init: int = 0, page_max: int = 1e10):
    urls = []
    rec_num_corase = 0
    headers = dc(common_headers)
    headers['Referer'] = f"https://sitesearch.asahi.com/sitesearch/?Keywords={parse.quote(keyword)}&Searchsubmit2=%E6%90%9C%E7%B4%A2&Searchsubmit=%E6%A4%9C%E7%B4%A2&iref=pc_ss_date&sort=2&start={page_init}"
    while True:
        json_request_url = "https://sitesearch.asahi.com/sitesearch-api/?Keywords=%s&start=%d&sort=2" % (parse.quote(keyword), page_init)
        succ = False
        res = None
        while not succ:
            try:
                res = r.get(json_request_url, headers=headers, proxies=proxies)
                succ = True
            except:
                sleep(20)

        lst = json.loads(str(res.content, encoding='utf-8'))['goo']
        total_num = int(lst['hit_num']['num'])
        rec_num_corase += int(lst['range']['paging_size'])
        print("keyword %s, record %d, sleep 1s" % (keyword, int(lst['range']['to'])))
        page_init = int(lst['range']['to']) + 1
        urls += [i['URL'] for i in lst['docs']]
        if rec_num_corase >= total_num or page_init >= page_max:
            break
        sleep(2)

    print('obtained ', urls.__len__(), 'URLs')
    return urls

def get_all_html_dictionary():
    return [l.__str__() for l in Path().iterdir()]

def get_and_process_page(url_list: list):
    current_html = get_all_html_dictionary()
    for url in tqdm(url_list):
        file_name = url.replace('https://digital.asahi.com/articles/', '')
        if file_name in current_html:
            continue

        succ = False
        resp = None
        while not succ:
            try:
                resp = r.get(url, proxies=proxies, headers=common_headers).text
                succ = True
            except:
                sleep(20)

        sleep(1.5 + random.uniform(0.5, 1))
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(resp)

def report_undefined_pattern(url: str):
    with open('undefined_patters.txt', 'a') as f:
        f.write(url + '\n')
        print('undefined pattern', url)



if len(sys.argv) == 2 and sys.argv[1] == '--local':
    with open('temp_list.json', 'r') as f:
        lst = json.load(f)
else:
    lst = get_list('五輪', 0, 2000)
    with open('temp_list.json', 'w') as f:
        json.dump(lst, f)
        print('list serialized')

filtered_lst = []
for l in lst:
    n = l.replace('https://www.asahi.com/articles/', 'https://digital.asahi.com/articles/')
    if n == l:
        report_undefined_pattern(l)
    else:
        trash = n.replace('.html', '')
        if trash == n:
            report_undefined_pattern(l)
        else:
            filtered_lst += [n]

get_and_process_page(filtered_lst)
