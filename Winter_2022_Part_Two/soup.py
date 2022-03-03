import json
from bs4 import BeautifulSoup
from tqdm import tqdm
import os
import typing
from IPython import embed
import functools
import time


source_dir = "./AsahiNews"
result_dir = "./results_summer_olympic"
test_txt = "./test.txt"
test_json = "./test.json"
test_html = "./test.html"


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
def check_duplication(file_list):
    failure = 1
    result_num = 0
    dic_for_dedupulicate = {}
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


            # content
            try:
                content = soup.find(class_="ArticleText").get_text().strip() \
                    .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")

            except:
                try:
                    content = soup.findAll("p")
                    trans_list = []
                    for piece in content:
                        trans_list.append(piece.get_text().strip() \
                                          .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ",
                                                                                                               ""))
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
                author_name = soup.find(class_="Sub").get_text().strip() \
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
                date = soup.find("time").get_text().strip() \
                    .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
            except Exception as e:
                print(e)
                print(file)
                print(f"find date failed {failure}")
                failure += 1
                date = "no date"
            dic = {}
            dic["title"] = title
            dic["content"] = content
            dic["date"] = date
            dic["author"] = author_name
            store_name = title
            store_position = result_dir + f"/{store_name}.json"
            try:
                with open(store_position, "a", encoding="utf-8") as t:
                    json.dump(dic, t, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"json dump failed {failure}")
                failure = failure + 1
                print(e)


        # deduplicate
        try:
            dic_for_dedupulicate[title] += 1
        except:
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


        # content
        try:
            content = soup.find(class_ = "ArticleText").get_text().strip()\
                .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")

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
        embed()
        print(content)


        # author
        try:
            author_name = soup.find(class_ = "Sub").get_text().strip()\
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
        try:
            date = soup.find("time").get_text().strip() \
                .replace(u'\u3000', u'').replace('\n', '').replace('\r', '').replace(" ", "")
        except Exception as e:
            print(e)
            print(file)
            print(f"find date failed {failure}")
            failure += 1
            date = "no date"
        dic = {}
        dic["title"] = title
        dic["content"] = content
        dic["date"] = date
        dic["author"] = author_name
        store_name = title
        store_position = result_dir + f"/{store_name}.json"
        try:
            with open(store_position, "a", encoding = "utf-8") as t:
                json.dump(dic, t, ensure_ascii = False, indent = 2)
        except Exception as e:
            print(f"json dump failed {failure}")
            failure = failure + 1
            print(e)


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

# some html is arranged out of typical "ArticleText". Maybe you should ask c7w for help.


if __name__ == '__main__':
    check_duplication(get_list(source_dir))
    # parese_and_check_duplication(test_html)
    # prettify(test_html)
