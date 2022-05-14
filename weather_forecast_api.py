# https://openweathermap.org/
import requests

api_key='26631f0f41b95fb9f5ac0df9a8f43c92'

def get_weather(city,lang,api_key=api_key):
  url=f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric&lang={lang}"
  response_data = requests.get(url)
  print(response_data)
  response = response_data.json()
  print(response)
  response_city = response["city"]["name"]
  forecast = response["list"]
  file = open("weather.txt","a")
  for weather in forecast:
    file.write(f'{response_city},{weather["dt_txt"]},{weather["main"]["temp"]},{weather["weather"][0]["description"]}\n\n')
  file.close()

def main_weather():
  print("hello")
  city = input("city: ")
  lang = input("language (en/de): ")
  # get_weather(city, lang)
  get_weather(city, lang)



main_weather()

