#import main() from scrape_using_beautifulSoup
# from scrape_using_beautifulSoup import main_bsoup
# from scrape_using_selenium import main_selenium
# from rest_apis_in_python import main_news
# from weather_forecast_api import main_api
# from grammer_correction_api import main_grammer

#import rest_apis_in_python
#import weather_forecast_api
#import create_rest_api.py
import grammer_correction_api
"""

file = input("Choose file: \n

Press a: Scrape ecommerce store using Selenium \n


Press b: Scrape realtime currency using BeautifulSoup \nPress c: Working with REST APIs\n

Press d:\nRequest weather forecast for the next 5 days from a weather api (https://openweathermap.org/forecast5).\nUser can choose city and language (en or de).\nData(city,time,temperature,sky condition) is appended into a .txt-file (filenname: weather.txt)\n>> your choice: ")


             
if file == "a": 
  main_selenium()
elif file == "b":
  main_bsoup()
#elif file == "c":
#  main_news()
elfif file =="d":
  main_api()
else: 
  print("no file selected")

"""