import os
import requests
# from datetime import datetime
import datetime

#api_key for spacenews.com
my_secret = os.environ['api_key']


def get_news(topic, from_date, to_date, language="en", api_key=my_secret):
  # request news articles save response in a list
  url = f'https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}'
  response_data = requests.get(url)
  response = response_data.json()
  articles = response["articles"]
  print(f"Total results: {len(articles)}")

  #print(articles)
#  news_articles = []
 # file = open("articles.txt","w")
 # for article in articles:
   # news_articles.append(f'\n\ntitle: {article["title"]} \nDescription: {article["description"]}')
  #  news_articles.append(article)
   # file.write(f'\nTitle: {article["title"]} \nDescription: {article["description"]}')
 # file.close()
  return articles

def check_period(from_date, to_date):
  # check if period of dates not greater than one month 
  from_date_obj = datetime.datetime.strptime(from_date,"%Y-%m-%d")
  current_date = datetime.datetime.now()
  date_delta_obj = current_date - from_date_obj
  days = date_delta_obj.days
  max_days_30 = 30
  max_days_31 = 31
  print(f"date_delta_obj: {date_delta_obj},\ndays:{days},\ntype days:{type(days)}")
  if int(days) >= max_days_30: 
    if int(days) > max_days_31:
      return False
    else: 
      return True
  else:
    return True


def filter_articles(articles):
  # keys: url, author, title, description, publishedAt - '2022-05-03T22:38:39Z', content, urlToImage
  print("first article title:", articles[0]["title"])
  print("first article author:", articles[0]["author"])
  print("first article content:", articles[0]["content"])
  




def main_news():
# get user choice 
  topic = input("Choose news topic (space / austria / united states /):  ")
  from_date = input("Choose start date in yyy-mm-dd format: ")
  to_date = input("Choose to date in yyy-mm-dd format: ") 
  language = input("Choose language (en/de): ")
  period_is_eligible = check_period(from_date,to_date)
  if period_is_eligible:
    articles = get_news(topic, from_date, to_date, language)
    filter_articles(articles)
  else:
    print("Period of dates not eligible.\nYou can only search articles up to one month in the past ")
  

main_news()

