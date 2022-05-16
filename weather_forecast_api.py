# https://openweathermap.org/
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
  with open("weather","a") as file: 
    for weather in forecast:
      # extract from response: city, date, temperature, sky condition 
      file.write(f'{response_city},{weather["dt_txt"]},{weather["main"]["temp"]},{weather["weather"][0]["description"]}\n')
  file.close()

def main_weather():
  city = input("city: ")
  lang = input("language (en/de): ")
  get_weather(city, lang)

main_weather()

