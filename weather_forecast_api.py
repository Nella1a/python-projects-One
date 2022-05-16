# Request weather forecast for the next 5 days from a weather api (https://openweathermap.org/forecast5).
# User can choose city and language (en or de)
# Data (City,Time,Temperature,Condition) is appended into a .txt-file (filenname: weather.txt)


import requests
import os

api_key = os.environ["udemy_weatherApp"]

def get_weather(city,lang,metric="metric",api_key=api_key):
  url=f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={metric}&lang={lang}"
  response_data = requests.get(url)
  # print(response_data)
  response = response_data.json()
  # print(response)
  response_city = response["city"]["name"]
  forecast = response["list"]
  with open("weather.txt","a") as file: 
    for weather in forecast:
      # extract from response: city, date, temperature, sky condition 
      file.write(f'{response_city},{weather["dt_txt"]},{weather["main"]["temp"]},{weather["weather"][0]["description"]}\n')
  file.close()

def main_weather():
  city = input("city: ")
  lang = input("language (en/de): ")
  get_weather(city, lang)

# main_weather()

