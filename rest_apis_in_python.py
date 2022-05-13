import requests


url = 'https://newsapi.org/v2/everything?qInTitle=austria&from=2022-5-01&to=2022-5-10&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c'

response_data = requests.get(url)
response = response_data.json()
#print(response["articles"])


print(response["articles"][0]["title"])

