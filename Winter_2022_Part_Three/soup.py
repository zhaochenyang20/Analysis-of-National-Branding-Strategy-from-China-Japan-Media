import json
from bs4 import BeautifulSoup
from tqdm import tqdm
import os
import typing
import functools
import time
from IPython import embed


source_dir = "./RJnews"
result_dir = "./results_winter_olympic"
test_txt = "./test.txt"
test_json = "./test.json"
test_html = "./test.html"
trans_dir = "./pieces"


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('start executing %s' % (fn.__name__))
        start_time = time.time()
        result = fn(*args, **kw)
        end_time = time.time()
        t = 1000 * (end_time - start_time)
        print('%s executed in %s ms' % (fn.__name__, t))
        return result
    return wrapper


@metric
def get_list(target):
    dirs = os.listdir(target)
    file_list = []
    for file in dirs:
         file_list.append(f"./{target}/{file}")
    return file_list


@metric
def html_cut_emain(file_list):
    num = 0
    for file in tqdm(file_list):
        with open(file, 'r', encoding = "utf-8", errors='ignore') as f:
            html_content = f.read()
            soup = BeautifulSoup(html_content, "lxml")
            all_emain = soup.findAll(class_ = "nk-gv-bodytitlemain")
            for emain in tqdm(all_emain):
                try:
                    with open(f"./{trans_dir}/{num}.txt", 'w', encoding = "utf-8", errors='ignore') as t:
                        t.write(f"{emain!r}")
                        for sibling in emain.next_siblings:
                            if sibling in all_emain:
                                break
                            t.write(f"{sibling!r}")
                    num = num + 1
                except Exception as e:
                    print(e)
                    continue
# here we have cut all html into pieces by class tag nk-gv-bodytitlemain


@metric
def html_cut_scorll(file_list):
    num = 0
    for file in tqdm(file_list):
        with open(file, 'r', encoding="utf-8", errors='ignore') as f:
            html_content = f.read()
            soup = BeautifulSoup(html_content, "lxml")
            all_scroll = soup.findAll(class_="nk-gv-bodyscroll-on")
            for scroll in tqdm(all_scroll):
                with open(f"./{trans_dir}/{num}.txt", 'a+', encoding="utf-8", errors='ignore') as t:
                    t.write(f"{scroll!r}")
                    for sibling in scroll.next_siblings:
                        if sibling in all_scroll:
                            break
                        t.write(f"{sibling!r}")
                num = num + 1


@metric
def soup_each_piece_of_news(file_list):
    failure = 1
    result_num = 1
    dic_for_dedupulicate = {}
    for file_name in tqdm(file_list):
        with open(file_name, "r", encoding="utf-8", errors='ignore') as f:
            try:
                html_content = f.read()
            except Exception as e:
                print(f"reading failed {failure}")
                failure = failure + 1
                continue
            soup = BeautifulSoup(html_content, "lxml")
            try:
                title = soup.find(class_ = "nk-gv-bodytitle").get_text().strip()
            except Exception as e:
                print(e)
                print(file_name)
                print(f"find bodytitle failed {failure}")
                failure = failure + 1
                title = "no title"
            try:
                info = soup.find(class_ = "nk-gv-attribute").get_text().strip()
            except Exception as e:
                print(e)
                print(file_name)
                print(f"find attribute failed {failure}")
                failure = failure + 1
                info = "no info"
            try:
                context_list = soup.findAll(class_ = "nk-gv-bodyscroll-on")
                context = ""
                for sentence in context_list:
                    context = context + sentence.get_text().strip() + "\r"
            except Exception as e:
                print(e)
                print(file_name)
                print(f"find context failed {failure}")
                failure = failure + 1
                context = "no context"
            dic = {}
            dic["title"] = title
            dic["info"] = info
            dic["context"] = context
            store_postion = result_dir + f"/{title}.json"
            try:
                dic_for_dedupulicate[f"{title}"] = dic_for_dedupulicate[f"{title}"] + 1
            except:
                dic_for_dedupulicate[f"{title}"] = 0
            try:
                with open(store_postion, mode = 'w', encoding = "utf-8") as t:
                    json.dump(dic, t, ensure_ascii = False, indent = 2)
            except Exception as e:
                print(f"json dump failed {failure}")
                failure = failure + 1
                print(e)
            result_num = result_num + 1
    print(f"success result {result_num}")
    print(dic_for_dedupulicate)


@metric
def deduplicate_and_identify(file_list):
    num = 0
    for file in tqdm(file_list):
        try:
            with open(file, "r", encoding="utf-8") as f:
                dic = json.load(f)
                dic["identity"] = num
                num = num + 1
            with open(file, "w", encoding="utf-8") as t:
                json.dump(dic, t, ensure_ascii=False, indent=2)
        except Exception as e:
            print(e)
            continue
# we can not read and rewrite a json file in one "with open" operation


@metric
def test(file_list):
    failure = 1
    result_num = 1
    dic_for_dedupulicate = {}
    for file_name in tqdm(file_list):
        with open(file_name, "r", encoding="utf-8") as f:
            try:
                html_content = f.read()
            except Exception as e:
                print(f"reading failed {failure}")
                failure = failure + 1
                continue
            soup = BeautifulSoup(html_content, "lxml")
            try:
                title = soup.find(class_ = "nk-gv-bodytitle").get_text().strip()
            except Exception as e:
                print(e)
                print(file_name)
                print(f"find bodytitle failed {failure}")
                failure = failure + 1
                title = "no title"
            try:
                info = soup.find(class_ = "nk-gv-attribute").get_text().strip()
            except Exception as e:
                print(e)
                print(file_name)
                print(f"find attribute failed {failure}")
                failure = failure + 1
                info = "no info"
            try:
                context_list = soup.findAll(class_ = "nk-gv-bodyscroll-on")
                context = ""
                for sentence in context_list:
                    context = context + sentence.get_text().strip() + "\r"
            except Exception as e:
                print(e)
                print(file_name)
                print(f"find context failed {failure}")
                failure = failure + 1
                context = "no context"
            dic = {}
            dic["title"] = title
            dic["info"] = info
            dic["context"] = context
            try:
                store_name = context[-20 : ]
            except:
                store_name = context
            store_postion = result_dir + f"/{store_name}.json"
            try:
                dic_for_dedupulicate[f"{store_name}"] = dic_for_dedupulicate[f"{store_name}"] + 1
            except:
                dic_for_dedupulicate[f"{store_name}"] = 0
            try:
                with open(store_postion, "a", encoding = "utf-8") as t:
                    json.dump(dic, t, ensure_ascii = False, indent = 2)
            except Exception as e:
                print(f"json dump failed {failure}")
                failure = failure + 1
                print(e)
            result_num = result_num + 1
    print(f"success result {result_num}")
    print(dic_for_dedupulicate)


@metric
def prettify(file):
    with open(file, "r", encoding="utf-8") as f:
        try:
            html_content = f.read()
        except Exception as e:
            print(f"reading failed")
            return
        soup = BeautifulSoup(html_content, "lxml").prettify()
        with open(test_txt, "w", encoding = "utf-8") as t:
            t.write(soup)


if __name__ == '__main__':
    html_cut_emain(get_list(source_dir))
    html_cut_scorll(get_list(source_dir))
    soup_each_piece_of_news(get_list(trans_dir))
    # test(get_list(trans_dir))
    # deduplicate_and_identify(get_list(result_dir))
    # prettify(test_html)
