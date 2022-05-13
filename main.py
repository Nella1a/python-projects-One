#import main() from scrape_using_beautifulSoup
from scrape_using_beautifulSoup import main_bsoup
from scrape_using_selenium import main_selenium
#from rest_apis_in_python import main_api


file = input("Choose file: \nPress a: Scrape ecommerce store using Selenium \nPress b: Scrape realtime currency using BeautifulSoup \nPress c: Working with REST API\n ->> your choice: ")

             
if file == "a": 
  main_selenium()
elif file == "b":
  main_bsoup()
#elif file == "c":
#  rest_apis_in_python.main
else: 
  print("no file selected")

  