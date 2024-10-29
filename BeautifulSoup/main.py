from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web = response.text

soup = BeautifulSoup(yc_web, "html.parser")

# first_article = soup.select_one(selector=".titleline>a")
# print(first_article)
# article_title = first_article.getText()
# print(article_title)
# article_link = first_article.get("href")
# print(article_link)
# article_upvote = soup.select_one(".score").getText()
# print(article_upvote)

articles = soup.select(selector=".titleline>a")
list_of_titles = [article.getText() for article in articles]
list_of_links = [article.get("href") for article in articles]
article_votes = soup.select(".score")
list_of_scores = [int(score.getText().split()[0]) for score in article_votes]

max_score = max(list_of_scores)
index = list_of_scores.index(max_score)

print(list_of_titles[index])
print(list_of_links[index])
print(list_of_scores[index])


# with open("./website.html") as website:
#     contents = website.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title.string)
#
# all_anchor_tags = soup.find_all("a")
#
# for tag in all_anchor_tags:
#     text = tag.getText()
#     link = tag.get("href")
#     # print(link)
#
# heading3 = soup.find(name="h3", class_="heading")
# # print(heading3)
#
# company_url = soup.select_one(selector="p a")
# # print(company_url)
#
# all_headings = soup.select(selector=".heading")
# print(all_headings)
