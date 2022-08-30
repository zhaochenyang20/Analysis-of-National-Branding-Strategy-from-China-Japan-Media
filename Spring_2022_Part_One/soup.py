import json
from bs4 import BeautifulSoup
from tqdm import tqdm
import os
import typing
from IPython import embed
import functools
import time
from collections import Counter


source_dir = "./rm_winter"
result_dir = "./results_winter_olympic_人民日报"
test_txt = "./test.txt"
test_json = "./test.json"
test_html = "./test.html"
trans_dir = "./transfer"


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('start executing %s' % (fn.__name__))
        start_time = time.time()
        result = fn(*args, **kw
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
def transfer(file_list):
    num = 0
    for file in tqdm(file_list):
        with open(file, "r", encoding="utf-8") as f:
            try:
                meta_web = json.load(f)["html_content"]
            except Exception as e:
                print("reading failed")
                continue
            soup = BeautifulSoup(meta_web, "lxml").prettify()
            with open(f"{trans_dir}/{num}.html", "w", encoding="utf-8") as t:
                t.write(soup)
                num += 1

@metric
def check_duplication(file_list):
    failure = 1
    dic_for_dedupulicate = Counter()
    for file in tqdm(file_list):
        with open(file, "r", encoding="utf-8") as f:

            # title
            try:
                html_content = f.read()
            except Exception as e:
                print(f"reading failed")
                return
            soup = BeautifulSoup(html_content, "lxml")
            try:
                title = soup.find("title").get_text().strip() \
                    .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            except Exception as e:
                print(e)
                print(file)
                print(f"find title failed {failure}")
                failure = failure + 1
                title = "no title"

            # contentexit
            try:
                content = "".join(soup.find(class_="show_text").get_text().strip() \
                                  .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "").split())
                content = "".join(content.split())
            except:
                try:
                    content = soup.findAll("p")
                    trans_list = []
                    for piece in content:
                        trans_list.append(piece.get_text().strip() \
                                          .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", ""))
                    try:
                        split = soup.find(class_="showCommentIcon").get_text().strip() \
                            .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
                        split_position = trans_list.index(split)
                    except:
                        try:
                            split = soup.find(class_="RelatedListMod").get_text().strip() \
                                .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
                            split_position = trans_list.index(split)
                        except:
                            split_position = len(trans_list)
                    trans_list = trans_list[:split_position]
                    content = [i for i in trans_list if i != '']
                    content = ",".join(content)
                except Exception as e:
                    print(e)
                    print(file)
                    print(f"find content failed {failure}")
                    failure = failure + 1
                    content = "no content"

            # author
            try:
                author_name = soup.find(class_="edit").get_text().strip() \
                    .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            except:
                try:
                    author_name = soup.find(class_="H8KYB").get_text().strip() \
                        .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
                except Exception as e:
                    print(e)
                    print(file)
                    print(f"find author failed {failure}")
                    failure += 1
                    author_name = "no author"

            # date
            try:
                date = "".join(soup.find(class_="sou").get_text().strip() \
                               .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ",
                                                                                                    "").split())
                if date == "":
                    date = "".join(soup.find(class_="col-1-1 fl").get_text().strip() \
                                   .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ",
                                                                                                        "").split())
                if date == "":
                    date = "".join(soup.find(class_="col-1-1").get_text().strip() \
                                   .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ",
                                                                                                        "").split())
            except Exception as e:
                try:
                    date = "".join(soup.find(class_="col-1-1 fl").get_text().strip() \
                                   .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ",
                                                                                                        "").split())
                    if date == "":
                        date = "".join(soup.find(class_="col-1-1").get_text().strip() \
                                       .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ",
                                                                                                            "").split())
                except:
                    try:
                        date = "".join(soup.find(class_="col-1-1").get_text().strip() \
                                       .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ",
                                                                                                            "").split())
                    except:
                        try:
                            date = "".join(soup.find(class_="publishtime").get_text().strip() \
                                           .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "").split())
                        except:
                            pass
                if date == "":
                    print(f"find date failed {failure}")
                    failure += 1
                    continue
                    date = "no date"
            dic = {}
            dic["title"] = title
            dic["content"] = content
            dic["date"] = date
            dic["author"] = author_name
            store_position = result_dir + f"/{title}.json"
            try:
                with open(store_position, "w+", encoding="utf-8", errors="ignore") as t:
                    json.dump(dic, t, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"json dump failed {failure}")
                failure = failure + 1
                print(e)


            # deduplicate
            dic_for_dedupulicate[title] = 1
    print(dic_for_dedupulicate)


