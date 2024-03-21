# program to find the most upvoted news from https://news.ycombinator.com/

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
tags = soup.find_all(name="span", class_="titleline")

tag_titles = []
tag_links = []

for tag in tags:
    tag_text = tag.select_one("a").getText()
    tag_titles.append(tag_text)
    tag_link = tag.select_one("a").get_attribute_list("href")
    if tag_link:
        tag_links.append(tag_link[0])

tag_upvotes = soup.find_all(name="span", class_="score")

score = 0
upvote_list = []
for upvote in tag_upvotes:
    tag_upvote = int(upvote.getText().split()[0])
    upvote_list.append(tag_upvote)
    if tag_upvote > score:
        score = tag_upvote

index = upvote_list.index(score) if score in upvote_list else -1
print(tag_titles[index], tag_links[index])
