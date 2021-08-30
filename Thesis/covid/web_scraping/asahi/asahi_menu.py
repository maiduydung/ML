# Import Module
from bs4 import BeautifulSoup
import requests
html = requests.get('https://www.asahi.com/ajw/articles/14427323')
soup = BeautifulSoup(html.text,'html.parser')


news_article = soup.find(['div'], class_='ArticleTitle').find('h1')
news_article = [string for string in news_article.stripped_strings][0]

news_writer = soup.find(['p'], class_='EnArticleName')
news_writer = [string for string in news_writer.stripped_strings][0]

news_written_date =  soup.find(['p'], class_='EnLastUpdated')
news_written_date = [string for string in news_written_date.stripped_strings][0]

news_text =  soup.find(['div'], class_='ArticleText')
news_text = [string for string in news_text.stripped_strings] #multiple elements, each of them is a str

temp = ''
for i in news_text:
    temp = temp + " " + i
news_text = temp







