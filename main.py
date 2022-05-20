from scrape_using_beautifulSoup import main_bsoup
from scrape_using_selenium import main_selenium
from rest_apis_in_python import main_news
from weather_forecast_api import main_weather
# from grammer_correction_api import main_grammer

#import rest_apis_in_python
#import weather_forecast_api
#import create_rest_api.py
# import grammar_correction_api


file = input("Choose file.\n\nPress a: Scrape ecommerce store using Selenium \n\nPress b: Scrape realtime currency (JPY,USD) using BeautifulSoup\n\nPress c: Use News API to request news articles from news sources and blogs across the web.User can choose topic, time period and language (de/en)\n\nPress d: Request weather forecast for the next 5 days using a weather api (https://openweathermap.org/forecast5).User can choose city and language (en/de).Data(city,time,temperature,sky condition) is append into a .txt-file (filenname: weather.txt)\n\n>> your choice: ")

             
if file == "a": 
  main_selenium()
elif file == "b":
  main_bsoup()
elif file == "c":
  main_news()
elif file == "d":
  main_weather()
else: 
  print("no file selected")

