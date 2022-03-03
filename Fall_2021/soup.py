import pymysql as sql
import json
from bs4 import BeautifulSoup as bp


def load_mysql():
    with open("sql_login.json") as f:
        sql_login = json.loads(f.read())
    return sql.connect(**sql_login)
# 加载mysql配置


conn = load_mysql()


def anal_bbs1(id, soup, url):
    with conn.cursor() as cur:
        sql_commit = f"UPDATE raw SET parsed = 0 where ID = {id};"
        cur.execute(sql_commit)
    conn.commit()

#不是硬编码的网页现在直接set pharsed=0，然后跳过

def anal_cjkeizai(id, soup, url):
    with conn.cursor() as cur:
        sql_commit = f"UPDATE raw SET parsed = 1 where ID = {id};"
        cur.execute(sql_commit)
    conn.commit()
    title_h1 = soup.findAll('h1')
    for piece in title_h1:
        if piece.get_text() != '':
            title = piece.get_text()
    print(title)
    content = soup.find('div', class_='txt clearfix').get_text()
    # print(content)
    info = soup.find('div', class_=["day", ]).get_text()
    # print(info)
    with conn.cursor() as cur:
        sql_commit = f"INSERT INTO news_content(title, content, info, url, id) VALUES ('{title}', '{content}','{info}','{url}', '{id}');"
        cur.execute(sql_commit)
    conn.commit()
    dic = {'title': title, 'content': content, 'info': info, 'url': url, 'id': id, }
    return dic


#ent和world共用一个函数
def anal_ent(id, soup, url):
    with conn.cursor() as cur:
        sql_commit = f"UPDATE raw SET parsed = 1 where ID = {id};"
        cur.execute(sql_commit)
    conn.commit()
    title_h1 = soup.findAll('h1')
    for piece in title_h1:
        if piece.get_text() != '':
            title = piece.get_text()
    #print(title)
    try:
        content = soup.find('div', class_='rm_txt_con').get_text()
    except:
        content = soup.find("div", class_='text_con w1000 clearfix').get_text()
    #print(content)
    try:
        info = soup.find('div', class_='col-1-1').get_text()
    except:
        info = soup.find('h4').get_text()
    #print(info)
    with conn.cursor() as cur:
        sql_commit = f"INSERT INTO news_content(title, content, info, url, id) VALUES ('{title}', '{content}','{info}','{url}', '{id}');"
        cur.execute(sql_commit)
    conn.commit()
    dic = {'title': title, 'content': content, 'info': info, 'url': url, 'id': id, }
    return dic


def anal_sc(id, soup, url):
    with conn.cursor() as cur:
        sql_commit = f"UPDATE raw SET parsed = 1 where ID = {id};"
        cur.execute(sql_commit)
    conn.commit()
    title_h1 = soup.findAll('h1')
    for piece in title_h1:
        if piece.get_text() != '':
            title = piece.get_text()
    print(title)
    try:
        content = soup.find('div', class_='text_con_left').get_text()
    except:
        try:
            content = soup.find('div', class_='rm_txt_con').get_text()
        except:
            content = soup.find("div", class_= 'content clear clearfix').get_text()
    #print(content)
    try:
        info = soup.find('div', class_="box01").get_text()
    except:
        try:
            info = soup.find('div', class_="col-1-1").get_text()
        except:
            info = soup.find('div', class_=["fl", ]).get_text()
    #print(info)
    with conn.cursor() as cur:
        sql_commit = f"INSERT INTO news_content(title, content, info, url, id) VALUES ('{title}', '{content}','{info}','{url}', '{id}');"
        cur.execute(sql_commit)
    conn.commit()
    dic = {'title': title, 'content': content, 'info': info, 'url': url, 'id': id, }
    return dic


