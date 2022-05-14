import os
import requests

#api_key for spacenews.com
my_secret = os.environ['api_key']


def get_news(topic, from_date, to_date, language="en", api_key=my_secret):
  # request news articles, save articles into a list and txt file
  url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
  response_data = requests.get(url)
  response = response_data.json()
  articles = response["articles"]
  print(articles)
  news_articles = []
  file = open("articles.txt","w")
  for article in articles:
    news_articles.append(f'\n\ntitle: {article["title"]} \nDescription: {article["description"]}')
    file.write(f'\nTitle: {article["title"]} \nDescription: {article["description"]}')
  file.close()
  return news_articles
  

def main_news():
# get user news choice 
  topic = input("Choose news topic (space / austria / united states /):  ")
  from_date = input("Choose start date in yyy-mm-dd format: ")
  to_date = input("Choose to date in yyy-mm-dd format: ") 
  language = input("Choose language (en/de: ")
  get_news(topic, from_date, to_date, language)
  

main_news()