@metric
def parese_and_check_duplication(file):
    failure = 1
    with open(file, "r", encoding="utf-8") as f:


        # title
        try:
            html_content = f.read()
        except Exception as e:
            print(f"reading failed")
            return
        soup = BeautifulSoup(html_content, "lxml")
        try:
            title = soup.find("title").get_text().strip()\
                    .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
        except Exception as e:
            print(e)
            print(file)
            print(f"find title failed {failure}")
            failure = failure + 1
            title = "no title"


        # content text
        try:
            content = "".join(soup.find(class_="show_text").get_text().strip() \
                           .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "").split())
            content = "".join(content.split())
        except:
            try:
                content = soup.findAll("p")
                trans_list = []
                for piece in content:
                    trans_list.append(piece.get_text().strip()\
                    .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", ""))
                try:
                    split = soup.find(class_ = "showCommentIcon").get_text().strip()\
                    .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
                    split_position = trans_list.index(split)
                except:
                    try:
                        split = soup.find(class_ = "RelatedListMod").get_text().strip()\
                        .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
                        split_position = trans_list.index(split)
                    except:
                        split_position = len(trans_list)
                trans_list = trans_list[:split_position]
                content = [i for i in trans_list if i != '']
                content = ",".join(content)
            except Exception as e:
                print(e)
                print(file)
                print(f"find content failed {failure}")
                failure = failure + 1
                content = "no content"


        # author
        try:
            author_name = soup.find(class_ = "edit").get_text().strip()\
                .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
        except:
            try:
                author_name = soup.find(class_ = "H8KYB").get_text().strip()\
                .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            except Exception as e:
                print(e)
                print(file)
                print(f"find author failed {failure}")
                failure += 1
                author_name = "no author"


        # date
        date = ""
        try:
            date = "".join(soup.find(class_="sou").get_text().strip() \
                .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "").split())
            if date == "":
                date = "".join(soup.find(class_="col-1-1 fl").get_text().strip() \
                .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "").split())
            if date == "":
                date = "".join(soup.find(class_="col-1-1").get_text().strip() \
                .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "").split())
        except:
            try:
                date = "".join(soup.find(class_="col-1-1 fl").get_text().strip() \
                               .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "").split())
                if date == "":
                    date = "".join(soup.find(class_="col-1-1").get_text().strip() \
                           .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "").split())
            except:
                try:
                    date = "".join(soup.find(class_="col-1-1").get_text().strip() \
                               .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "").split())
                except:
                    try:
                        date = "".join(soup.find(class_="publishtime").get_text().strip() \
                                   .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "").split())
                    except:
                        date == ""
                        pass
        if date == "":
            print(f"find date failed {failure}")
            failure += 1
            date = "no date"
        dic = {}
        dic["title"] = title
        dic["content"] = content
        dic["date"] = date
        dic["author"] = author_name
        store_position = result_dir + f"/{title}.json"
        try:
            with open(store_position, "a", encoding = "utf-8", errors="ignore") as t:
                json.dump(dic, t, ensure_ascii = False, indent = 2)
        except Exception as e:
            print(f"json dump failed {failure}")
            failure = failure + 1
            print(e)
        embed()


@metric
def prettify(file):
    with open(file, "r", encoding="utf-8") as f:
        try:
            meta_web = json.load(f)["html_content"]
        except Exception as e:
            print("reading failed")
            return
        soup = BeautifulSoup(meta_web, "lxml").prettify()
        with open(test_txt, "w", encoding = "utf-8") as t:
            t.write(soup)

# some html is arranged out of typical "ArticleText". Maybe you should ask c7w for help.


if __name__ == '__main__':
    check_duplication(get_list(trans_dir))
    # parese_and_check_duplication(test_html)
    # prettify(test_json)
    # transfer(get_list(source_dir))