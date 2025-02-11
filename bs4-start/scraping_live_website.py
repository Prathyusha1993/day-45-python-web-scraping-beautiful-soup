from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
print(soup.title)

articles = soup.find_all(name='a', class_='storylink')
article_texts = []
article_links = []

for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.get('href')
    article_links.append(link)


article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)

# print(article_texts[largest_index])
print(article_texts)
print(article_links)
# print(article_links[largest_index])
print(article_upvote)

# print(int(article_upvote[0].split()[0]))


