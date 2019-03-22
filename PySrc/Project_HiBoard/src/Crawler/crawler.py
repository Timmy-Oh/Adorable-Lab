from bs4 import BeautifulSoup
import bs4
import urllib.request
import urllib.parse
import requests
import re

# 2018-01-01 ~ 2019-03-21
startNo, endNo = 78000, 570000
with open('./cw_db.tsv', 'w', encoding='utf-8') as f:
    for docNo in range(startNo, endNo+1):
        try:
            home_url = "https://www1.president.go.kr/petitions/" + str(docNo)
            soup = BeautifulSoup(urllib.request.urlopen(home_url).read(), 'html.parser')
            article = soup.select('div.petitionsView_left_pg')[0]
            #vars
            title = article.select('h3.petitionsView_title')[0].text.strip()
            agree = article.select('h2.petitionsView_count')[0].select('span.counter')[0].text.strip()
            infobox = article.select('ul.petitionsView_info_list')[0].text
            category = re.findall('카테고리(.*)', infobox)[0].strip()
            date_start = re.findall('청원시작(.*)', infobox)[0].strip()
            date_end = re.findall('청원마감(.*)', infobox)[0].strip()
            content = article.select('div.View_write')[0].text
            content = re.sub('\s+', ' ', content).strip()
            print(docNo, category, date_start, date_end, agree, title, content[:20])
            res = "\t".join([str(docNo), category, date_start, date_end, agree, title, content])
            f.write(res + "\n")
            # break

        except Exception as e:
            print("Error : ", e)
