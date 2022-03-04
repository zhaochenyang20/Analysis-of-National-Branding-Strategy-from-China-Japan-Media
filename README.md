# Crawlers

## 核心文件说明

### RJNews.py

- 使用清华大学账号登录

- 从清华大学数据库爬取日本经济新闻的相关内容（这个真的可以说吗）
- 使用`selenium`模拟点击和下载

### AsahiNews.py

- 从`requests`朝日新闻官网按关键词爬取新闻列表，存到本地json
- 使用预先购买的购买朝日新闻会员账号，从浏览器登录后复制cookie到info.json

### RMNews.py

- 先从人民网API请求新闻，存入数据库
- 再用`requests`请求页面，将响应存入数据库

### NHK.py

- 先爬取列表数据存入`nhk.json`
- 再从NHK官网爬取新闻，存到本地

### core.py

- 一些公共函数

# Parsers

## 核心文件说明

- Fall_2021 与 Spring_2022_Part_One 为 2021 年秋季学期与 2022 年春季学期处理人民日报的工作目录。主要工作文件为 soup.py ，该部分代码耦合程度较高，但是成功处理了爬取出的 html 文件，并且将数据储存在了 hex.sql 或者 result 目录下
- Winter_2022_Part_One 与 Winter_2022_Part_Three 分别处理了日经新闻的夏奥会部分与冬奥会部分。这部分代码较为解耦合，主要的工作文件仍然为 soup.py，原始数据为 RJnews 文件夹，中间转录数据为 pieces 文件夹，而最后的结果为 results 文件夹
- Winter_2022_Part_Two 与 Winter_2022_Part_Four 分别处理了朝日新闻的夏奥会部分与冬奥会部分。这部分代码较为解耦合，主要的工作文件仍然为 soup.py，原始数据为 AsahiNews 文件夹，最后的结果为 results 文件夹

## 主要函数

- metric 为函数装饰器，用于输出函数的执行信息与执行时长
- get_list 利用 os.listdir 返回了某个一级文件夹下的所有文件名字的列表，便于随后读取 html 文件
- check_duplication 用于去除重复的新闻，日经新闻重复较多，而朝日新闻较少
- parese_and_check_duplication 为针对单个 html 的测试函数
- prettify 用于将 html 文件美化，便于可视化以辅助切割
- html_cut_emain 与 html_cut_scorll 用于解读日经新闻，因为日经新闻一个文件下有 400 个新闻，故而需要按照 emain 和 scorll 这两个  class 来切分出每一个新闻
- soup_each_piece_of_news 用于将 cut 完成后的新闻拆分读取，工作原理同 parese_and_check_duplication
- deduplicate_and_identify 用于将某个目录下的重复文件提出
- test 为针对某个列表里文件来查询重复次数的测试函数

# Visualization

- lu_Spring 文件夹下的 processDataInJapan.py 用于统计日本媒体新闻中的关键词出现次数

- refactorJsons.py 用于将之前格式并不完善的 Json 文件重构，并且添加日期

- AddAllTheTxt.py 将中文新闻和日语新闻所有 Json 文件合并成一个文件（由于存在 一些非 Json 文件，Windows cmd 中的 Copy 功能会失败，使用鲁棒性更高的 try-except 语句进行处理，跳过文件小于 5 份）

- calculateYumiuhu.py 统计读卖 Json 文件列表中字典个数并求和

- cloudWords.py 导入已生成的词频数目和图片轮廓（冰墩墩）生成词云图

- divideTheLanguageChinaAndJapan.py 检测内容是否包含平假名的 ASCII 码，从而将 18098 份文件分离为中文新闻和日语新闻（中文新闻：8646 份，日语新闻：9452 份）

- drawDNAGraphs.py 导入 getSpecificWordFrequency.py 中生成的词频，并依据两者公用的全局变量绘制 DNA 图（横轴代表时间，纵轴代表不同关键词，颜色透明度代表该词在某段时间内出现的频率）

- getRank.py 导入 processDataInJapan.py 中生成的内容、标题频次（以字典列表的形式存储），为后续计算饼状图和柱状图的“其他”类别，将字典排序，生成三维列表

- getSpecificWordFrequency.py 在 refactor 后的文件中统计给定关键词的在不同时间段的频次，生成字典列表

- graphPieAndColumn.py 处理 getRank.py 中生成的三维列表，生成带有“其他”类别的 list1,list2，分别传入绘制饼状图和柱状图函数中，批量生成对应图表

- processDataInJapan.py 预处理 Scanner.xlsx 中不同 sheet 中不同列关键词在中文新闻和日语新闻中出现的次数总和，使用 Counter() 计数器。最开始处理时约有 15% 的数据丢失，调查原因发现 content 有时写成 context ，使用连续的 try-except 语句达到 0-2 错误量，同时促进了 Json 文件的重构

- refactorJsons.py 将 Json 文件中所有的 key 值统一“度量衡”，同时使用正则表达式查询的方法提取出 time 或 date 中年月日，以八位整型的方式存储在 date 中，以便后续计算词频随时间分布
