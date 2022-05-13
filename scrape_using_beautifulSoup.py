# scrape realtime currency rates 
from bs4 import BeautifulSoup

def get_currency(in_currency, out_currency):
  url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
  print(url)

get_currency("USD","EUR")
