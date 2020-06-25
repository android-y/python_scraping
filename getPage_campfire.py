# coding: utf-8
import requests
# import pprint
from bs4 import BeautifulSoup
# import re
import pickle
from slack_notify import slack_post

url = "https://camp-fire.jp/projects/category/technology"
html = requests.get(url)
# print(html.text)

soup = BeautifulSoup(html.text, "html.parser")
# pprint.pprint(column)

with open("/mnt/c/Users/android/practice/campfiretag.pickle", "rb") as f:
    tags = pickle.load(f)

# tags = []
count = 0
for projectid in soup("div", class_="box-in"):
    tag = projectid.get("data_project_id")
    if tag in tags:
        pass
    else:
        tags.append(tag)
        count += 1
        box = projectid.find("div", class_="box-title")
        box2 = box.find("a")
        title = box2.get("title")
        url = box2.get("href")
        # print(tag)
        slack_post(title + ": https://camp-fire.jp" + url)

if count == 0:
    slack_post("新着記事はありません")

with open("/mnt/c/Users/android/practice/campfiretag.pickle", "wb") as f:
    pickle.dump(tags, f)