def anal_acftu(id, soup, url):
    with conn.cursor() as cur:
        sql_commit = f"UPDATE raw SET parsed = 1 where ID = {id};"
        cur.execute(sql_commit)
    conn.commit()
    title_h1 = soup.findAll('h1')
    for piece in title_h1:
        if piece.get_text() != '':
            title = piece.get_text()
    print(title)
    content = soup.find('div', class_='show_text').get_text()
    # print(content)
    info = soup.find('p', class_="text_dot_line").get_text()
    #print(info)
    with conn.cursor() as cur:
        sql_commit = f"INSERT INTO news_content(title, content, info, url, id) VALUES ('{title}', '{content}','{info}','{url}', '{id}');"
        cur.execute(sql_commit)
    conn.commit()
    dic = {'title': title, 'content': content, 'info': info, 'url': url, 'id': id, }
    return dic


def anal_japan(id, soup, url):
    with conn.cursor() as cur:
        sql_commit = f"UPDATE raw SET parsed = 1 where ID = {id};"
        cur.execute(sql_commit)
    conn.commit()
    title_h1 = soup.findAll('h1')
    for piece in title_h1:
        if piece.get_text() != '':
            title = piece.get_text()
    print(title)
    content = soup.find('div', class_="fl text_con_left").get_text()
    # print(content)
    try:
        info = soup.find('div', class_="fl").get_text()
    except:
        info = soup.find('h4').get_text()
    #print(info)
    with conn.cursor() as cur:
        sql_commit = f"INSERT INTO news_content(title, content, info, url, id) VALUES ('{title}', '{content}','{info}','{url}', '{id}');"
        cur.execute(sql_commit)
    conn.commit()
    dic = {'title': title, 'content': content, 'info': info, 'url': url, 'id': id, }
    return dic


def anal_cpc(id, soup, url):
    with conn.cursor() as cur:
        sql_commit = f"UPDATE raw SET parsed = 1 where ID = {id};"
        cur.execute(sql_commit)
        conn.commit()
    title_h1 = soup.findAll('h1')
    for piece in title_h1:
        if piece.get_text() != '':
            title_1 = piece.get_text()
    title_h2 = soup.findAll('h1')
    for piece in title_h2:
        if piece.get_text() != '':
            title_2 = piece.get_text()
    title = title_1 + title_2
    print(title)
    content = soup.find('div', class_="show_text").get_text()
    #print(content)
    info = soup.find('p', class_="sou").get_text()
    print(info)
    with conn.cursor() as cur:
        sql_commit = f"INSERT INTO news_content(title, content, info, url, id) VALUES ('{title}', '{content}','{info}','{url}', '{id}');"
        cur.execute(sql_commit)
    conn.commit()
    dic = {'title': title, 'content': content, 'info': info, 'url': url, 'id': id, }
    return dic



with conn.cursor(sql.cursors.DictCursor) as cur:
    sql_commit = "SELECT * FROM raw;"
    # where url = 'http://sc.people.com.cn/n2/2021/0831/c345167-34892908.html'
    cur.execute(sql_commit)
    all_news = cur.fetchall()


for each_news in all_news:
    news_content = each_news["html_content"]
    url = each_news["url"]
    identity = each_news["ID"]
    soup = bp(str(news_content, "utf-8"),'html.parser')
    try:
        if url.find("v.") != -1 or url.find('api.weibo') != -1:
            continue
        if url.find("bbs1") != -1:
            anal_bbs1(identity, soup, url)
        elif url.find("cjkeizai") != -1:
            dic = anal_cjkeizai(identity, soup, url)
        elif url.find("ent") != -1 or url.find("world") != -1 or url.find("yjy") != -1 or url.find("society") != -1 or \
                url.find("health") != -1 or url.find("finance") != -1 or url.find("zj") != -1 or\
                url.find("military") != -1 or url.find("politics") != -1 or url.find("opinion") != -1 or url.find("spfjc")\
                != -1:
            dic = anal_ent(identity, soup, url)
        elif url.find("acftu") != -1:
            dic = anal_acftu(identity, soup, url)
        elif url.find("japan") != -1:
            dic = anal_japan(identity, soup, url)
        elif url.find("cpc") != -1:
            dic = anal_cpc(identity, soup, url)
        else:
            dic = anal_sc(identity, soup, url)
        print(f'right url {url}')
        name = dic['title']
        print(name)
        with open(f'./result/{name}.json', 'w+', encoding='utf-8') as f:
            json.dump(dic, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(e)
        print(f'wrong url {url}')
