# scrape realtime currency rates 
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
  # get url with currency request, get response, find currency and print only float
  url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
  resp = requests.get(url).text
  soup = BeautifulSoup(resp, "html.parser")
  rate = soup.find("span",class_="ccOutputRslt").get_text()
  rate = float(rate.split(" ")[0]) # different option: rate[: -4]
  return rate

current_rate = get_currency("JPY","USD")
print(current_rate)


# https://developers.google.com/adsense/management/appendix/currencies.csv